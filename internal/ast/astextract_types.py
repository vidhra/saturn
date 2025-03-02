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

    # Regex to identify attribute lines of the form:
    #   name (str):
    #       Some description...
    attr_pattern = re.compile(r"^\s*(\w+)\s*\(\s*([\w\[\], \.]+)\)\:\s*(.*)$")

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            # Check if this class inherits from proto.Message
            base_names = [base.id for base in node.bases if isinstance(base, ast.Name)]
            # Or, if there's a more complex base like proto.Message in a dotted import:
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
                
                # We'll do a docstring-based approach to parse any "Attributes:" section
                doc_lines = docstring.splitlines()
                in_attributes_section = False
                attr_name_in_progress = None
                attr_desc_in_progress = []

                for line in doc_lines:
                    # Detect if we are in the "Attributes:" section
                    if "Attributes:" in line:
                        in_attributes_section = True
                        continue

                    # If we are in the attributes section, look for attribute lines
                    if in_attributes_section:
                        match = attr_pattern.match(line)
                        if match:
                            # Finalize any previous attribute
                            if attr_name_in_progress:
                                existing = attributes.get(attr_name_in_progress, {})
                                existing["description"] = (
                                    existing.get("description", "")
                                    + " "
                                    + " ".join(attr_desc_in_progress)
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
                            # If we already matched an attribute, keep reading lines
                            if attr_name_in_progress:
                                attr_desc_in_progress.append(line.strip())

                # Finalize any leftover attribute
                if attr_name_in_progress:
                    existing = attributes.get(attr_name_in_progress, {})
                    existing["description"] = (
                        existing.get("description", "")
                        + " "
                        + " ".join(attr_desc_in_progress)
                    ).strip()
                    attributes[attr_name_in_progress] = existing

                # Build final output for this request class
                extracted_classes.append({
                    "type": "request_class",
                    "name": class_name,
                    "docstring": docstring_truncated,
                    "attributes": attributes
                })

    return extracted_classes

def main():
    # Example usage: parse the "cloud_billing.py" file that includes request classes
    # Adjust the path below as appropriate for your environment
    metadata_path = r"C:\Users\AMD\vidhra\internal\ast\google-cloud-python\packages\google-cloud-billing\google\cloud\billing_v1\gapic_metadata.json"
    client_file = r"C:\Users\AMD\vidhra\internal\ast\google-cloud-python\packages\google-cloud-billing\google\cloud\billing_v1\types\cloud_billing.py"

    # (Optional) load metadata for other tasks
    metadata = load_gapic_metadata(metadata_path)

    request_classes_info = extract_request_classes_from_file(client_file)
    
    # Write out the extracted data
    output_file = "extracted_request_classes.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(request_classes_info, f, indent=2)

    print(f"Extracted {len(request_classes_info)} request classes from {client_file}")
    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()