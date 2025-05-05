import asyncio
import traceback
from typing import Tuple, Type, List, Dict, Any

from .base_state import BaseState, StateMachineContext

# Import other state classes for transitions
from .processing_results_state import ProcessingResultsState
from .failed_state import FailedState

class ExecutingState(BaseState):
    """State responsible for executing selected tools using the GCP Executor."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: EXECUTING ---")
        
        tools_to_execute = context.selected_tools_for_execution
        if not tools_to_execute:
            print("No tools selected for execution. Transitioning to PROCESSING_RESULTS.")
            context.execution_results = [] # Ensure results list is empty
            return ProcessingResultsState, context

        print(f"Executing {len(tools_to_execute)} tool(s)...")
        execution_results: List[Tuple[str, bool, Any]] = []
        
        # --- Execution Logic --- 
        # Decide whether to run sequentially or concurrently
        # Concurrent execution using asyncio.gather:
        tasks = []
        for tool_call in tools_to_execute:
            tool_name = tool_call.get('name')
            tool_args = tool_call.get('arguments', {})
            if tool_name:
                print(f"  Queueing execution: {tool_name}")
                # Wrap the executor call in a separate async function to handle results/errors
                tasks.append(self._execute_single_tool(context, tool_name, tool_args))
            else:
                 print(f"  [Warning] Skipping tool call with missing name: {tool_call}")
                 # Add a placeholder result for the skipped call
                 execution_results.append(("unknown_tool", False, "Tool call skipped due to missing name"))

        if tasks:
            # Run tasks concurrently and gather results
            results = await asyncio.gather(*tasks, return_exceptions=True)
            execution_results.extend(results)
        # --- End Execution Logic --- 

        context.execution_results = execution_results
        print(f"Finished executing tools. Got {len(execution_results)} result(s). Transitioning to PROCESSING_RESULTS.")
        return ProcessingResultsState, context

    async def _execute_single_tool(self, context: StateMachineContext, tool_name: str, tool_args: Dict[str, Any]) -> Tuple[str, bool, Any]:
        """Helper coroutine to execute one tool and capture its result or error."""
        try:
            print(f"    Starting execution: {tool_name}")
            success, result = await context.gcp_executor.execute(tool_name, tool_args, context.knowledge_base)
            print(f"    Finished execution: {tool_name} (Success: {success})")
            return (tool_name, success, result)
        except Exception as exec_err:
            print(f"    [Error] Unexpected exception during {tool_name} execution: {exec_err}")
            traceback.print_exc()
            # Return failure tuple in case of unexpected errors in the execute call itself
            return (tool_name, False, f"Unexpected executor error: {exec_err}") 