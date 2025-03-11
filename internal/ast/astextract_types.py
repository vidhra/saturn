import ast
import json
import re
import os

def load_gapic_metadata(metadata_file: str):
    """Load the GAPIC metadata JSON file."""
    with open(metadata_file, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_request_classes_from_file(file_path: str):
    """
    Scan the specified file for classes inheriting from proto.Message
    (e.g. 'class GetBillingAccountRequest(proto.Message): ...')
    and extract a list of request classes. For each class:
      - Capture the class name.
      - Capture & truncate the docstring (to 1024 chars).
      - Extract attributes from any 'Attributes:' block in the docstring
        of the form:
            attribute_name (str):
                Some multiline description
    Returns a list of dictionaries with keys:
      - 'type': Always 'request_class'
      - 'name': The class name
      - 'docstring': The truncated docstring
      - 'attributes': A dict of {attribute_name: {"type": "...", "description": "..."}}
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()

    tree = ast.parse(source, file_path)
    extracted_classes = []

    # Regex to identify attribute lines, e.g. "attribute_name (str): Some description..."
    attr_pattern = re.compile(r"^\s*(\w+)\s*\(\s*([\w\[\], \.]+)\)\:\s*(.*)$")

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Determine if this class inherits from proto.Message.
            base_names = [base.id for base in node.bases if isinstance(base, ast.Name)]
            base_attrs = [
                f"{base.value.id}.{base.attr}" 
                for base in node.bases 
                if isinstance(base, ast.Attribute) and hasattr(base.value, "id")
            ]
            all_bases = base_names + base_attrs

            if any("proto.Message" in b for b in all_bases):
                class_name = node.name
                docstring = ast.get_docstring(node) or ""
                docstring_truncated = docstring.strip()[:1024]

                attributes = {}
                # Look for an "Attributes:" section in the docstring.
                doc_lines = docstring.splitlines()
                in_attributes_section = False
                attr_name_in_progress = None
                attr_desc_in_progress = []

                for line in doc_lines:
                    # Enter the attributes section when the marker is encountered.
                    if "Attributes:" in line:
                        in_attributes_section = True
                        continue

                    if in_attributes_section:
                        match = attr_pattern.match(line)
                        if match:
                            # Finalize any previous attribute being processed.
                            if attr_name_in_progress:
                                existing = attributes.get(attr_name_in_progress, {})
                                existing["description"] = (
                                    existing.get("description", "") + " " +
                                    " ".join(attr_desc_in_progress)
                                ).strip()
                                attributes[attr_name_in_progress] = existing
                                attr_name_in_progress = None
                                attr_desc_in_progress = []

                            attr_name, attr_type, attr_desc = match.groups()
                            attr_name = attr_name.strip()
                            attr_type = attr_type.strip()
                            attributes[attr_name] = {
                                "type": attr_type or "string",
                                "description": attr_desc.strip()
                            }
                            attr_name_in_progress = attr_name
                            attr_desc_in_progress = []
                        else:
                            if attr_name_in_progress:
                                attr_desc_in_progress.append(line.strip())

                # Finalize the last attribute if still in progress.
                if attr_name_in_progress:
                    existing = attributes.get(attr_name_in_progress, {})
                    existing["description"] = (
                        existing.get("description", "") + " " +
                        " ".join(attr_desc_in_progress)
                    ).strip()
                    attributes[attr_name_in_progress] = existing

                extracted_classes.append({
                    "type": "request_class",
                    "name": class_name,
                    "docstring": docstring_truncated,
                    "attributes": attributes
                })

    return extracted_classes

def process_package_types(metadata_path: str):
    """
    For a given gapic_metadata.json file, locate the 'types' directory within the package,
    and extract all request classes from every Python file in that directory.
    Returns a dictionary mapping file paths to lists of extracted request classes.
    """
    package_dir = os.path.dirname(metadata_path)
    types_dir = os.path.join(package_dir, "types")
    extracted_types = {}

    if os.path.isdir(types_dir):
        for root, _, files in os.walk(types_dir):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    classes = extract_request_classes_from_file(file_path)
                    if classes:
                        extracted_types[file_path] = classes
    return extracted_types

def process_all_packages_types(base_directory: str):
    """
    Recursively search for gapic_metadata.json files under the base directory,
    process each package to extract request classes from its 'types' directory,
    and save each package's results in its own output folder.
    """
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == "gapic_metadata.json":
                metadata_path = os.path.join(root, file)
                types_data = process_package_types(metadata_path)
                if types_data:
                    working_dir = r"\Users\AMD\vidhra\internal\ast"
                    output_dir = os.path.join(working_dir, "extracted_methods")
                    tools_dir = os.path.join(output_dir, metadata_path.split("\\")[-2])
                    os.makedirs(tools_dir, exist_ok=True)
                    output_file = os.path.join(tools_dir, "types.json")
                    with open(output_file, "w", encoding="utf-8") as f:
                        json.dump(types_data, f, indent=2)
                    print(f"Extracted request classes saved to {output_file}")

def main():
    # Set the base directory for the packages.
    base_directory = r"\Users\AMD\vidhra\internal\ast\google-cloud-python\packages"
    process_all_packages_types(base_directory)

if __name__ == "__main__":
    main()
