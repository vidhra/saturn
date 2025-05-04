# Contains logic refactored from call.py for loading/managing API definitions
import json
import os
import glob
from typing import List, Dict, Any, Optional

# May need embedding model for filtering later
# from sentence_transformers import SentenceTransformer
# import numpy as np

class KnowledgeBase:
    def __init__(self, api_defs_dir: str):
        """Initializes the Knowledge Base by loading API definitions."""
        self.api_defs_dir = api_defs_dir
        self.tools_data: Dict[str, Any] = {}
        self.types_data: Dict[str, Any] = {}
        self.raw_tools: List[Dict[str, Any]] = [] # Store initially parsed tools
        # self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2') # Load if filtering needed
        self._load_definitions()
        self._build_raw_tools()

    def _load_definitions(self):
        """Loads tools.json and types.json from subdirectories."""
        print(f"Loading API definitions from: {self.api_defs_dir}")
        tool_pattern = os.path.join(self.api_defs_dir, "*", "tools.json")
        type_pattern = os.path.join(self.api_defs_dir, "*", "types.json")

        for tool_file in glob.glob(tool_pattern):
            service_dir = os.path.dirname(tool_file)
            service_name = os.path.basename(service_dir) # e.g., vpcaccess_v1
            try:
                with open(tool_file, "r", encoding="utf-8") as f:
                    self.tools_data[service_name] = json.load(f)
                print(f"  Loaded tools for: {service_name}")
            except Exception as e:
                print(f"  Error loading tools from {tool_file}: {e}")

        for type_file in glob.glob(type_pattern):
            service_dir = os.path.dirname(type_file)
            service_name = os.path.basename(service_dir)
            try:
                with open(type_file, "r", encoding="utf-8") as f:
                    self.types_data[service_name] = json.load(f)
                print(f"  Loaded types for: {service_name}")
            except Exception as e:
                print(f"  Error loading types from {type_file}: {e}")
        
        if not self.tools_data:
             print(f"Warning: No tool definitions found in {self.api_defs_dir}")
        if not self.types_data:
             print(f"Warning: No type definitions found in {self.api_defs_dir}")


    def _transform_fields(self, schema_fragment: Any) -> Any:
        """
        Recursively walks the schema, converts enums, and resolves references if needed.
        (Simplified version from call.py - may need enhancement for $ref later)
        """
        if not isinstance(schema_fragment, dict):
            return schema_fragment

        # Convert enumerations (similar to call.py)
        if schema_fragment.get("type") == "enum" and "values" in schema_fragment:
            enum_vals = list(schema_fragment.pop("values").keys())
            schema_fragment["type"] = "string"
            schema_fragment["enum"] = enum_vals
            # OpenAI often expects a description for enums
            if "description" not in schema_fragment:
                 schema_fragment["description"] = f"Must be one of: {', '.join(enum_vals)}"
            else:
                 schema_fragment["description"] += f" Must be one of: {', '.join(enum_vals)}"


        # Recurse into properties, items, etc.
        if "properties" in schema_fragment and isinstance(schema_fragment["properties"], dict):
            schema_fragment["properties"] = {
                k: self._transform_fields(v) for k, v in schema_fragment["properties"].items()
            }
        if "items" in schema_fragment:
             schema_fragment["items"] = self._transform_fields(schema_fragment["items"])
        if "additionalProperties" in schema_fragment:
             schema_fragment["additionalProperties"] = self._transform_fields(schema_fragment["additionalProperties"])
        # Add recursion for other potential nested schema locations if needed (e.g., allOf, anyOf)

        return schema_fragment

    def _build_raw_tools(self):
        """
        Builds the initial list of OpenAI tool definitions from loaded data.
        Refactored and generalized from build_openai_tools in call.py.
        """
        print("Building initial tool definitions...")
        all_tools = []
        request_types_map = {}

        # First pass: build the request types map from all loaded types.json
        for service_name, service_types in self.types_data.items():
            if isinstance(service_types, dict):
                # Original structure was { file: [types] }, handle potential variations
                # Assuming the list of types is the primary value if dict
                 type_list = next(iter(service_types.values()), []) 
            elif isinstance(service_types, list):
                 type_list = service_types
            else:
                 type_list = []
                 print(f"Warning: Unexpected format for types_data[{service_name}]")

            for type_info in type_list:
                if type_info.get("type") == "message": # Assuming type:message maps to request objects
                    type_name = type_info.get("name")
                    if type_name:
                         # Store with service prefix to avoid name collisions
                        request_types_map[f"{service_name}.{type_name}"] = type_info

        # Second pass: iterate through tools.json and build tool definitions
        for service_name, service_tools in self.tools_data.items():
            for method in service_tools.get("methods", []):
                func_def = method.get("function", {})
                method_name = func_def.get("name")
                request_types = func_def.get("request_types", [])
                
                if not method_name or not request_types:
                    continue
                
                # Assume the first request type is the primary one
                # Add service prefix to look up in our combined map
                request_type_key = f"{service_name}.{request_types[0]}"
                
                if request_type_key not in request_types_map:
                    print(f"  Warning: Request type '{request_type_key}' not found for method '{method_name}'")
                    continue

                import copy
                type_info = request_types_map[request_type_key]
                # Deep copy parameters before transforming
                parameters_copy = copy.deepcopy(type_info.get("parameters", {}))

                # Transform enums, etc.
                parameters_transformed = self._transform_fields(parameters_copy)

                # Construct the tool name with service prefix
                tool_name = f"{service_name}.{method_name}"
                
                # Build the final tool definition for OpenAI
                openai_tool = {
                    "type": "function",
                    "function": {
                        "name": tool_name,
                        "description": type_info.get("description", f"Calls the {tool_name} method."),
                        "parameters": parameters_transformed,
                    }
                }
                all_tools.append(openai_tool)
                print(f"  Built tool: {tool_name}")

        self.raw_tools = all_tools
        print(f"Finished building {len(self.raw_tools)} raw tools.")

        # Build a quick lookup map for type schemas by full name (service.TypeName)
        self._type_schema_map = {}
        for service_name, service_types_file_content in self.types_data.items():
             # Assuming structure { "/path/to/file.py": [ {type_info}, ... ] }
             if isinstance(service_types_file_content, dict):
                 for file_path, type_list in service_types_file_content.items():
                     if isinstance(type_list, list):
                         for type_info in type_list:
                             type_name = type_info.get("name")
                             if type_name:
                                 # Use service_name as part of the key for uniqueness
                                 full_type_name = f"{service_name}.{type_name}"
                                 self._type_schema_map[full_type_name] = type_info
                                 # Also store potential references like google.cloud... if available
                                 reference = type_info.get("reference") # Check if types.json includes this
                                 if reference:
                                      self._type_schema_map[reference] = type_info
             else:
                 print(f"Warning: Unexpected format for types_data[{service_name}]")


    def get_formatted_tools(self, query: Optional[str] = None, similarity_threshold: float = 0.6) -> List[Dict[str, Any]]:
        """
        Returns the list of tools formatted for OpenAI.
        Optionally filters tools/parameters based on query similarity (feature from call.py).
        """
        # TODO: Implement optional filtering based on query similarity if needed.
        # This involves embedding the query and parameter descriptions.
        # For now, just return all built tools.
        if query:
            print(f"Query-based filtering not yet implemented. Returning all {len(self.raw_tools)} tools.")
            # Add filtering logic here using self.embedding_model if required in future

        return self.raw_tools

    def get_request_types_for_method(self, service_method_name: str) -> List[str]:
        """
        Finds the original request type names associated with a combined service.method name.
        Example: input 'vpcaccess_v1.create_connector', find associated request types in tools.json.
        Returns the *original* type names (without service prefix).
        """
        service_name, method_name = service_method_name.split('.', 1)
        if service_name not in self.tools_data:
            return []

        # Iterate through the top-level keys (service class names) in the loaded JSON
        service_class_definitions = self.tools_data[service_name]
        if not isinstance(service_class_definitions, dict):
             print(f"Warning: Expected dict for tools_data[{service_name}], got {type(service_class_definitions)}. Cannot find methods.")
             return []
        
        for service_class_name, service_class_def in service_class_definitions.items():
            # Now access the 'methods' list within the service class definition
            methods_list = service_class_def.get("methods", [])
            if not isinstance(methods_list, list):
                print(f"Warning: Expected list for methods in {service_class_name}, got {type(methods_list)}.")
                continue # Skip if structure is unexpected

            for method_def in methods_list:
                fn_info = method_def.get("function", {})
                if fn_info.get("name") == method_name:
                    request_types = fn_info.get("request_types", [])
                    if request_types:
                        print(f"Found request types {request_types} for {service_method_name}")
                        return request_types # Return the list found
                    else:
                        print(f"Warning: Method {service_method_name} found but has no request_types defined.")
                        return [] # Found method but no types defined

        # Method not found in any service class within the file
        print(f"Method '{method_name}' not found under any service class in {service_name}/tools.json")
        return []

    def get_type_schema(self, full_type_name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the JSON schema definition for a given type name.
        The type name should ideally be prefixed with the service name
        (e.g., 'vpcaccess_v1.CreateConnectorRequest') or be a full reference.
        """
        schema = self._type_schema_map.get(full_type_name)
        if schema:
            print(f"Found schema for type: {full_type_name}")
            return schema
        else:
            # Attempt fallback/variations if needed? (e.g., search without service prefix)
            print(f"Warning: Schema not found for type: {full_type_name}")
            return None

# Example Usage removed to prevent linting issues. 