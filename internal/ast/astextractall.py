import os
import json
import ast
import re

def load_gapic_metadata(metadata_file):
    """Load the GAPIC metadata JSON file."""
    with open(metadata_file, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_methods_from_file(file_path, class_name, target_methods):
    """
    Parse the given file and extract methods from the specified class.
    Only methods whose names are in target_methods are extracted.

    Returns a list of dictionaries with keys:
      - type
      - function:
          - name
          - description
          - parameters (as JSON schema)
          - request_types

    Parameters are extracted from:
      1. The function signature (positional and keyword-only arguments).
      2. Docstring parameter lines of the form:
            name (:class:`some_type`):
                Some description
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    # Parse the source code into an AST
    tree = ast.parse(source, file_path)
    extracted_methods = []

    # Search for the target class
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            # Look through all methods in this class
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    method_name = item.name

                    # Only extract if the method is in our target list
                    if method_name in target_methods:
                        properties = {}
                        required = []

                        # 1) From function signature: treat each arg as a string property
                        #    ignoring "self" or "cls"
                        for arg in item.args.args:
                            if arg.arg not in ("self", "cls"):
                                properties[arg.arg] = {
                                    "type": "string",
                                    "description": ""
                                }
                                required.append(arg.arg)

                        # 2) Keyword-only arguments
                        for arg in item.args.kwonlyargs:
                            properties[arg.arg] = {
                                "type": "string",
                                "description": ""
                            }
                            required.append(arg.arg)

                        # Get the docstring (limited to 1024 characters)
                        docstring = ast.get_docstring(item) or ""
                        stripped_docstring = docstring.strip()[:1024]

                        # 3) Extract the request type from the first parameter's annotation
                        updated_request_types = []
                        # Look for a parameter named "request"
                        for arg in item.args.args:
                            if arg.arg == "request" and arg.annotation is not None:
                                # Use ast.unparse to get the string representation of the annotation.
                                annotation_str = ast.unparse(arg.annotation)
                                # Look for a type that ends with "Request". This handles annotations like:
                                # Optional[Union[functions.ListFunctionsRequest, dict]]
                                matches = re.findall(r"([a-zA-Z_][\w\.]*Request)", annotation_str)
                                if matches:
                                    updated_request_types.extend(matches)
                                break  # We only check the first occurrence of "request"

                        # Fallback: if no request type was found via the annotation,
                        # try extracting from the docstring.
                        if not updated_request_types:
                            request_types = re.findall(
                                r"Request(?: message)? for\s*``([^`]+)``", docstring
                            )
                            for rt in request_types:
                                if not rt.endswith("Request"):
                                    updated_request_types.append(rt + "Request")
                                else:
                                    updated_request_types.append(rt)

                        # 4) Parse docstring lines for parameter lines of the form:
                        #      name (:class:`str`):
                        #          Some description
                        param_pattern = re.compile(
                            r"^\s*(\w+)\s*\(\s*\:class\:\`(.*?)\`\)\:\s*(.*)$"
                        )
                        doc_lines = docstring.splitlines()
                        param_name_in_progress = None
                        param_desc_in_progress = []

                        for line in doc_lines:
                            match = param_pattern.match(line)
                            if match:
                                if param_name_in_progress:
                                    # Finalize previous parameter description
                                    existing = properties.get(param_name_in_progress, {})
                                    existing["description"] = (
                                        existing.get("description", "") + " " +
                                        " ".join(param_desc_in_progress)
                                    ).strip()
                                    properties[param_name_in_progress] = existing
                                    param_name_in_progress = None
                                    param_desc_in_progress = []

                                param_name, param_type, param_desc = match.groups()
                                existing = properties.get(param_name, {})
                                existing["type"] = param_type or "string"
                                existing["description"] = param_desc.strip()
                                properties[param_name] = existing

                                param_name_in_progress = param_name
                                param_desc_in_progress = []
                            else:
                                if param_name_in_progress:
                                    param_desc_in_progress.append(line.strip())

                        # Finalize any remaining parameter
                        if param_name_in_progress:
                            existing = properties.get(param_name_in_progress, {})
                            existing["description"] = (
                                existing.get("description", "") + " " +
                                " ".join(param_desc_in_progress)
                            ).strip()
                            properties[param_name_in_progress] = existing

                        # Build final method information
                        method_info = {
                            "type": "function",
                            "function": {
                                "name": method_name,
                                "description": stripped_docstring,
                                "parameters": {
                                    "type": "object",
                                    "properties": properties,
                                    "required": required
                                },
                                "request_types": updated_request_types
                            }
                        }
                        extracted_methods.append(method_info)
            break  # Stop after processing the target class
    return extracted_methods


def camel_to_snake(name):
    """Convert CamelCase to snake_case."""
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

def process_package(metadata_path):
    """
    For a given gapic_metadata.json file, load the metadata, extract the target methods
    for each grpc-async client, locate the corresponding async_client.py file,
    and extract the relevant functions.
    Returns a dictionary keyed by service name.
    """
    results = {}
    package_dir = os.path.dirname(metadata_path)
    metadata = load_gapic_metadata(metadata_path)

    for service_name, service_metadata in metadata.get("services", {}).items():
        clients = service_metadata.get("clients", {})
        grpc_async = clients.get("grpc-async")
        if not grpc_async:
            continue

        # Extract target methods from the RPC definitions
        rpcs = grpc_async.get("rpcs", {})
        target_methods = set()
        for rpc_name, details in rpcs.items():
            for method in details.get("methods", []):
                target_methods.add(method)
        if not target_methods:
            continue

        # Construct the expected path to the async client file.
        service_folder = camel_to_snake(service_name)
        client_file = os.path.join(package_dir, "services", service_folder, "async_client.py")
        if not os.path.exists(client_file):
            print(f"Warning: {client_file} not found for service {service_name}")
            continue

        # Assume the async client class name is the service name with 'AsyncClient' appended.
        class_name = service_name + "AsyncClient"
        methods_info = extract_methods_from_file(client_file, class_name, target_methods)

        results[service_name] = {
            "methods": methods_info
        }
    return results

def process_all_packages(base_directory):
    """
    Recursively search for gapic_metadata.json files under the base directory,
    process each package to extract async client methods, and save each package's results
    in its own folder.
    """
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == "gapic_metadata.json":
                metadata_path = os.path.join(root, file)
                package_results = process_package(metadata_path)
                if package_results:
                    # Create an output folder within the package directory
                    working_dir = r"/Users/prashanthvarma/Saturn/internal/ast"
                    output_dir = os.path.join(working_dir, "extracted_methods")
                    tools_dir = os.path.join(output_dir, metadata_path.split("/")[-2])
                    os.makedirs(tools_dir, exist_ok=True)
                    output_file = os.path.join(tools_dir, "tools.json")
                    with open(output_file, "w", encoding="utf-8") as f:
                        json.dump(package_results, f, indent=2)
                    print(f"Extracted async method information saved to {output_file}")

def main():
    # Set the base directory for the packages.
    base_directory = r"/Users/prashanthvarma/Saturn/internal/ast/google-cloud-python/packages"
    
    # Process each package and save the results in its own folder.
    process_all_packages(base_directory)

if __name__ == "__main__":
    main()
