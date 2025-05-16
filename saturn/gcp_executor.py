# Contains logic refactored from call.py for executing GCP API calls
import importlib
import json
import google.api_core.exceptions
import google.oauth2.service_account # Needed for credentials file
from typing import Dict, Any, Tuple, Optional, List
import asyncio
import traceback
# import re # No longer needed
from google.api_core.operation import Operation # Import Operation for type checking
from google.api_core.operation_async import AsyncOperation # Import AsyncOperation
from google.protobuf.json_format import MessageToDict # For result conversion
from rich.console import Console # Added console for rich printing

# Import necessary components from the package
from .knowledge_base import KnowledgeBase

# Mapping from service name prefix (used in tool names) to the actual google-cloud library package
# This needs to be maintained or generated dynamically.
# Example:
SERVICE_TO_LIBRARY_MAP = {
    "vpcaccess_v1": "google.cloud.vpcaccess_v1",
    "compute_v1": "google.cloud.compute_v1",
    "storage_v1": "google.cloud.storage_v1",
    "run_v2": "google.cloud.run_v2",
    # Add more services as needed
}

# Mapping from service name prefix to the Async Client class name within that library
# Example:
SERVICE_TO_CLIENT_CLASS_MAP = {
    "vpcaccess_v1": "VpcAccessServiceAsyncClient",
    "compute_v1": "InstancesAsyncClient", # Or other specific clients like NetworksAsyncClient etc.
    "storage_v1": "StorageAsyncClient",
    "run_v2": "JobsAsyncClient",
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
        # Add state tracking for steps
        self.step_results = {}
        self.current_step = None
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

    async def execute(
        self,
        service_method_name: str, # e.g., vpcaccess_v1.create_connector
        llm_args: Dict[str, Any], # Renamed args to llm_args for clarity
        knowledge_base: KnowledgeBase, # Pass real KB to get original request type name
        console: Console # Added console for rich printing
    ) -> Tuple[bool, Any]:
        """
        Dynamically executes a GCP API call based on the service and method name.
        Directly uses LLM provided args to instantiate the request object.
        Handles common GCP exceptions.
        Refactored from dynamic_executor in call.py.
        """
        console.print(f"  Executing GCP call: [bold cyan]{service_method_name}[/bold cyan]")

        # 1. Find the target request type(s) for this method
        request_type_names = knowledge_base.get_request_types_for_method(service_method_name)
        if not request_type_names:
            return False, f"Could not find request type definition for method '{service_method_name}' in Knowledge Base."
        
        # Assume the first type is the primary one for now
        # TODO: Handle methods with multiple potential request types?
        target_request_type_name = request_type_names[0] 
        console.print(f"    Target Request Type: [bold]{target_request_type_name}[/bold]")

        # 2. Dynamically import the necessary library and client
        try:
            # --- Find the correct service key and method name --- 
            found_service_key = None
            method_name_only = None # Extracted method name part
            known_service_keys = list(knowledge_base.tools_data.keys()) # Get keys from KB
            for key in known_service_keys:
                if service_method_name.startswith(f"{key}_"):
                     if found_service_key is None or len(key) > len(found_service_key):
                          found_service_key = key
                          method_name_only = service_method_name[len(key) + 1:]
            
            if not found_service_key or not method_name_only:
                 # Use the error message from KB as it lists known keys
                 return False, f"Could not reliably split tool name '{service_method_name}' into a known service key and method name (Known: {known_service_keys})."

            service_key_for_import = found_service_key # e.g., vpcaccess_v1
            # --- End splitting logic ---

            # Get the service definition to find the actual class name key
            service_tools_def = knowledge_base.tools_data.get(service_key_for_import)
            if not service_tools_def or not isinstance(service_tools_def, dict):
                 return False, f"Could not find service definition or definition is not a dict for key '{service_key_for_import}' in tools_data."
            
            # Assume the first key in the service definition is the Service Class Name
            service_class_name_actual = next(iter(service_tools_def.keys()), None)
            if not service_class_name_actual:
                 return False, f"Could not extract service class name key from definition for '{service_key_for_import}'."

            library_name = f"google.cloud.{service_key_for_import}"
            console.print(f"    Importing library: [italic]{library_name}[/italic]")
            module = importlib.import_module(library_name)
            
            # Use the extracted actual service class name for client lookup
            # client_class_base = service_key_for_import.split('_')[0]
            # client_class_name_pascal = self._to_pascal_case(client_class_base) + "Service" # Old logic
            client_class_name_pascal = service_class_name_actual # e.g. VpcAccessService

            # Heuristic: Try Async client first, then sync
            client_class = getattr(module, client_class_name_pascal + "AsyncClient", None)
            if not client_class:
                 client_class = getattr(module, client_class_name_pascal + "Client", None)
            if not client_class:
                 raise ImportError(f"Could not find {client_class_name_pascal}Client or {client_class_name_pascal}AsyncClient in {library_name}")
            
            console.print(f"    Initializing client: [italic]{client_class.__name__}[/italic]")
            # Use credentials if provided, otherwise rely on ADC
            if self.credentials_path:
                console.print("    Using provided credentials file.")
                credentials = google.oauth2.service_account.Credentials.from_service_account_file(self.credentials_path)
                client = client_class(credentials=credentials)
            else:
                console.print("    Using Application Default Credentials (ADC).")
                client = client_class()

            # Get the actual request class object
            request_class = getattr(module.types, target_request_type_name, None)
            if not request_class:
                # Fallback: Sometimes types are directly under the module
                request_class = getattr(module, target_request_type_name, None)
            if not request_class:
                 raise ImportError(f"Could not find request class '{target_request_type_name}' in {library_name} or {library_name}.types")

        except ImportError as e:
            return False, f"Import error: {e}"
        except Exception as e: # Catch other potential init errors
            return False, f"Client/Request initialization error: {e}"
        
        # 3. Construct the Request object using LLM args
        console.print(f"    Attempting to construct request object: [bold]{request_class.__name__}[/bold] with LLM args:")
        # console.print(llm_args) # Optional: Print the args for debugging

        # --- Prepare and Make the API Call --- 
        
        # Directly attempt to construct request object using LLM args
        print(f"Attempting to construct request object: {target_request_type_name} with LLM args:")
        # console.print(llm_args) # REMOVE this line - 'console' not defined here
        # from rich.console import Console # Temp import if needed
        # Console().print(llm_args)
        try:
            # === Direct Instantiation ===
            # Special handling for project_id - ensure it's set if needed by the constructor
            # The actual required fields are determined by the RequestClass constructor
            constructor_args = llm_args.copy()
            # Ensure parent is constructed if needed (common pattern)
            if 'parent' not in constructor_args and ('project' in constructor_args or self.gcp_project_id) and ('location' in constructor_args or 'region' in constructor_args):
                proj = self.gcp_project_id or constructor_args.get('project')
                loc = constructor_args.get('location') or constructor_args.get('region')
                if proj and loc:
                    constructor_args['parent'] = f"projects/{proj}/locations/{loc}"
                    print(f"  Auto-constructed 'parent': {constructor_args['parent']}")
                # Clean up potentially redundant args if parent was constructed
                constructor_args.pop('project', None)
                constructor_args.pop('location', None)
                constructor_args.pop('region', None)
            
            # Ensure project_id is present if required by the library (less common now with parent)
            # if 'project_id' not in constructor_args and self.gcp_project_id:
            #    constructor_args['project_id'] = self.gcp_project_id
                
            request_obj = request_class(**constructor_args)
            # === End Direct Instantiation ===
        except TypeError as te:
             # TypeError likely indicates mismatch between llm_args and RequestClass fields
             print(f"[Error] Failed to construct {target_request_type_name}: Argument mismatch.")
             print(f"  LLM Args: {llm_args}")
             print(f"  Error: {te}")
             return False, f"Argument mismatch constructing {target_request_type_name}: {te}" 
        except Exception as const_err:
            # Catch other potential errors during construction
            print(f"[Error] Failed to construct {target_request_type_name}: {const_err}")
            return False, f"Construction error for {target_request_type_name}: {const_err}" 

        console.print(f"Calling method: {method_name_only}") # Use extracted method name
        # print(f"Request object: {request_obj}") # Can be very verbose
        # api_result = await getattr(client, service_method_name)(request=request_obj) # Old call using full name
        api_result = await getattr(client, method_name_only)(request=request_obj)
        console.print("Initial GCP API call successful.")

        # --- Handle Result (Check for LRO, Pagers, etc.) --- 
        final_result = api_result
        
        # Check if the result is an AsyncOperation (LRO)
        if isinstance(api_result, AsyncOperation):
            console.print(f"Result is an AsyncOperation (LRO). Waiting for completion... (Operation ID: {api_result.operation.name})")
            # Wait for the LRO to complete. Timeout can be added.
            try:
                # The timeout here is for the wait itself, not the operation total time
                final_result = await asyncio.wait_for(api_result.result(), timeout=self.config.get('gcp_lro_wait_timeout', 300.0))
                console.print("LRO completed successfully.")
            except asyncio.TimeoutError:
                console.print("Warning: Timed out waiting for LRO to complete.")
                return False, f"Timed out waiting for operation {api_result.operation.name} to complete."
            except Exception as lro_err:
                console.print(f"Error occurred during LRO execution: {lro_err}")
                # Try to get metadata or error details from the operation if possible
                op_error = getattr(api_result.operation, 'error', None)
                return False, f"Operation {api_result.operation.name} failed: {lro_err} {op_error or ''}"

        # Handle potential pagers/async iterators AFTER LRO check (LRO result might be iterable)
        elif hasattr(final_result, "__aiter__"):
            console.print("Result is an async iterator/pager. Collecting items...")
            collected_results = []
            async for item in final_result:
                # Convert proto messages to dicts
                try:
                     # Ensure 'item' is a protobuf message; otherwise, this will fail.
                     # It's generally good practice for GCP client libraries.
                     collected_results.append(MessageToDict(item, preserving_proto_field_name=True, including_default_value_fields=True))
                except Exception as conversion_err:
                     # Log the actual item type if conversion fails for debugging
                     console.print(f"Warning: Failed to convert item of type {type(item)} to dict: {conversion_err}. Appending raw item.")
                     collected_results.append(item) # Keep raw item if conversion fails
            console.print(f"Collected {len(collected_results)} items.")
            return True, collected_results # Return list of results
        
        # --- Convert single result to Dict --- 
        try:
             # Attempt conversion even if not LRO/pager
             final_result_dict = MessageToDict(final_result, preserving_proto_field_name=True, including_default_value_fields=True)
             console.print("Converted final result to dictionary.")
             return True, final_result_dict
        except Exception as conversion_err:
             # Log the actual item type if conversion fails for debugging
             console.print(f"Warning: Failed to convert final result of type {type(final_result)} to dict: {conversion_err}. Returning raw result.")
             return True, final_result # Return raw result if conversion fails

    async def execute_step(
        self,
        step_id: str,
        service_method_name: str,
        llm_args: Dict[str, Any],
        knowledge_base: KnowledgeBase,
        console: Console,
        dependencies: List[str] = None
    ) -> Tuple[bool, Any]:
        """
        Execute a single step in the DAG, handling dependencies and state tracking.
        
        Args:
            step_id: Unique identifier for this step
            service_method_name: The GCP service method to call
            llm_args: Arguments for the method
            knowledge_base: Knowledge base for API definitions
            console: Console for logging
            dependencies: List of step IDs this step depends on
            
        Returns:
            Tuple of (success, result)
        """
        try:
            # Store current step for context
            self.current_step = step_id
            
            # Check dependencies
            if dependencies:
                for dep in dependencies:
                    if dep not in self.step_results:
                        return False, f"Dependency {dep} not executed yet"
                    if not self.step_results[dep][0]:  # Check if dependency failed
                        return False, f"Dependency {dep} failed: {self.step_results[dep][1]}"
            
            # Execute the actual GCP call
            success, result = await self.execute(service_method_name, llm_args, knowledge_base, console)
            
            # Store result
            self.step_results[step_id] = (success, result)
            
            return success, result
            
        except Exception as e:
            error_msg = f"Error executing step {step_id}: {str(e)}"
            console.print(f"[bold red]{error_msg}[/bold red]")
            self.step_results[step_id] = (False, error_msg)
            return False, error_msg

    async def execute_dag(
        self,
        dag_definition: Dict[str, Any],
        knowledge_base: KnowledgeBase,
        console: Console
    ) -> Dict[str, Tuple[bool, Any]]:
        """
        Execute a DAG of GCP operations.
        
        Args:
            dag_definition: Dictionary containing nodes, edges, and execution order
            knowledge_base: Knowledge base for API definitions
            console: Console for logging
            
        Returns:
            Dictionary mapping step IDs to their (success, result) tuples
        """
        try:
            # Reset state
            self.step_results = {}
            
            # Get execution order
            execution_order = dag_definition.get("execution_order", [])
            if not execution_order:
                raise ValueError("No execution order defined in DAG")
            
            # Execute steps in order
            for step_id in execution_order:
                node = dag_definition["nodes"][step_id]
                
                console.print(f"\n[bold cyan]Executing step {step_id}[/bold cyan]")
                console.print(f"Description: {node.get('description', 'No description')}")
                
                if node.get("dependencies"):
                    console.print(f"Dependencies: {', '.join(node['dependencies'])}")
                
                success, result = await self.execute_step(
                    step_id=step_id,
                    service_method_name=node["tool"],
                    llm_args=node["parameters"],
                    knowledge_base=knowledge_base,
                    console=console,
                    dependencies=node.get("dependencies", [])
                )
                
                if not success:
                    console.print(f"[bold red]Step {step_id} failed:[/bold red] {result}")
                    # Optionally break on first failure
                    # break
                else:
                    console.print(f"[bold green]Step {step_id} completed successfully[/bold green]")
            
            return self.step_results
            
        except Exception as e:
            console.print(f"[bold red]Error executing DAG:[/bold red] {str(e)}")
            return self.step_results

# Helper (if needed, from call.py)
# def convert_strings_to_json(data: dict) -> dict:
#     """Recursively attempt to parse any string fields as JSON objects."""
#     # ... implementation ... 