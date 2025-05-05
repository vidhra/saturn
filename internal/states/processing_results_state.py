from typing import Tuple, Type, List, Dict, Any

from .base_state import BaseState, StateMachineContext

# Import other state classes for transitions
from .error_handling_state import ErrorHandlingState
from .completed_state import CompletedState

class ProcessingResultsState(BaseState):
    """State responsible for processing tool execution results and updating state."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: PROCESSING_RESULTS ---")

        execution_results = context.execution_results
        current_errors = []
        has_errors = False

        if not execution_results:
            print("No execution results to process.")
            # This happens if ToolSelection found no tools. Did the LLM intend to finish?
            # Check if the previous state was Planning and had errors
            # This logic might be simplified based on how ToolSelection transitions.
            # If we reach here without executing anything, and there were no prior errors expecting correction,
            # assume completion. Otherwise, assume failure.
            # Revisit this logic based on ToolSelection behavior.
            if not context.current_errors: # If no *prior* errors were being corrected
                print("No tools executed and no prior errors. Assuming completion.")
                return CompletedState, context
            else:
                print("No tools executed, but prior errors existed. Assuming failure to correct.")
                # Keep existing context.current_errors
                from .failed_state import FailedState
                return FailedState, context

        print(f"Processing {len(execution_results)} execution result(s)...")
        for result_tuple in execution_results:
            # Handle potential exceptions returned by asyncio.gather
            if isinstance(result_tuple, Exception):
                print(f"  [Error] Encountered exception from execution task: {result_tuple}")
                # Try to associate with a tool if possible, otherwise generic error
                tool_name = "unknown_tool (task exception)"
                error_details = str(result_tuple)
                current_errors.append({
                    "method": tool_name,
                    "error": error_details,
                    "arguments": {} # Arguments might be lost here
                })
                has_errors = True
                # Update node state if DAG is used
                # if tool_name in context.node_states: context.node_states[tool_name] = "FAILED"
                continue

            # Unpack normal results
            tool_name, success, result = result_tuple
            print(f"  Processing result for: {tool_name} (Success: {success})")

            # --- Update DAG state (Placeholder) ---
            # If using a DAG, update the node status
            # context.node_states[tool_name] = "COMPLETED" if success else "FAILED"
            
            if success:
                # Store successful output
                context.node_outputs[tool_name] = result 
            else:
                has_errors = True
                # Extract arguments used for this specific failed tool
                args_used = "unknown"
                for tool_call in context.selected_tools_for_execution:
                    if tool_call.get('name') == tool_name:
                        args_used = tool_call.get('arguments', {})
                        break
                
                current_errors.append({
                    "method": tool_name,
                    "error": str(result), # Convert result (error message) to string
                    "arguments": args_used
                })
        # --- End Processing Loop --- 

        # Update context with errors from this execution run
        context.current_errors = current_errors

        # 5. Decide Next State
        if has_errors:
            print(f"Encountered {len(current_errors)} error(s) during execution. Transitioning to ERROR_HANDLING.")
            return ErrorHandlingState, context
        else:
            print("All executed tools successful.")
            # --- Check for DAG Completion (Placeholder) ---
            # If using a DAG, check if all nodes are COMPLETED.
            # all_done = all(status == "COMPLETED" for status in context.node_states.values())
            all_done = True # Placeholder: Assume done if no errors in this batch

            if all_done:
                print("All tasks appear completed. Transitioning to COMPLETED.")
                return CompletedState, context
            else:
                # More steps remaining in the DAG
                print("Tasks remain in DAG. Transitioning back to PLANNING.")
                # Clear errors before replanning for next steps
                context.current_errors = [] 
                from .planning_state import PlanningState
                return PlanningState, context 