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

            if not context.current_errors:
                print("No tools executed and no prior errors. Assuming completion.")
                return CompletedState, context
            else:
                print("No tools executed, but prior errors existed. Assuming failure to correct.")
                # Keep existing context.current_errors
                from .failed_state import FailedState
                return FailedState, context

        print(f"Processing {len(execution_results)} execution result(s)...")
        for result_tuple in execution_results:
           
            if isinstance(result_tuple, Exception):
                print(f"  [Error] Encountered exception from execution task: {result_tuple}")
               
                tool_name = "unknown_tool (task exception)"
                error_details = str(result_tuple)
                current_errors.append({
                    "method": tool_name,
                    "error": error_details,
                    "arguments": {} 
                })
                has_errors = True
               
                continue

            tool_name, success, result = result_tuple
            print(f"  Processing result for: {tool_name} (Success: {success})")
            
            if success:
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
                    "error": str(result), 
                    "arguments": args_used
                })

        context.current_errors = current_errors

        if has_errors:
            print(f"Encountered {len(current_errors)} error(s) during execution. Transitioning to ERROR_HANDLING.")
            return ErrorHandlingState, context
        else:
            print("All executed tools successful.")

            all_done = True 

            if all_done:
                print("All tasks appear completed. Transitioning to COMPLETED.")
                return CompletedState, context
            else:
                print("Tasks remain in DAG. Transitioning back to PLANNING.")
                context.current_errors = [] 
                from .planning_state import PlanningState
                return PlanningState, context 