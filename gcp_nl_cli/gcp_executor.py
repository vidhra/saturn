# Contains logic refactored from call.py for executing GCP API calls
import importlib
import json
import google.api_core.exceptions
import google.oauth2.service_account # Needed for credentials file
from typing import Dict, Any, Tuple, Optional, List
import asyncio
import traceback
import re # Needed for robust key matching

# Import necessary components from the package
from .knowledge_base import KnowledgeBase

# Mapping from service name prefix (used in tool names) to the actual google-cloud library package
# This needs to be maintained or generated dynamically.
# Example:
SERVICE_TO_LIBRARY_MAP = {
    "vpcaccess_v1": "google.cloud.vpcaccess_v1",
    "compute_v1": "google.cloud.compute_v1",
    "storage_v1": "google.cloud.storage_v1",
    # Add more services as needed
}

# Mapping from service name prefix to the Async Client class name within that library
# Example:
SERVICE_TO_CLIENT_CLASS_MAP = {
    "vpcaccess_v1": "VpcAccessServiceAsyncClient",
    "compute_v1": "InstancesAsyncClient", # Or other specific clients like NetworksAsyncClient etc.
    "storage_v1": "StorageAsyncClient",
    # Add more services as needed
}

class GcpExecutor:
    def __init__(self, config: Dict[str, Any]):
        """Initializes the GCP Executor."""
        self.config = config
        self.gcp_project_id = config.get('gcp_project_id')
        self.credentials_path = config.get('gcp_credentials_path')
        # Initialize clients dynamically as needed or maintain a cache
        self.clients = {}
        print(f"GCP Executor initialized for project: {self.gcp_project_id}")

    async def _get_client(self, service_name: str) -> Any:
        """Dynamically imports and initializes a GCP Async Client."""
        if service_name in self.clients:
            return self.clients[service_name]

        library_name = SERVICE_TO_LIBRARY_MAP.get(service_name)
        client_class_name = SERVICE_TO_CLIENT_CLASS_MAP.get(service_name)

        if not library_name or not client_class_name:
            raise ValueError(f"No library or client class mapping found for service: {service_name}")

        try:
            print(f"Importing library: {library_name}")
            module = importlib.import_module(library_name)
            ClientClass = getattr(module, client_class_name)
            
            print(f"Initializing client: {client_class_name}")
            # Pass credentials explicitly if path is provided, otherwise use ADC
            if self.credentials_path:
                 print(f"Using credentials from: {self.credentials_path}")
                 credentials = google.oauth2.service_account.Credentials.from_service_account_file(self.credentials_path)
                 client = ClientClass(credentials=credentials)
            else:
                 # Use Application Default Credentials (ADC)
                 print("Using Application Default Credentials (ADC).")
                 client = ClientClass()

            self.clients[service_name] = client
            return client
        except ImportError:
            raise ImportError(f"Could not import GCP library '{library_name}'. Is it installed? (e.g., pip install google-cloud-compute)")
        except AttributeError:
             raise AttributeError(f"Could not find client class '{client_class_name}' in library '{library_name}'. Check SERVICE_TO_CLIENT_CLASS_MAP.")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize GCP client for {service_name}: {e}")


    def _get_request_class(self, service_name: str, request_type_name: str) -> Any:
        """Dynamically imports the Request class (e.g., CreateConnectorRequest)."""
        library_name = SERVICE_TO_LIBRARY_MAP.get(service_name)
        if not library_name:
             raise ValueError(f"No library mapping found for service: {service_name}")
        
        try:
            module = importlib.import_module(library_name)
            RequestClass = getattr(module, request_type_name)
            return RequestClass
        except ImportError:
             raise ImportError(f"Could not import GCP library '{library_name}' to get request type '{request_type_name}'.")
        except AttributeError:
             raise AttributeError(f"Could not find request class '{request_type_name}' in library '{library_name}'.")
        except Exception as e:
             raise RuntimeError(f"Failed to get request class {request_type_name} for {service_name}: {e}")

    def _normalize_key(self, key: str) -> str:
        """Converts camelCase or snake_case to lowercase snake_case for comparison."""
        key = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', key)
        key = re.sub('([a-z0-9])([A-Z])', r'\1_\2', key).lower()
        # Specific common synonym groups (map to a canonical name)
        synonyms = {
            "connector_id": "connector_id", "name": "connector_id", "connectorid": "connector_id",
            "region": "region", "location": "region",
            "ip_cidr_range": "ip_cidr_range", "ipcidrrrange": "ip_cidr_range", "cidr": "ip_cidr_range"
            # Add more synonyms as needed
        }
        normalized = key.replace("_", "") # Also check without underscores
        for k, v in synonyms.items():
            if key == k or normalized == k.replace("_", ""):
                return v
        return key # Return original if no synonym mapping

    def _find_llm_arg_value(self, target_schema_key: str, llm_args: Dict[str, Any]) -> Optional[Any]:
        """
        Finds a value in the potentially messy LLM args for a specific schema key.
        Handles synonyms, case variations, and 'body' nesting.
        """
        canonical_target_key = self._normalize_key(target_schema_key)
        print(f"    _find_llm_arg: Searching for schema key '{target_schema_key}' (canonical: '{canonical_target_key}')")

        # 1. Check top-level args (case-insensitive and synonym check)
        for llm_key, llm_value in llm_args.items():
            canonical_llm_key = self._normalize_key(llm_key)
            if canonical_llm_key == canonical_target_key:
                print(f"      Found match at top level: '{llm_key}' -> '{llm_value}'")
                return llm_value

        # 2. Check inside 'body' if it exists
        body = llm_args.get("body")
        if isinstance(body, dict):
            print(f"      Checking inside 'body' field...")
            for body_key, body_value in body.items():
                canonical_body_key = self._normalize_key(body_key)
                if canonical_body_key == canonical_target_key:
                     print(f"      Found match inside 'body': '{body_key}' -> '{body_value}'")
                     return body_value

        print(f"      Value for '{target_schema_key}' not found.")
        return None # Value not found


    def _build_request_object(
        self,
        schema: Dict[str, Any],
        llm_args: Dict[str, Any], # Pass the original, full llm_args down
        knowledge_base: KnowledgeBase,
        parent_required_fields: List[str] = [], # Keep track of parent requirements
        is_nested: bool = False # Flag to indicate if we are building a nested object
    ) -> Optional[Dict[str, Any]]: # Return Optional to indicate potential failure of optional objects
        """
        Builds the request object dictionary based on the schema,
        using configured values and extracting specific values from LLM args.
        Returns None if building an OPTIONAL nested object fails due to missing required fields inside it.
        """
        built_object = {}
        schema_props = schema.get("properties", {})
        schema_required = schema.get("required", [])
        level_prefix = "  " * (1 if is_nested else 0)
        print(f"{level_prefix}Building object based on schema properties: {list(schema_props.keys())}")
        if not schema_props:
            print(f"{level_prefix}Warning: Schema has no properties defined.")
            return {} # Return empty for schemas with no properties

        successfully_built_something = False # Track if we actually assign any values

        for prop_name, prop_schema in schema_props.items():
            value = None
            prop_type = prop_schema.get("type")
            prop_ref = prop_schema.get("reference")
            is_current_prop_required = prop_name in schema_required

            # --- Special Handling for specific fields (only at top level) ---
            if not is_nested and prop_name == "parent":
                 print(f"{level_prefix}  Handling special field: 'parent'")
                 llm_region = self._find_llm_arg_value("region", llm_args)
                 project = self.gcp_project_id
                 if not project:
                     project = self._find_llm_arg_value("project", llm_args)
                     if not project or project == "your-project-id":
                          raise ValueError("Project ID is missing or placeholder. Configure it or provide a valid one.")
                 if project and llm_region:
                     value = f"projects/{project}/locations/{llm_region}"
                     print(f"{level_prefix}    Constructed 'parent': {value}")

            # --- Handle Nested Objects --- 
            elif prop_type == "object" or prop_ref:
                print(f"{level_prefix}  Handling nested object field: '{prop_name}' (Required by current schema: {is_current_prop_required})")
                nested_schema = prop_schema.get("resolved_schema")
                if not nested_schema and prop_ref:
                    nested_schema = knowledge_base.get_type_schema(prop_ref)
                
                if nested_schema:
                    actual_nested_schema = nested_schema.get("parameters", nested_schema)
                    if actual_nested_schema.get("type") == "object":
                        nested_llm_dict = self._find_llm_arg_value(prop_name, llm_args)
                        build_args = nested_llm_dict if isinstance(nested_llm_dict, dict) else llm_args
                        source_msg = "nested dict" if isinstance(nested_llm_dict, dict) else "main LLM args"
                        print(f"{level_prefix}    Building '{prop_name}' recursively using {source_msg}")
                        
                        try:
                            # Pass current schema's required fields for context
                            nested_object = self._build_request_object(
                                actual_nested_schema, 
                                build_args, 
                                knowledge_base, 
                                parent_required_fields=schema_required, # Pass parent's reqs
                                is_nested=True
                            )
                            # If build returns None (optional failed build), keep value as None
                            # Otherwise, assign the built dict
                            if nested_object is not None:
                                 value = nested_object 
                                 # Check if the nested object is empty - might still be valid if all its fields were optional
                                 if not value:
                                     print(f"{level_prefix}    Note: Recursive build for '{prop_name}' resulted in an empty dictionary.")
                                     # We might still assign it if the field itself is optional
                                     # Or discard if it signifies failure?
                                     # If prop_name is required, but nested build is empty, validation later will fail

                        except ValueError as ve:
                            # If the nested build failed due to missing fields *within it*,
                            # only re-raise if the nested property ITSELF is required by the *parent*
                            print(f"{level_prefix}    Caught ValueError during recursive build for '{prop_name}': {ve}")
                            if is_current_prop_required:
                                print(f"{level_prefix}    Property '{prop_name}' is required by parent. Re-raising error.")
                                raise ve # Re-raise if the field itself was required
                            else:
                                print(f"{level_prefix}    Property '{prop_name}' is optional. Suppressing build error.")
                                value = None # Failed to build optional nested object
                    else:
                         print(f"{level_prefix}  Warning: Resolved schema for nested '{prop_name}' is not type 'object'. Skipping recursive build.")
                else:
                     print(f"{level_prefix}  Warning: Could not resolve schema for nested property '{prop_name}' (ref: {prop_ref}). Skipping.")

            # --- Primitive Types --- 
            else:
                 print(f"{level_prefix}  Handling primitive field: '{prop_name}'")
                 value = self._find_llm_arg_value(prop_name, llm_args)

            # --- Assign Value --- 
            if value is not None:
                 # Only log assignment, not the value itself to avoid large logs
                 print(f"{level_prefix}  Assigning value for '{prop_name}'")
                 built_object[prop_name] = value
                 successfully_built_something = True
            # --- End Property Loop ---

        # --- Final Validation for the current level --- 
        print(f"{level_prefix}Validating required fields for current level: {schema_required}")
        missing_required = []
        for req_field in schema_required:
            if req_field not in built_object:
                 print(f"{level_prefix}Error: Missing required field '{req_field}' at this level.")
                 missing_required.append(req_field)

        if missing_required:
            raise ValueError(f"Failed to construct object. Missing required fields: {', '.join(missing_required)}")

        # If we are building a nested object that is optional in the parent,
        # and we didn't manage to assign *any* values to it (because LLM didn't provide them),
        # return None to signal it shouldn't be included in the parent. Check if it contains *any* value.
        if is_nested and not built_object and prop_name not in parent_required_fields:
             print(f"{level_prefix}Optional nested object '{prop_name}' is empty. Returning None.")
             return None

        print(f"{level_prefix}Finished building object. Keys: {list(built_object.keys())}")
        return built_object

    def _map_arguments_to_request_schema(
        self,
        args: Dict[str, Any], # These are the raw LLM args
        request_type_name: str,
        service_name: str,
        knowledge_base: KnowledgeBase
    ) -> Dict[str, Any]:
        """Builds the request object based on schema and LLM args."""
        print(f"Attempting SCHEMA-DRIVEN BUILD for request type: {request_type_name}")

        full_type_name = f"{service_name}.{request_type_name}"
        full_type_info = knowledge_base.get_type_schema(full_type_name)

        if not full_type_info:
             # Try without service prefix
             full_type_info = knowledge_base.get_type_schema(request_type_name)
             if not full_type_info:
                  raise ValueError(f"Cannot build request: Schema info not found for {full_type_name} or {request_type_name}")

        # --- Extract the actual schema from the 'parameters' field --- 
        target_schema = full_type_info.get("parameters")
        if not isinstance(target_schema, dict) or target_schema.get("type") != "object":
             # If 'parameters' is missing or not an object schema, something is wrong with types.json structure
             raise ValueError(f"Invalid schema structure found for {full_type_name or request_type_name}. Expected 'parameters' field with object schema.")
        # --- 

        print(f"Building request object using schema: {full_type_name or request_type_name}")
        print(f"LLM Args provided: {json.dumps(args, indent=2)}")

        built_request_obj = self._build_request_object(target_schema, args, knowledge_base)

        print(f"Constructed Request Object: {json.dumps(built_request_obj, indent=2)}")
        return built_request_obj

    async def execute(
        self,
        service_method_name: str, # e.g., vpcaccess_v1.create_connector
        args: Dict[str, Any],
        knowledge_base: KnowledgeBase # Pass real KB to get original request type name
    ) -> Tuple[bool, Any]:
        """
        Dynamically executes a GCP API call based on the service and method name.
        Handles common GCP exceptions.
        Refactored from dynamic_executor in call.py.
        """
        print(f"Executing GCP call: {service_method_name}")
        request_type_name = "UnknownRequest"
        try:
            # --- Determine Service, Method, Client, Request Type --- 
            if '.' not in service_method_name:
                 raise ValueError(f"Invalid service_method_name format: {service_method_name}. Expected 'service.method'.")
                 
            service_name, method_name = service_method_name.split('.', 1)
            
            # Get the original request type name(s) from the knowledge base
            request_type_names = knowledge_base.get_request_types_for_method(service_method_name)
            if not request_type_names:
                 return False, f"Could not find request type mapping for method: {service_method_name}"
            request_type_name = request_type_names[0] # Use first one

            client = await self._get_client(service_name)
            # Check if the method exists on the client
            if not hasattr(client, method_name):
                 raise AttributeError(f"Client object of type {type(client).__name__} has no method '{method_name}'")
            method_to_call = getattr(client, method_name)
            
            RequestClass = self._get_request_class(service_name, request_type_name)

            # --- Prepare and Make the API Call --- 
            raw_args = args # Original arguments from the tool call

            # Map arguments to the structure needed by the Request class
            try:
                mapped_args = self._map_arguments_to_request_schema(
                    raw_args,
                    request_type_name,
                    service_name,
                    knowledge_base
                )
            except ValueError as ve:
                 return False, f"Argument mapping error for {request_type_name}: {ve}"
            except Exception as e:
                 return False, f"Unexpected error during argument mapping for {request_type_name}: {e}"
            
            # Construct request object using the mapped arguments
            print(f"Constructing request object: {request_type_name} with mapped args: {json.dumps(mapped_args, indent=2)}")
            try:
                request_obj = RequestClass(**mapped_args)
            except TypeError as te:
                 # More informative TypeError
                 return False, f"Failed to construct {request_type_name}. Check if mapped arguments match its constructor. Error: {te}"

            print(f"Calling method: {method_name}")
            print(f"Request object: {request_obj}")
            result = await method_to_call(request=request_obj)
            print("GCP call successful.")
            
            # Handle potential pagers/async iterators
            if hasattr(result, "__aiter__"):
                print("Result is an async iterator, collecting items...")
                collected_results = []
                async for item in result:
                    # TODO: Convert proto messages to dicts for cleaner output/state?
                    # from google.protobuf.json_format import MessageToDict
                    # collected_results.append(MessageToDict(item))
                    collected_results.append(item) 
                print(f"Collected {len(collected_results)} items.")
                return True, collected_results # Return list of results
            else:
                 # TODO: Convert single proto message result to dict?
                # from google.protobuf.json_format import MessageToDict
                # return True, MessageToDict(result)
                 return True, result # Return single result

        # --- Error Handling (More specific) --- 
        except google.api_core.exceptions.InvalidArgument as e:
            return False, f"Invalid Argument (400) for {service_method_name}: {str(e)}"
        except google.api_core.exceptions.PermissionDenied as e:
            return False, f"Permission Denied (403) for {service_method_name}: {str(e)}"
        except google.api_core.exceptions.NotFound as e:
            return False, f"Not Found (404) for {service_method_name}: {str(e)}"
        except google.api_core.exceptions.AlreadyExists as e:
            return False, f"Already Exists (409) for {service_method_name}: {str(e)}"
        except google.api_core.exceptions.FailedPrecondition as e:
            return False, f"Failed Precondition (412) for {service_method_name}: {str(e)}"
        except google.api_core.exceptions.ResourceExhausted as e:
            return False, f"Resource Exhausted (429) for {service_method_name}: {str(e)}"
        except AttributeError as e:
            return False, f"Attribute Error during execution setup for {service_method_name}: {str(e)}"
        except ImportError as e:
             return False, f"Import Error during execution setup for {service_method_name}: {str(e)}"
        except TypeError as e:
            return False, f"Type Error (likely bad arguments for {request_type_name}): {str(e)}"
        except ValueError as e:
             return False, f"Value Error during execution setup for {service_method_name}: {str(e)}"
        except Exception as e:
            print(f"------ UNEXPECTED GCP EXECUTOR ERROR for {service_method_name} ------")
            traceback.print_exc()
            print("------------------------------------------------------------")
            return False, f"Unexpected Execution Error for {service_method_name}: {str(e)}"

# Helper (if needed, from call.py)
# def convert_strings_to_json(data: dict) -> dict:
#     """Recursively attempt to parse any string fields as JSON objects."""
#     # ... implementation ... 