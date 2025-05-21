import ast
import json
import re
import os

def load_gapic_metadata(metadata_file: str):
    """Load the GAPIC metadata JSON file."""
    with open(metadata_file, "r", encoding="utf-8") as f:
        return json.load(f)

def convert_type(type_str: str, type_registry=None) -> dict:
    """
    Convert a raw type string into a nested JSON schema–like definition.
    Recognizes array types (MutableSequence/List), mapping types (MutableMapping/Dict),
    built-in types, and for custom types looks up the global registry.
    """
    type_str = type_str.strip()
    
    # Handle array types: e.g. MutableSequence[...] or List[...]
    if type_str.startswith("MutableSequence[") or type_str.startswith("List["):
        inner = type_str[type_str.find("[") + 1 : -1]
        inner_schema = convert_type(inner, type_registry)
        return {"type": "array", "items": inner_schema}
    
    # Handle mapping types: e.g. MutableMapping[str, str] or Dict[str, int]
    if type_str.startswith("MutableMapping[") or type_str.startswith("Dict["):
        inner = type_str[type_str.find("[") + 1 : -1]
        parts = [p.strip() for p in inner.split(",")]
        if len(parts) == 2:
            value_schema = convert_type(parts[1], type_registry)
            return {"type": "object", "additionalProperties": value_schema}
        else:
            return {"type": "object"}
    
    # Map common built-in types.
    simple_mappings = {
        "str": "string",
        "int": "integer",
        "float": "number",
        "bool": "boolean"
    }
    if type_str in simple_mappings:
        return {"type": simple_mappings[type_str]}
    
    # Otherwise, assume a custom type.
    # Use the simple type name (e.g. Instance from google.cloud.filestore_v1.types.Instance)
    simple_name = type_str.split('.')[-1]
    if type_registry and simple_name in type_registry:
        # Initially return a reference; it will be inlined later.
        return {"reference": type_str}
    
    # Fallback if type not found in registry.
    return {"type": "object", "reference": type_str}

def resolve_nested_references(schema: dict, type_registry: dict, path=None) -> dict:
    """
    Recursively replace custom type references (schemas with a "reference" key)
    with the corresponding schema from the global type registry.
    Uses a 'path' list to track the resolution chain to avoid infinite recursion.
    The original "reference" is preserved, while the resolved schema is stored under "resolved_schema".
    """
    if path is None:
        path = []
    
    if "reference" in schema:
        ref = schema["reference"]
        simple_name = ref.split('.')[-1]
        if simple_name in path:
            # Circular reference detected; return as-is.
            return schema
        new_path = path + [simple_name]
        if simple_name in type_registry:
            # Resolve nested type and store it under "resolved_schema" without removing the original "reference".
            resolved = resolve_nested_references(type_registry[simple_name], type_registry, new_path)
            schema["resolved_schema"] = resolved
            return schema
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

def extract_request_classes_from_file(file_path: str, type_registry=None, filter_requests: bool = False):
    """
    Scan the specified file for classes inheriting from proto.Message and extract classes.
    
    If filter_requests is True, only classes whose names end with "Request" are processed.
    
    For each class:
      - Capture the class name.
      - Capture & truncate the docstring (to 1024 chars).
      - Extract attributes from any 'Attributes:' block in the docstring.
      - Mark fields as output_only if their description indicates they're output-only.
    
    Returns a list of dictionaries formatted for LLM function calling,
    with nested types resolved using the provided type_registry.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source, file_path)
    extracted_classes = []
    
    # Regex to identify attribute lines.
    attr_pattern = re.compile(r"^\s*(\w+)\s*\(\s*([\w\[\], \.]+)\)\:\s*(.*)$")
    
    # Output-only indicators in field descriptions
    output_only_patterns = [
        r'output[ \-_]*only',
        r'server[ \-_]*generated',
        r'read[ \-_]*only',
        r'returned by the server',
        r'populated by the server',
        r'output parameter',
        r'response only',
        r'returned but not accepted'
    ]
    output_only_regex = re.compile('|'.join(output_only_patterns), re.IGNORECASE)

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Check if class inherits from proto.Message.
            base_names = [base.id for base in node.bases if isinstance(base, ast.Name)]
            base_attrs = [
                f"{base.value.id}.{base.attr}"
                for base in node.bases 
                if isinstance(base, ast.Attribute) and hasattr(base.value, "id")
            ]
            all_bases = base_names + base_attrs
            if not any("proto.Message" in b for b in all_bases):
                continue

            class_name = node.name
            # If filtering for requests, skip if the class name does not end with "Request".
            if filter_requests and not class_name.endswith("Request"):
                continue

            docstring = ast.get_docstring(node) or ""
            docstring_truncated = docstring.strip()[:1024]

            # Extract raw attributes from the "Attributes:" section.
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
                                                       " " +
                                                       " ".join(current_desc_lines)).strip()
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
                    else:
                        if current_attr:
                            current_desc_lines.append(line.strip())
            if current_attr:
                existing = raw_attributes.get(current_attr, {})
                existing["description"] = (existing.get("description", "") +
                                           " " +
                                           " ".join(current_desc_lines)).strip()
                raw_attributes[current_attr] = existing

            # Build the JSON schema for parameters.
            schema_properties = {}
            required_fields = []
            for attr_name, details in raw_attributes.items():
                converted_type = (convert_type(details["raw_type"], type_registry)
                                  if details.get("raw_type") else {"type": "string"})
                if type_registry is not None:
                    resolved_type = resolve_nested_references(converted_type, type_registry)
                else:
                    resolved_type = converted_type
                
                # Check if the field description indicates it's output-only
                is_output_only = output_only_regex.search(details["description"]) is not None
                
                if details["description"].lstrip().startswith("Required"):
                    required_fields.append(attr_name)
                
                schema_properties[attr_name] = {
                    "description": details["description"],
                    **resolved_type
                }
                
                # Add output_only property if the field is determined to be output-only
                if is_output_only:
                    schema_properties[attr_name]["output_only"] = True

            parameters_schema = {
                "type": "object",
                "properties": schema_properties
            }
            if required_fields:
                parameters_schema["required"] = required_fields

            extracted_classes.append({
                "type": "function",
                "name": class_name,
                "description": docstring_truncated,
                "parameters": parameters_schema
            })

    return extracted_classes

def process_package_types(metadata_path: str, type_registry: dict) -> dict:
    """
    For a given gapic_metadata.json file, locate the 'types' directory within the package,
    and extract all proto.Message classes (only those ending with "Request") from every Python file,
    using the provided type_registry for nested type resolution.
    Returns a dictionary mapping file paths to lists of extracted classes.
    """
    package_dir = os.path.dirname(metadata_path)
    types_dir = os.path.join(package_dir, "types")
    extracted_types = {}

    if os.path.isdir(types_dir):
        for root, _, files in os.walk(types_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    # When processing package types, filter for request classes only.
                    classes = extract_request_classes_from_file(file_path, type_registry, filter_requests=True)
                    if classes:
                        extracted_types[file_path] = classes
    return extracted_types

def build_type_registry(base_directory: str) -> dict:
    """
    Recursively search for gapic_metadata.json files under the base directory,
    process each package's 'types' directory, and build a global registry mapping
    custom type names (simple name only) to their extracted JSON schema (parameters).
    
    In the global registry, all types (both request and non-request) are included.
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
                                # For the registry, extract all types (do not filter by request).
                                classes = extract_request_classes_from_file(file_path, type_registry=None, filter_requests=False)
                                for cls in classes:
                                    # Use the class name as key.
                                    registry[cls["name"]] = cls["parameters"]
    return registry

def process_all_packages_types(base_directory: str):
    """
    Build a global type registry from all packages, then recursively search for gapic_metadata.json
    files under the base directory, process each package to extract proto.Message classes (only request types)
    from its 'types' directory (using the global registry to inline nested types), and save each package's
    results in its own output folder. The global type registry is also saved.
    """
    # Build the global registry (includes all types).
    type_registry = build_type_registry(base_directory)
    
    # Save the global type registry to a file.
    working_dir = r"/Users/prashanthvarma/Saturn/internal/ast"
    output_dir = os.path.join(working_dir, "extracted_methods")
    os.makedirs(output_dir, exist_ok=True)
    registry_file = os.path.join(output_dir, "global_type_registry.json")
    with open(registry_file, "w", encoding="utf-8") as f:
        json.dump(type_registry, f, indent=2)
    print(f"Global type registry saved to {registry_file}")

    # Process each package and store only request types.
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == "gapic_metadata.json":
                metadata_path = os.path.join(root, file)
                types_data = process_package_types(metadata_path, type_registry)
                if types_data:
                    tools_dir = os.path.join(output_dir, metadata_path.split("/")[-2])
                    os.makedirs(tools_dir, exist_ok=True)
                    output_file = os.path.join(tools_dir, "types.json")
                    with open(output_file, "w", encoding="utf-8") as f:
                        json.dump(types_data, f, indent=2)
                    print(f"Extracted request classes saved to {output_file}")

def main():
    base_directory = r"/Users/prashanthvarma/Saturn/internal/ast/google-cloud-python/packages"
    process_all_packages_types(base_directory)

if __name__ == "__main__":
    main()
