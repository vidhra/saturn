import os
import json
import ast
import re

# ---------------------------
# Shared utility functions
# ---------------------------
def load_gapic_metadata(metadata_file):
    with open(metadata_file, "r", encoding="utf-8") as f:
        return json.load(f)

def camel_to_snake(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

# ---------------------------
# Tools Code: Extract async client methods
# ---------------------------
def extract_methods_from_file(file_path, class_name, target_methods, type_registry=None):
    """
    Extract methods from the given class.
    If a method's docstring declares a request type and that type is present in the type_registry,
    then the method's parameters (originally derived from the signature) will be replaced
    by the detailed parameters extracted from the types.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source, file_path)
    extracted_methods = []

    # Find the target class in the AST.
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            # Loop over each method in the class.
            for item in node.body:
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    method_name = item.name
                    if method_name in target_methods:
                        properties = {}
                        required = []

                        # (1) From function signature: add each argument (ignoring "self"/"cls")
                        for arg in item.args.args:
                            if arg.arg not in ("self", "cls"):
                                properties[arg.arg] = {"type": "string", "description": ""}
                                required.append(arg.arg)
                        for arg in item.args.kwonlyargs:
                            properties[arg.arg] = {"type": "string", "description": ""}
                            required.append(arg.arg)

                        # (2) Get and trim the docstring.
                        docstring = ast.get_docstring(item) or ""
                        stripped_docstring = docstring.strip()[:1024]

                        # (3) Extract declared request types from the docstring.
                        request_types = re.findall(r"Request message for\s*``([^`]+)``", docstring)
                        updated_request_types = []
                        for rt in request_types:
                            if not rt.endswith("Request"):
                                updated_request_types.append(rt + "Request")
                            else:
                                updated_request_types.append(rt)

                        # (4) Further update parameters from docstring lines (if present).
                        param_pattern = re.compile(r"^\s*(\w+)\s*\(\s*\:class\:\`(.*?)\`\)\:\s*(.*)$")
                        doc_lines = docstring.splitlines()
                        param_name_in_progress = None
                        param_desc_in_progress = []

                        for line in doc_lines:
                            match = param_pattern.match(line)
                            if match:
                                if param_name_in_progress:
                                    existing = properties.get(param_name_in_progress, {})
                                    existing["description"] = (
                                        existing.get("description", "") + " " + " ".join(param_desc_in_progress)
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

                        if param_name_in_progress:
                            existing = properties.get(param_name_in_progress, {})
                            existing["description"] = (
                                existing.get("description", "") + " " + " ".join(param_desc_in_progress)
                            ).strip()
                            properties[param_name_in_progress] = existing

                        # Build the initial method info using the extracted arguments.
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

                        # -------------
                        # NEW: If a request type is declared and exists in the type registry,
                        # replace the parameters with the detailed schema from the types extraction.
                        if type_registry and updated_request_types:
                            for rt in updated_request_types:
                                if rt in type_registry:
                                    method_info["function"]["parameters"] = type_registry[rt]
                                    break
                        # -------------

                        extracted_methods.append(method_info)
            break  # Stop after processing the target class.
    return extracted_methods

def process_package(metadata_path, type_registry=None):
    """
    Process a package: load its gapic metadata, extract target methods from the async client,
    and (if available) use the type_registry to provide detailed parameter information.
    """
    results = {}
    package_dir = os.path.dirname(metadata_path)
    metadata = load_gapic_metadata(metadata_path)

    for service_name, service_metadata in metadata.get("services", {}).items():
        clients = service_metadata.get("clients", {})
        grpc_async = clients.get("grpc-async")
        if not grpc_async:
            continue

        # Collect target method names from the RPC definitions.
        rpcs = grpc_async.get("rpcs", {})
        target_methods = set()
        for rpc_name, details in rpcs.items():
            for method in details.get("methods", []):
                target_methods.add(method)
        if not target_methods:
            continue

        # Locate the async client file.
        service_folder = camel_to_snake(service_name)
        client_file = os.path.join(package_dir, "services", service_folder, "async_client.py")
        if not os.path.exists(client_file):
            print(f"Warning: {client_file} not found for service {service_name}")
            continue

        # Assume the async client class name is the service name with 'AsyncClient' appended.
        class_name = service_name + "AsyncClient"
        methods_info = extract_methods_from_file(client_file, class_name, target_methods, type_registry=type_registry)
        results[service_name] = {"methods": methods_info}
    return results

# ---------------------------
# Types Extraction Code
# ---------------------------
def convert_type(type_str, type_registry=None):
    type_str = type_str.strip()
    # Handle array types.
    if type_str.startswith("MutableSequence[") or type_str.startswith("List["):
        inner = type_str[type_str.find("[") + 1: -1]
        inner_schema = convert_type(inner, type_registry)
        return {"type": "array", "items": inner_schema}
    # Handle mapping types.
    if type_str.startswith("MutableMapping[") or type_str.startswith("Dict["):
        inner = type_str[type_str.find("[") + 1: -1]
        parts = [p.strip() for p in inner.split(",")]
        if len(parts) == 2:
            value_schema = convert_type(parts[1], type_registry)
            return {"type": "object", "additionalProperties": value_schema}
        else:
            return {"type": "object"}
    # Map built-in types.
    simple_mappings = {"str": "string", "int": "integer", "float": "number", "bool": "boolean"}
    if type_str in simple_mappings:
        return {"type": simple_mappings[type_str]}
    # Otherwise, assume a custom type.
    simple_name = type_str.split('.')[-1]
    if type_registry and simple_name in type_registry:
        return {"reference": type_str}
    return {"type": "object", "reference": type_str}

def resolve_nested_references(schema, type_registry, path=None):
    if path is None:
        path = []
    if "reference" in schema:
        ref = schema["reference"]
        simple_name = ref.split('.')[-1]
        if simple_name in path:
            return schema  # Circular reference detected.
        new_path = path + [simple_name]
        if simple_name in type_registry:
            inlined_schema = resolve_nested_references(type_registry[simple_name], type_registry, new_path)
            return inlined_schema
        else:
            return schema
    if schema.get("type") == "object":
        new_schema = dict(schema)
        if "properties" in new_schema:
            new_props = {}
            for key, prop_schema in new_schema["properties"].items():
                new_props[key] = resolve_nested_references(prop_schema, type_registry, path)
            new_schema["properties"] = new_props
        if "additionalProperties" in new_schema:
            new_schema["additionalProperties"] = resolve_nested_references(new_schema["additionalProperties"], type_registry, path)
        return new_schema
    if schema.get("type") == "array" and "items" in schema:
        new_schema = dict(schema)
        new_schema["items"] = resolve_nested_references(schema["items"], type_registry, path)
        return new_schema
    return schema

def extract_types_from_file(file_path, type_registry=None, filter_requests=False):
    """
    Extract message (and enum) types from the given file.
    When filter_requests is True, only classes ending with "Request" are processed (and enums are skipped).
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    tree = ast.parse(source, file_path)
    extracted = []
    attr_pattern = re.compile(r"^\s*(\w+)\s*\(\s*([\w\[\], \.]+)\)\:\s*(.*)$")
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            base_names = [base.id for base in node.bases if isinstance(base, ast.Name)]
            base_attrs = [f"{base.value.id}.{base.attr}" for base in node.bases 
                          if isinstance(base, ast.Attribute) and hasattr(base.value, "id")]
            all_bases = base_names + base_attrs
            is_message = any("proto.Message" in b for b in all_bases)
            is_enum = any("proto.Enum" in b for b in all_bases)
            if not (is_message or is_enum):
                continue

            class_name = node.name
            if filter_requests:
                if is_message and not class_name.endswith("Request"):
                    continue
                if is_enum:
                    continue

            docstring = ast.get_docstring(node) or ""
            docstring_truncated = docstring.strip()[:1024]

            if is_message:
                raw_attributes = {}
                doc_lines = docstring.splitlines()
                in_attributes_section = False
                current_attr = None
                current_desc_lines = []
                for line in doc_lines:
                    if "Attributes:" in line:
                        in_attributes_section = True
                        continue
                    if in_attributes_section:
                        match = attr_pattern.match(line)
                        if match:
                            if current_attr:
                                existing = raw_attributes.get(current_attr, {})
                                existing["description"] = (existing.get("description", "") +
                                                           " " + " ".join(current_desc_lines)).strip()
                                raw_attributes[current_attr] = existing
                                current_attr = None
                                current_desc_lines = []
                            attr_name, attr_type, attr_desc = match.groups()
                            attr_name = attr_name.strip()
                            attr_type = attr_type.strip()
                            raw_attributes[attr_name] = {
                                "raw_type": attr_type,
                                "description": attr_desc.strip()
                            }
                            current_attr = attr_name
                            current_desc_lines = []
                        else:
                            if current_attr:
                                current_desc_lines.append(line.strip())
                if current_attr:
                    existing = raw_attributes.get(current_attr, {})
                    existing["description"] = (existing.get("description", "") +
                                               " " + " ".join(current_desc_lines)).strip()
                    raw_attributes[current_attr] = existing

                schema_properties = {}
                required_fields = []
                for attr_name, details in raw_attributes.items():
                    converted_type = convert_type(details["raw_type"], type_registry) if details.get("raw_type") else {"type": "string"}
                    resolved_type = resolve_nested_references(converted_type, type_registry) if type_registry else converted_type
                    if details["description"].lstrip().startswith("Required"):
                        required_fields.append(attr_name)
                    schema_properties[attr_name] = {"description": details["description"], **resolved_type}
                parameters_schema = {"type": "object", "properties": schema_properties}
                if required_fields:
                    parameters_schema["required"] = required_fields
                extracted.append({
                    "type": "function",  # Treat messages like functions for schema purposes.
                    "name": class_name,
                    "description": docstring_truncated,
                    "parameters": parameters_schema
                })
            elif is_enum:
                enum_values = {}
                for item in node.body:
                    if isinstance(item, ast.Assign):
                        if len(item.targets) == 1 and isinstance(item.targets[0], ast.Name):
                            key = item.targets[0].id
                            if key.startswith("_"):
                                continue
                            if hasattr(item.value, "value"):
                                value = item.value.value
                            elif hasattr(item.value, "n"):
                                value = item.value.n
                            else:
                                continue
                            enum_values[key] = {"value": value}
                extracted.append({
                    "type": "enum",
                    "name": class_name,
                    "description": docstring_truncated,
                    "values": enum_values
                })
    return extracted

def build_type_registry(base_directory):
    """
    Recursively search for gapic_metadata.json files under the base directory,
    and process each package’s 'types' directory to build a global type registry.
    The registry maps the simple class names (e.g. CreateInstanceRequest) to their JSON schema.
    """
    registry = {}
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == "gapic_metadata.json":
                metadata_path = os.path.join(root, file)
                package_dir = os.path.dirname(metadata_path)
                types_dir = os.path.join(package_dir, "types")
                if os.path.isdir(types_dir):
                    for root2, _, files2 in os.walk(types_dir):
                        for file2 in files2:
                            if file2.endswith(".py"):
                                file_path = os.path.join(root2, file2)
                                # For the global registry, extract all types.
                                types_in_file = extract_types_from_file(file_path, type_registry=None, filter_requests=False)
                                for t in types_in_file:
                                    key = t["name"]
                                    # For message types, store the parameters schema.
                                    if t["type"] == "function":
                                        registry[key] = t.get("parameters")
                                    else:
                                        registry[key] = t
    return registry

# ---------------------------
# Main: Combine both functionalities
# ---------------------------
def process_all_packages(base_directory):
    # Build the global type registry first.
    type_registry = build_type_registry(base_directory)
    # Process each package, using the type registry to enhance method parameter details.
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == "gapic_metadata.json":
                metadata_path = os.path.join(root, file)
                package_results = process_package(metadata_path, type_registry=type_registry)
                if package_results:
                    working_dir = r"\Users\AMD\vidhra\internal\ast"
                    output_dir = os.path.join(working_dir, "extracted_methods")
                    # Use the package folder name (assumed to be the parent folder of gapic_metadata.json)
                    tools_dir = os.path.join(output_dir, metadata_path.split("\\")[-2])
                    os.makedirs(tools_dir, exist_ok=True)
                    output_file = os.path.join(tools_dir, "tools.json")
                    with open(output_file, "w", encoding="utf-8") as f:
                        json.dump(package_results, f, indent=2)
                    print(f"Extracted async method information saved to {output_file}")

def main():
    base_directory = r"\Users\AMD\vidhra\internal\ast\google-cloud-python\packages"
    process_all_packages(base_directory)

if __name__ == "__main__":
    main()
