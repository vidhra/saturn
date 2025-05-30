# Contains logic refactored from call.py for loading/managing API definitions
import json
import os
import glob
import copy
from typing import List, Dict, Any, Optional
from saturn.file_build_tools import FileBuildToolCaller


class KnowledgeBase:
    def __init__(self, api_defs_dir: str, external_tools: Optional[List[Dict[str, Any]]] = None, working_directory: str = "."):
        """Initializes the Knowledge Base by loading API definitions and merging external tools if provided."""
        self.api_defs_dir = api_defs_dir
        self.working_directory = working_directory
        self.tools_data: Dict[str, Any] = {}
        self.types_data: Dict[str, Any] = {}
        self.raw_tools: List[Dict[str, Any]] = []
        self.file_build_tools: List[Dict[str, Any]] = []
        
        self._load_definitions()
        self._build_raw_tools()
        self._load_file_build_tools()
        
        if external_tools:
            self.merge_external_tools(external_tools)

    def _load_definitions(self):
        print(f"Loading API definitions from: {self.api_defs_dir}")
        tool_pattern = os.path.join(self.api_defs_dir, "*", "tools.json")
        type_pattern = os.path.join(self.api_defs_dir, "*", "types.json")

        for tool_file in glob.glob(tool_pattern):
            service_dir = os.path.dirname(tool_file)
            service_name = os.path.basename(service_dir)
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

    def _load_file_build_tools(self):
        try:
            file_build_caller = FileBuildToolCaller(self.working_directory)
            self.file_build_tools = file_build_caller.get_tools_schema()
            print(f"Loaded {len(self.file_build_tools)} file build tools")
        except Exception as e:
            print(f"Error loading file build tools: {e}")
            self.file_build_tools = []

    def _transform_fields(self, schema_fragment: Any) -> Any:
        if not isinstance(schema_fragment, dict):
            return schema_fragment
       
        if schema_fragment.get("type") == "enum" and "values" in schema_fragment:
            enum_vals = list(schema_fragment.pop("values").keys())
            schema_fragment["type"] = "string"
            schema_fragment["enum"] = enum_vals
            
            if "description" not in schema_fragment:
                 schema_fragment["description"] = f"Must be one of: {', '.join(enum_vals)}"
            else:
                 schema_fragment["description"] += f" Must be one of: {', '.join(enum_vals)}"

        if "properties" in schema_fragment and isinstance(schema_fragment["properties"], dict):
            schema_fragment["properties"] = {
                k: self._transform_fields(v) for k, v in schema_fragment["properties"].items()
            }
        if "items" in schema_fragment:
             schema_fragment["items"] = self._transform_fields(schema_fragment["items"])
        if "additionalProperties" in schema_fragment:
             schema_fragment["additionalProperties"] = self._transform_fields(schema_fragment["additionalProperties"])

        return schema_fragment

    def _build_raw_tools(self):
        """
        Builds the initial list of OpenAI tool definitions from loaded data.
        Refactored and generalized from build_openai_tools in call.py.
        """
        print("Building initial tool definitions...")
        all_tools = []
        request_types_map = {}

        for service_name, service_types_content in self.types_data.items(): 
            all_type_definitions_for_service = []
            if isinstance(service_types_content, dict):
                for file_path_key in service_types_content: 
                    file_type_list = service_types_content[file_path_key]
                    if isinstance(file_type_list, list):
                        all_type_definitions_for_service.extend(file_type_list)
            elif isinstance(service_types_content, list):
                all_type_definitions_for_service = service_types_content
            else:
                print(f"Warning: Unexpected format for types_data[{service_name}], type is {type(service_types_content)}. Skipping.")
                continue

            for type_info in all_type_definitions_for_service:
                if type_info.get("type") == "function": 
                    type_name = type_info.get("name")
                    if type_name:
                        map_key = f"{service_name}.{type_name}"
                        request_types_map[map_key] = type_info

        for service_name, service_tools in self.tools_data.items():
            if not isinstance(service_tools, dict):
                 continue
            
            for service_class_name, service_class_def in service_tools.items():
                 if not isinstance(service_class_def, dict) or "methods" not in service_class_def:
                      continue

                 for method in service_class_def.get("methods", []):
                    func_def = method.get("function", {})
                    method_name = func_def.get("name")
                    request_types = func_def.get("request_types", [])

                    if not method_name or not request_types:
                         continue

                    raw_request_type_name_from_tools = request_types[0]
                    base_request_type_name = raw_request_type_name_from_tools.split('.')[-1]
                    request_type_key = f"{service_name}.{base_request_type_name}"

                    if request_type_key not in request_types_map:
                        continue

                    type_info = request_types_map[request_type_key]
                    parameters_copy = copy.deepcopy(type_info.get("parameters", {}))
                    parameters_transformed = self._transform_fields(parameters_copy)
                    tool_name_for_openai = f"{service_name}_{method_name}"

                    openai_tool = {
                        "type": "function",
                        "function": {
                            "name": tool_name_for_openai,
                            "description": func_def.get("description", type_info.get("description", f"Calls the {tool_name_for_openai} method.")),
                            "parameters": parameters_transformed,
                        }
                    }
                    all_tools.append(openai_tool)

        self.raw_tools = all_tools
        print(f"Finished building {len(self.raw_tools)} raw tools.")

        self._type_schema_map = {}
        for service_name, service_types_file_content in self.types_data.items():
             if isinstance(service_types_file_content, dict):
                 for file_path, type_list in service_types_file_content.items():
                     if isinstance(type_list, list):
                         for type_info in type_list:
                             type_name = type_info.get("name")
                             if type_name:

                                 full_type_name = f"{service_name}.{type_name}"
                                 self._type_schema_map[full_type_name] = type_info
                                
                                 reference = type_info.get("reference")
                                 if reference:
                                      self._type_schema_map[reference] = type_info
             else:
                 print(f"Warning: Unexpected format for types_data[{service_name}]")


    def get_formatted_tools(self, query: Optional[str] = None, similarity_threshold: float = 0.6) -> List[Dict[str, Any]]:
        """
        Returns the list of tools formatted for OpenAI.
        Optionally filters tools/parameters based on query similarity (feature from call.py).
        """
        all_tools = self.raw_tools.copy()
        all_tools.extend(self.file_build_tools)
        
        if query:
            print(f"Query-based filtering not yet implemented. Returning all tools.")

        return all_tools

    def get_file_build_tools(self) -> List[Dict[str, Any]]:
        return self.file_build_tools

    def get_api_tools(self) -> List[Dict[str, Any]]:
        return self.raw_tools

    def get_available_tools(self) -> List[str]:
        api_tool_names = [tool["function"]["name"] for tool in self.raw_tools]
        file_build_tool_names = [tool["function"]["name"] for tool in self.file_build_tools]
        return api_tool_names + file_build_tool_names

    def get_tool_counts(self) -> Dict[str, int]:
        return {
            "api_tools": len(self.raw_tools),
            "file_build_tools": len(self.file_build_tools),
            "total_tools": len(self.raw_tools) + len(self.file_build_tools)
        }

    def get_request_types_for_method(self, service_method_name: str) -> List[str]:
        """
        Finds the original request type names associated with a combined service.method name.
        Example: input 'vpcaccess_v1_create_connector', find associated request types in tools.json.
        Returns the *original* type names (without service prefix).
        """
        found_service_key = None
        method_name = None
        for key in self.tools_data.keys():
            if service_method_name.startswith(f"{key}_"):
                if found_service_key is None or len(key) > len(found_service_key):
                     found_service_key = key
                     method_name = service_method_name[len(key) + 1:] 

        if not found_service_key or not method_name:
            print(f"Error: Could not reliably split tool name '{service_method_name}' into a known service key and method name.")
            print(f"  Known service keys: {list(self.tools_data.keys())}")
            return []
        
        service_name = found_service_key 

        service_class_definitions = self.tools_data[service_name]
        if not isinstance(service_class_definitions, dict):
             print(f"Warning: Expected dict for tools_data[{service_name}], got {type(service_class_definitions)}. Cannot find methods.")
             return []
        
        for service_class_name, service_class_def in service_class_definitions.items():
            methods_list = service_class_def.get("methods", [])
            if not isinstance(methods_list, list):
                print(f"Warning: Expected list for methods in {service_class_name}, got {type(methods_list)}.")
                continue 

            for method_def in methods_list:
                fn_info = method_def.get("function", {})
                if fn_info.get("name") == method_name:
                    request_types = fn_info.get("request_types", [])
                    if request_types:
                        print(f"Found request types {request_types} for {service_method_name}")
                        return request_types 
                    else:
                        print(f"Warning: Method {service_method_name} found but has no request_types defined.")
                        return []

        print(f"Method '{method_name}' not found under any service class in {service_name}/tools.json (derived from tool name '{service_method_name}')")
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
        
        for tool_def in self.file_build_tools:
            if tool_def.get("function", {}).get("name") == tool_name:
                return tool_def["function"].get("parameters")
        
        return None

    def merge_external_tools(self, external_tools: List[Dict[str, Any]]):
        """
        Merge a list of OpenAI-compatible tool schemas (e.g., from file_build_tools) into the KnowledgeBase.
        This allows file tools to be available for planning and execution.
        """
        if not isinstance(external_tools, list):
            print("merge_external_tools: Provided external_tools is not a list.")
            return
        initial_count = len(self.raw_tools)
        self.raw_tools.extend(external_tools)
        print(f"Merged {len(external_tools)} external tools. Total tools now: {len(self.raw_tools)} (was {initial_count})")

    def is_file_build_tool(self, tool_name: str) -> bool:
        """Check if a tool is a file/build related tool."""
        file_build_tool_names = {
            'read_file', 'write_file', 'list_files', 'copy_file', 'template_file',
            'detect_project_type', 'build_project', 'test_project', 'lint_project',
            'generate_dockerfile', 'build_docker_image', 'run_docker_container',
            'docker_compose_up', 'execute_command'
        }
        return tool_name in file_build_tool_names
