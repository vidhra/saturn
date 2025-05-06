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
        # --- Debug --- 
        print(f"[KB Debug] KnowledgeBase initialized. {len(self.raw_tools)} raw tools built.")
        if not self.raw_tools:
            print("[KB Debug] WARNING: raw_tools list is empty after initialization.")
        # --- End Debug ---

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
        print("[KB Debug] --- Pass 1: Building request_types_map ---")
        for service_name, service_types_content in self.types_data.items(): # Renamed for clarity
            print(f"[KB Debug] Processing types for service: {service_name}")
            
            all_type_definitions_for_service = []
            if isinstance(service_types_content, dict):
                # This is the case for run_v2: {filepath: [type_defs], filepath2: [type_defs]}
                print(f"[KB Debug]   Service types content is dict. Iterating through its values (lists of types).")
                for file_path_key in service_types_content: # Iterate through file paths
                    file_type_list = service_types_content[file_path_key]
                    if isinstance(file_type_list, list):
                        all_type_definitions_for_service.extend(file_type_list)
                    else:
                        print(f"[KB Debug]     Warning: Expected a list of types for file '{file_path_key}' in '{service_name}', got {type(file_type_list)}")
            elif isinstance(service_types_content, list):
                # This might be the case for simpler services where types.json is just a list
                print(f"[KB Debug]   Service types content is list.")
                all_type_definitions_for_service = service_types_content
            else:
                print(f"Warning: Unexpected format for types_data[{service_name}], type is {type(service_types_content)}. Skipping.")
                continue # Skip this service if format is unknown

            print(f"[KB Debug]   Total type definitions found for {service_name}: {len(all_type_definitions_for_service)}")
            for type_info in all_type_definitions_for_service:
                # print(f"[KB Debug]     Checking type_info: {type_info.get('name')}, type: {type_info.get('type')}") # DEBUG (Verbose)
                if type_info.get("type") == "function": # Assuming "function" is the indicator for request type schemas
                    type_name = type_info.get("name")
                    if type_name:
                         # Store with service prefix to avoid name collisions
                        map_key = f"{service_name}.{type_name}" # e.g., run_v2.GetExecutionRequest
                        request_types_map[map_key] = type_info
                        print(f"[KB Debug]     Added to request_types_map: Key='{map_key}'")

        print(f"[KB Debug] --- Pass 1 Complete: request_types_map has {len(request_types_map)} entries ---")

        # Second pass: iterate through tools.json and build tool definitions
        print("[KB Debug] --- Pass 2: Building tools from tools_data ---")
        for service_name, service_tools in self.tools_data.items():
            print(f"[KB Debug] Processing tools for service: {service_name}")
            if not isinstance(service_tools, dict):
                 print(f"[KB Debug]   WARNING: Expected service_tools for '{service_name}' to be a dict, got {type(service_tools)}. Skipping.")
                 continue
            
            for service_class_name, service_class_def in service_tools.items():
                 print(f"[KB Debug]   Processing service class/key: {service_class_name}")
                 if not isinstance(service_class_def, dict) or "methods" not in service_class_def:
                      print(f"[KB Debug]     Skipping '{service_class_name}', not a dict or no 'methods' key.")
                      continue

                 for method in service_class_def.get("methods", []):
                    func_def = method.get("function", {})
                    method_name = func_def.get("name")
                    request_types = func_def.get("request_types", [])

                    if not method_name:
                         print("[KB Debug]         Skipping method: No method name found.")
                         continue
                    if not request_types:
                         print(f"[KB Debug]         Skipping method '{method_name}': No request_types defined.")
                         continue

                    raw_request_type_name_from_tools = request_types[0]
                    base_request_type_name = raw_request_type_name_from_tools.split('.')[-1]
                    request_type_key = f"{service_name}.{base_request_type_name}"
                    
                    print(f"[KB Debug]       Method '{method_name}', Raw Request Type from tools.json: '{raw_request_type_name_from_tools}', Base Name: '{base_request_type_name}', Generated Lookup Key: '{request_type_key}'")

                    if request_type_key not in request_types_map:
                        print(f"[KB Debug]         WARNING: Key '{request_type_key}' not found in request_types_map. Cannot build tool '{service_name}_{method_name}'.")
                        similar_keys = [k for k in request_types_map if base_request_type_name in k and service_name in k]
                        if similar_keys:
                             print(f"[KB Debug]           Possible related keys found in map for {service_name}.{base_request_type_name}: {similar_keys}")
                        else:
                             print(f"[KB Debug]           No similar keys found in map for {service_name}.{base_request_type_name}.")
                        # Check if map contains *any* keys for the service for broader debugging
                        service_specific_keys_in_map = [k for k in request_types_map if k.startswith(f"{service_name}.")]
                        if not service_specific_keys_in_map:
                            print(f"[KB Debug]           No keys found for service '{service_name}' in request_types_map at all.")
                        elif len(service_specific_keys_in_map) < 10: # Print a few if the list is small
                            print(f"[KB Debug]           Some keys for service '{service_name}' in map: {service_specific_keys_in_map[:5]}")


                        continue
                    else:
                        print(f"[KB Debug]         Key '{request_type_key}' FOUND in request_types_map.")

                    import copy
                    type_info = request_types_map[request_type_key]
                    parameters_copy = copy.deepcopy(type_info.get("parameters", {}))
                    parameters_transformed = self._transform_fields(parameters_copy)
                    tool_name_for_openai = f"{service_name}_{method_name}"

                    openai_tool = {
                        "type": "function",
                        "function": {
                            "name": tool_name_for_openai,
                            "description": func_def.get("description", type_info.get("description", f"Calls the {tool_name_for_openai} method.")), # Prefer description from tools.json func_def
                            "parameters": parameters_transformed,
                        }
                    }
                    all_tools.append(openai_tool)
                    print(f"[KB Debug]       Successfully built tool: {tool_name_for_openai}")


        self.raw_tools = all_tools
        print(f"[KB Debug] --- Pass 2 Complete ---") # DEBUG
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
        # --- Debug --- 
        print(f"[KB Debug] get_formatted_tools called. Current raw_tools count: {len(self.raw_tools)}")
        # --- End Debug ---
        
        # TODO: Implement optional filtering based on query similarity if needed.
        if query:
            print(f"[KB Debug] Query-based filtering not yet implemented. Returning all raw tools.")
            # Add filtering logic here using self.embedding_model if required in future

        return self.raw_tools # Return the built list

    def get_request_types_for_method(self, service_method_name: str) -> List[str]:
        """
        Finds the original request type names associated with a combined service.method name.
        Example: input 'vpcaccess_v1_create_connector', find associated request types in tools.json.
        Returns the *original* type names (without service prefix).
        """
        # --- Updated logic to handle underscores in service names --- 
        found_service_key = None
        method_name = None
        for key in self.tools_data.keys():
             # Check if the tool name starts with the key followed by an underscore
            if service_method_name.startswith(f"{key}_"):
                # Choose the longest matching key (e.g., prefer 'vpcaccess_v1' over 'vpcaccess')
                if found_service_key is None or len(key) > len(found_service_key):
                     found_service_key = key
                     # Extract method name after the prefix and underscore
                     method_name = service_method_name[len(key) + 1:] 

        if not found_service_key or not method_name:
            print(f"Error: Could not reliably split tool name '{service_method_name}' into a known service key and method name.")
            print(f"  Known service keys: {list(self.tools_data.keys())}")
            return []
        
        service_name = found_service_key # Use the actual key found
        # --- End updated logic ---

        # if service_name not in self.tools_data: # Check is implicitly done above
        #     print(f"Warning: Service '{service_name}' not found in loaded tools data.") # Updated warning
        #     return []

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
        print(f"Method '{method_name}' not found under any service class in {service_name}/tools.json (derived from tool name '{service_method_name}')") # Updated warning
        return []

    def get_type_schema(self, full_type_name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the full schema for a given type name (e.g., service.TypeName or google.cloud... reference).
        """
        return self._type_schema_map.get(full_type_name)

    def get_tool_parameter_json_schema(self, tool_name: str) -> Optional[Dict[str, Any]]:
        """
        Retrieves the JSON schema for the parameters of a given tool name.
        The tool_name is expected to be in the format 'service_method' (e.g., vpcaccess_v1_create_connector).
        """
        # self.raw_tools is a list of dicts, each like:
        # {
        #   "type": "function",
        #   "function": {
        #     "name": "service_method_name",
        #     "description": "...",
        #     "parameters": { /* JSON Schema for parameters */ }
        #   }
        # }
        for tool_def in self.raw_tools:
            if tool_def.get("function", {}).get("name") == tool_name:
                return tool_def["function"].get("parameters")
        print(f"[KB Debug] Tool name '{tool_name}' not found in raw_tools for schema retrieval.")
        return None

# Example Usage removed to prevent linting issues. 