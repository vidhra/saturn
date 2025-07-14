import json
from typing import Tuple, Type
from .base_state import BaseState, StateMachineContext

class CompletedState(BaseState):
    """Final state indicating successful completion."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: COMPLETED ---")
        
        # Save workflow as .sat file with captured commands if configured
        if getattr(context, 'save_workflow_after_execution', False) and not getattr(context, 'is_loaded_workflow', False):
            try:
                from internal.saturn_workflow import SaturnWorkflow
                workflow_handler = SaturnWorkflow()
                
                # Generate .sat file in workflows directory with captured commands
                workflows_dir = context.config.get("workflows_dir", "workflows")
                sat_filepath = workflow_handler.save_workflow(
                    dag=context.dag,
                    step_details_map=context.step_details_map,
                    execution_order=context.execution_order,
                    original_query=context.original_query,
                    output_dir=workflows_dir
                )
                
                if context.console:
                    context.console.print(f"[dim green]✓ Workflow saved with executed commands: {sat_filepath}[/dim green]")
                    context.console.print(f"[dim]Re-run with: saturn run {sat_filepath}[/dim]")
                
                # Store the sat file path in context for reference
                context.generated_sat_file = sat_filepath
                
            except Exception as e:
                if context.console:
                    context.console.print(f"[yellow]Warning: Failed to save workflow file: {e}[/yellow]")
        
        if context.node_outputs:
            print("Final node outputs:")
            try:
                print(json.dumps(context.node_outputs, indent=2))
            except TypeError:
                print(context.node_outputs)
        if context.llm_text_response:
             print(f"Final LLM text response: {context.llm_text_response}")

        return CompletedState, context 