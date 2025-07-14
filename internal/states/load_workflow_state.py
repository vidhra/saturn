from typing import Any, Dict, Tuple, Type

from rich.panel import Panel
from rich.table import Table

from .base_state import BaseState, StateMachineContext
from .executing_state import ExecutingState
from .failed_state import FailedState


class LoadWorkflowState(BaseState):
    """State responsible for loading Saturn workflows from .sat files."""

    async def run(
        self, context: StateMachineContext
    ) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: LOAD_WORKFLOW ---")
        
        console = context.console
        
        # Get the .sat file path from context
        sat_file_path = context.config.get("sat_file_path")
        if not sat_file_path:
            error_msg = "No .sat file path provided for workflow loading"
            print(f"Error: {error_msg}")
            context.current_errors.append({
                "method": "LOAD_WORKFLOW",
                "error": error_msg,
                "arguments": {}
            })
            return FailedState, context
        
        if console:
            console.print(
                Panel(
                    f"Loading Saturn workflow from: [cyan]{sat_file_path}[/cyan]",
                    title="[bold blue]Workflow Loading[/bold blue]",
                    border_style="blue"
                )
            )
        
        try:
            from internal.saturn_workflow import SaturnWorkflow
            workflow_handler = SaturnWorkflow()
            
            # Load the workflow
            dag, step_details_map, execution_order, original_query = workflow_handler.load_workflow(sat_file_path)
            
            # Validate the loaded workflow
            if not workflow_handler.validate_workflow(sat_file_path):
                error_msg = f"Workflow validation failed for: {sat_file_path}"
                print(f"Error: {error_msg}")
                context.current_errors.append({
                    "method": "LOAD_WORKFLOW",
                    "error": error_msg,
                    "arguments": {"file_path": sat_file_path}
                })
                return FailedState, context
            
            # Store workflow data in context
            context.dag = dag
            context.step_details_map = step_details_map
            context.execution_order = execution_order
            context.original_query = original_query  # Update context with original query from .sat file
            
            # Record the workflow loading in state recorder
            context.state_recorder.record_dag_structure({
                "nodes": {step_id: {
                    "description": details.get("description"),
                    "cloud_provider": details.get("cloud_provider"),
                    "dependencies": details.get("dependencies", []),
                    "tool_to_use": details.get("tool_to_use"),
                    "pass_output_to_next": details.get("pass_output_to_next"),
                } for step_id, details in step_details_map.items()},
                "edges": [f"{e.source} -> {e.target}" for e in dag.edges],
                "execution_order": execution_order
            })
            
            # Initialize all nodes in the state recorder
            for step_id, details in step_details_map.items():
                context.state_recorder.record_node_initialization(
                    node_id=step_id,
                    tool_name=details.get("tool_to_use", "cli_command_generation"),
                    attempt=0,
                    args={"cloud_provider": details.get("cloud_provider")},
                    initial_status="LOADED_FROM_SAT"
                )
            
            if console:
                # Display loaded workflow summary
                summary_table = Table(
                    title=f"Loaded Workflow Summary",
                    show_header=True,
                    header_style="bold magenta"
                )
                summary_table.add_column("Step ID", style="cyan")
                summary_table.add_column("Provider", style="dim")
                summary_table.add_column("Description", style="")
                summary_table.add_column("Dependencies", style="dim")
                summary_table.add_column("Tool", style="green")
                
                for step_id in execution_order:
                    details = step_details_map.get(step_id, {})
                    provider = details.get("cloud_provider", "FILE/MCP")
                    if provider and isinstance(provider, str):
                        provider = provider.upper()
                    elif not provider:
                        tool_name = details.get("tool_to_use", "")
                        if tool_name.startswith("mcp_"):
                            provider = "MCP"
                        else:
                            provider = "FILE"
                    
                    description = details.get("description", "N/A")
                    dependencies = ", ".join(details.get("dependencies", [])) or "-"
                    tool = details.get("tool_to_use", "cli_command_generation")
                    
                    summary_table.add_row(step_id, provider, description, dependencies, tool)
                
                console.print(summary_table)
                console.print(f"\n[green]✓ Workflow loaded successfully: {len(step_details_map)} steps[/green]")
                console.print(f"[dim]Execution order: {' -> '.join(execution_order)}[/dim]")
            
            context.state_recorder.record_event(
                "workflow_loaded_from_sat",
                {
                    "sat_file_path": sat_file_path,
                    "dag_nodes": len(dag.vertices),
                    "dag_edges": len(dag.edges),
                    "execution_order": execution_order,
                    "original_query": original_query
                }
            )
            
            # Mark that this is a loaded workflow to use stored commands
            context.is_loaded_workflow = True
            
            print("Workflow loading completed successfully. Transitioning to EXECUTING.")
            return ExecutingState, context
            
        except FileNotFoundError as e:
            error_msg = f"Workflow file not found: {e}"
            print(f"Error: {error_msg}")
            context.current_errors.append({
                "method": "LOAD_WORKFLOW",
                "error": error_msg,
                "arguments": {"file_path": sat_file_path}
            })
            return FailedState, context
            
        except ValueError as e:
            error_msg = f"Invalid workflow file format: {e}"
            print(f"Error: {error_msg}")
            context.current_errors.append({
                "method": "LOAD_WORKFLOW",
                "error": error_msg,
                "arguments": {"file_path": sat_file_path}
            })
            return FailedState, context
            
        except Exception as e:
            error_msg = f"Unexpected error loading workflow: {e}"
            print(f"Error: {error_msg}")
            context.current_errors.append({
                "method": "LOAD_WORKFLOW",
                "error": error_msg,
                "arguments": {"file_path": sat_file_path}
            })
            return FailedState, context 