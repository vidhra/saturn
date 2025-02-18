import os
import json
import ast

def load_gapic_metadata(metadata_file):
    """Load the GAPIC metadata JSON file."""
    with open(metadata_file, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_methods_from_file(file_path, class_name, target_methods):
    """
    Parse the given file and extract methods from the specified class.
    Only methods whose names are in target_methods are extracted.
    
    Returns a list of dictionaries with keys: name, description, parameters.
    The parameters are formatted as a JSON schema.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        source = f.read()
    
    tree = ast.parse(source, file_path)
    extracted_methods = []

    # Find the target class by name.
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            for item in node.body:
                # Process both synchronous and asynchronous methods.
                if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    method_name = item.name
                    if method_name in target_methods:
                        # Build parameter schema: default each parameter to type string.
                        properties = {}
                        required = []
                        
                        # Process regular arguments.
                        for arg in item.args.args:
                            if arg.arg in ("self", "cls"):
                                continue
                            properties[arg.arg] = {"type": "string", "description": ""}
                            required.append(arg.arg)
                        
                        # Process keyword-only arguments.
                        for arg in item.args.kwonlyargs:
                            properties[arg.arg] = {"type": "string", "description": ""}
                            required.append(arg.arg)
                        
                        # Get the method docstring (if available).
                        docstring = ast.get_docstring(item) or ""
                        
                        method_info = {
                            "type": "function",
                            "function": {
                            "name": method_name,
                            "description": docstring.strip()[:1024],
                            "parameters": {
                                "type": "object",
                                "properties": properties,
                                "required": required
                                }
                            }
                            }
                        extracted_methods.append(method_info)
            break  # Found the class; no need to search further.
    return extracted_methods

def main():
    # Set the paths to the metadata JSON and the async client file.
    metadata_path = r"C:\Users\AMD\vidhra\internal\ast\google-cloud-python\packages\google-cloud-billing\google\cloud\billing_v1\gapic_metadata.json"
    client_file = r"C:\Users\AMD\vidhra\internal\ast\google-cloud-python\packages\google-cloud-billing\google\cloud\billing_v1\services\cloud_billing\async_client.py"
    
    # Load the GAPIC metadata.
    metadata = load_gapic_metadata(metadata_path)
    
    # For the async client, use the "grpc-async" metadata.
    grpc_async_metadata = metadata["services"]["CloudBilling"]["clients"]["grpc-async"]
    rpcs = grpc_async_metadata["rpcs"]
    
    # Collect all method names specified in the metadata.
    target_methods = set()
    for rpc_name, details in rpcs.items():
        for method in details.get("methods", []):
            target_methods.add(method)
    
    # Specify the class name as defined in the file.
    class_name = "CloudBillingAsyncClient"
    
    # Extract method information.
    methods_info = extract_methods_from_file(client_file, class_name, target_methods)
    
    # Write the output in the desired JSON format (an array of method objects).
    output_file = "extracted_async_methods.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(methods_info, f, indent=2)
    
    print(f"Extracted method information saved to {output_file}")

if __name__ == "__main__":
    main()
