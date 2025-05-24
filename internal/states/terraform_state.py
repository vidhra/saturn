from typing import Tuple, Type, List, Dict, Any
import json
from .base_state import BaseState, StateMachineContext

# Import other state classes for transitions
from .processing_results_state import ProcessingResultsState
from .failed_state import FailedState

class TerraformState(BaseState):
    """State responsible for executing Terraform configurations and managing infrastructure as code."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: TERRAFORM_EXECUTION ---")
        
        # Check if we have Terraform executor in context
        terraform_executor = getattr(context, 'terraform_executor', None)
        if not terraform_executor:
            error_msg = "Terraform executor not available in context"
            print(f"[Error] {error_msg}")
            context.current_errors.append({
                "method": "TerraformState",
                "error": error_msg,
                "arguments": {}
            })
            return FailedState, context

        # Get selected tools for Terraform execution
        tools_to_execute = context.selected_tools_for_execution
        if not tools_to_execute:
            print("No Terraform tools selected for execution. Transitioning to PROCESSING_RESULTS.")
            context.execution_results = []
            return ProcessingResultsState, context

        print(f"Executing {len(tools_to_execute)} Terraform operation(s)...")
        execution_results: List[Tuple[str, bool, Any]] = []
        
        # Execute Terraform operations
        for tool_call in tools_to_execute:
            tool_name = tool_call.get('name', 'terraform_operation')
            tool_args = tool_call.get('arguments', {})
            
            print(f"  Executing Terraform operation: {tool_name}")
            
            try:
                # Extract execution parameters
                execution_mode = tool_args.get('execution_mode', 'terraform')
                configuration = tool_args.get('configuration', '')
                step_id = tool_args.get('step_id', tool_name)
                
                # Execute using Terraform executor
                success, result = await terraform_executor.execute(
                    configuration,
                    context.console if hasattr(context, 'console') else None,
                    step_id,
                    execution_mode
                )
                
                execution_results.append((tool_name, success, result))
                
                if success:
                    print(f"  ✓ Terraform operation {tool_name} completed successfully")
                    
                    # Store Terraform outputs in context for later use
                    if isinstance(result, dict) and 'outputs' in result:
                        if not hasattr(context, 'terraform_outputs'):
                            context.terraform_outputs = {}
                        context.terraform_outputs[step_id] = result['outputs']
                        
                else:
                    print(f"  ✗ Terraform operation {tool_name} failed: {result}")
                    
            except Exception as e:
                print(f"  [Error] Exception during Terraform execution: {str(e)}")
                execution_results.append((tool_name, False, f"Exception: {str(e)}"))
                context.current_errors.append({
                    "method": "TerraformState.execute",
                    "error": f"Terraform execution failed: {str(e)}",
                    "arguments": tool_args
                })

        # Store execution results in context
        context.execution_results = execution_results
        
        # Check if all operations succeeded
        all_succeeded = all(result[1] for result in execution_results)
        
        if all_succeeded:
            print("All Terraform operations completed successfully. Transitioning to PROCESSING_RESULTS.")
            return ProcessingResultsState, context
        else:
            print("Some Terraform operations failed. Transitioning to FAILED.")
            return FailedState, context

class TerraformPlanningState(BaseState):
    """State responsible for planning Terraform operations based on DAG analysis."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: TERRAFORM_PLANNING ---")
        
        # Check if we have a DAG definition to work with
        if not context.dag_definition:
            error_msg = "No DAG definition available for Terraform planning"
            print(f"[Error] {error_msg}")
            context.current_errors.append({
                "method": "TerraformPlanningState",
                "error": error_msg,
                "arguments": {}
            })
            return FailedState, context

        # Analyze DAG for Terraform-suitable operations
        terraform_operations = self._analyze_dag_for_terraform(context.dag_definition)
        
        if not terraform_operations:
            print("No operations suitable for Terraform found. Transitioning to regular execution.")
            # Import the regular executing state
            from .executing_state import ExecutingState
            return ExecutingState, context
        
        print(f"Found {len(terraform_operations)} operations suitable for Terraform execution")
        
        # Prepare Terraform configurations
        terraform_tools = []
        for op in terraform_operations:
            terraform_config = self._prepare_terraform_config(op, context)
            if terraform_config:
                terraform_tools.append(terraform_config)
        
        # Update context with Terraform tools
        context.selected_tools_for_execution = terraform_tools
        
        print(f"Prepared {len(terraform_tools)} Terraform configurations. Transitioning to TERRAFORM_EXECUTION.")
        return TerraformState, context

    def _analyze_dag_for_terraform(self, dag_definition: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Analyze DAG to identify operations suitable for Terraform."""
        
        terraform_operations = []
        nodes = dag_definition.get("nodes", {})
        
        # Keywords that suggest Terraform suitability
        terraform_keywords = [
            'template', 'infrastructure', 'provision', 'deployment',
            'instance-template', 'network', 'firewall', 'sql-instance',
            'cluster', 'load-balancer', 'storage'
        ]
        
        for node_id, node_data in nodes.items():
            description = node_data.get('description', '').lower()
            tool_to_use = node_data.get('tool_to_use', '')
            
            # Check if this operation would benefit from Terraform
            is_terraform_suitable = (
                tool_to_use == 'terraform' or
                any(keyword in description for keyword in terraform_keywords) or
                'create' in description and any(keyword in description for keyword in ['instance', 'network', 'firewall'])
            )
            
            if is_terraform_suitable:
                terraform_operations.append({
                    'node_id': node_id,
                    'node_data': node_data,
                    'description': description
                })
        
        return terraform_operations

    def _prepare_terraform_config(self, operation: Dict[str, Any], context: StateMachineContext) -> Dict[str, Any]:
        """Prepare a Terraform configuration for a specific operation."""
        
        node_id = operation['node_id']
        node_data = operation['node_data']
        description = operation['description']
        
        # Extract cloud provider
        cloud_provider = node_data.get('cloud_provider', 'gcp')
        
        if cloud_provider != 'gcp':
            print(f"  [Warning] Terraform conversion only supports GCP currently, skipping {node_id}")
            return None
        
        # Try to extract or infer the gcloud command
        gcloud_command = None
        
        # Check if there's an explicit command
        if 'command' in node_data:
            gcloud_command = node_data['command']
        else:
            # Try to infer command from description and tool
            gcloud_command = self._infer_gcloud_command(node_data)
        
        if not gcloud_command:
            print(f"  [Warning] Could not determine gcloud command for {node_id}")
            return None
        
        return {
            'name': f'terraform_{node_id}',
            'arguments': {
                'configuration': gcloud_command,
                'execution_mode': 'convert',  # Convert from gcloud to Terraform
                'step_id': node_id,
                'description': description
            }
        }

    def _infer_gcloud_command(self, node_data: Dict[str, Any]) -> str:
        """Infer a gcloud command from node data."""
        
        description = node_data.get('description', '').lower()
        
        # Simple command inference based on description patterns
        if 'instance template' in description and 'create' in description:
            # Extract template name if possible
            words = description.split()
            template_name = None
            for i, word in enumerate(words):
                if word in ['template', 'named'] and i + 1 < len(words):
                    template_name = words[i + 1].strip("'\"")
                    break
            
            if template_name:
                return f"gcloud compute instance-templates create {template_name} --machine-type=e2-medium --image-family=debian-11 --image-project=debian-cloud"
        
        elif 'network' in description and 'create' in description:
            # Extract network name if possible
            words = description.split()
            network_name = None
            for i, word in enumerate(words):
                if word in ['network', 'named'] and i + 1 < len(words):
                    network_name = words[i + 1].strip("'\"")
                    break
            
            if network_name:
                return f"gcloud compute networks create {network_name} --subnet-mode=auto"
        
        # Add more inference patterns as needed
        
        return None

class TerraformImportState(BaseState):
    """State responsible for importing existing GCP resources into Terraform state."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: TERRAFORM_IMPORT ---")
        
        # Check if we have import specifications
        import_specs = getattr(context, 'terraform_import_specs', [])
        if not import_specs:
            print("No Terraform import specifications found. Transitioning to PROCESSING_RESULTS.")
            return ProcessingResultsState, context
        
        terraform_executor = getattr(context, 'terraform_executor', None)
        if not terraform_executor:
            error_msg = "Terraform executor not available for import operations"
            print(f"[Error] {error_msg}")
            context.current_errors.append({
                "method": "TerraformImportState",
                "error": error_msg,
                "arguments": {}
            })
            return FailedState, context
        
        print(f"Importing {len(import_specs)} existing resources into Terraform state...")
        
        import_results = []
        
        for spec in import_specs:
            resource_address = spec.get('resource_address')
            resource_id = spec.get('resource_id')
            
            if not resource_address or not resource_id:
                print(f"  [Warning] Skipping invalid import spec: {spec}")
                continue
            
            print(f"  Importing {resource_address} -> {resource_id}")
            
            try:
                # This would use the terraform import command
                # For now, just record the import intention
                import_result = terraform_executor.import_existing_resources({
                    resource_address: resource_id
                })
                
                import_results.append({
                    'resource_address': resource_address,
                    'resource_id': resource_id,
                    'success': True,
                    'result': import_result
                })
                
                print(f"  ✓ Successfully imported {resource_address}")
                
            except Exception as e:
                print(f"  ✗ Failed to import {resource_address}: {e}")
                import_results.append({
                    'resource_address': resource_address,
                    'resource_id': resource_id,
                    'success': False,
                    'error': str(e)
                })
        
        # Store import results in context
        context.terraform_import_results = import_results
        
        # Check if all imports succeeded
        all_succeeded = all(result['success'] for result in import_results)
        
        if all_succeeded:
            print("All Terraform imports completed successfully. Transitioning to PROCESSING_RESULTS.")
            return ProcessingResultsState, context
        else:
            print("Some Terraform imports failed. Transitioning to PROCESSING_RESULTS with partial results.")
            return ProcessingResultsState, context 