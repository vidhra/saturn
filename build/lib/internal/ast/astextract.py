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
      - function
        - name
        - description
        - parameters (as JSON schema)
        - request_types

    The parameters are drawn from both:
      1. The function signature (positional + keyword-only arguments).
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
                        # Prepare a JSON-schema style structure
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

                        # Get the docstring
                        docstring = ast.get_docstring(item) or ""
                        stripped_docstring = docstring.strip()[:1024]

                        # 3) From docstring: identify request message like MoveBillingAccountRequest
                        request_types = re.findall(
                            r"Request message for\s*``([^`]+)``", docstring
                        )

                        # Force each extracted type to end with "Request"
                        # e.g. "TestIamPermissions" -> "TestIamPermissionsRequest"
                        updated_request_types = []
                        for rt in request_types:
                            if not rt.endswith("Request"):
                                updated_request_types.append(rt + "Request")
                            else:
                                updated_request_types.append(rt)

                        # 4) Parse docstring lines for param lines of the form:
                        #      name (:class:`str`):
                        #          Some description
                        #    You can adjust the regex to match your docstring conventions
                        param_pattern = re.compile(
                            r"^\s*(\w+)\s*\(\s*\:class\:\`(.*?)\`\)\:\s*(.*)$"
                        )

                        doc_lines = docstring.splitlines()
                        # We'll keep a buffer for multi-line descriptions
                        param_name_in_progress = None
                        param_desc_in_progress = []

                        for line in doc_lines:
                            match = param_pattern.match(line)
                            if match:
                                # If we were already collecting lines for a previous param, finalize it
                                if param_name_in_progress:
                                    # finalize the previous parameter
                                    # Merge back into 'properties' if it exists, otherwise create
                                    existing = properties.get(param_name_in_progress, {})
                                    existing["description"] = (
                                        existing.get("description", "") 
                                        + " " + " ".join(param_desc_in_progress)
                                    ).strip()
                                    properties[param_name_in_progress] = existing
                                    param_name_in_progress = None
                                    param_desc_in_progress = []

                                param_name, param_type, param_desc = match.groups()

                                # Initialize or update the property
                                existing = properties.get(param_name, {})
                                # let the docstring's param type override "string" if desired
                                existing["type"] = param_type or "string"
                                # doc param line might have an initial short description
                                existing["description"] = param_desc.strip()
                                properties[param_name] = existing

                                # Mark that we can keep reading for multi-line desc
                                param_name_in_progress = param_name
                                param_desc_in_progress = []
                            else:
                                # If we are continuing the doc for a param
                                if param_name_in_progress:
                                    param_desc_in_progress.append(line.strip())

                        # If the docstring ended but we still had an in-progress param
                        if param_name_in_progress:
                            existing = properties.get(param_name_in_progress, {})
                            existing["description"] = (
                                existing.get("description", "")
                                + " "
                                + " ".join(param_desc_in_progress)
                            ).strip()
                            properties[param_name_in_progress] = existing

                        # Build final method info
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
            break  # Found the class; no need to continue searching
    return extracted_methods

def main():
    # Adjust these paths as needed for your environment
    metadata_path = r"C:\Users\AMD\vidhra\internal\ast\google-cloud-python\packages\google-cloud-billing\google\cloud\billing_v1\gapic_metadata.json"
    client_file = r"C:\Users\AMD\vidhra\internal\ast\google-cloud-python\packages\google-cloud-billing\google\cloud\billing_v1\services\cloud_billing\async_client.py"

    metadata = load_gapic_metadata(metadata_path)

    # For the async client, use the "grpc-async" metadata.
    grpc_async_metadata = metadata["services"]["CloudBilling"]["clients"]["grpc-async"]
    rpcs = grpc_async_metadata["rpcs"]

    # Gather all method names mentioned in the metadata
    target_methods = set()
    for rpc_name, details in rpcs.items():
        for method in details.get("methods", []):
            target_methods.add(method)

    # The async client class to scan
    class_name = "CloudBillingAsyncClient"

    # Extract definitions from the Python source
    methods_info = extract_methods_from_file(client_file, class_name, target_methods)

    # Write results to JSON
    output_file = "extracted_async_methods.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(methods_info, f, indent=2)

    print(f"Extracted method information saved to {output_file}")

if __name__ == "__main__":
    main()
