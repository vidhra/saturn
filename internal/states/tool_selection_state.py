import json
import json_repair
from typing import Tuple, Type, List, Dict, Any
from pydantic import ValidationError

from .base_state import BaseState, StateMachineContext
from .executing_state import ExecutingState
from .completed_state import CompletedState
from .failed_state import FailedState

class ToolSelectionState(BaseState):
    """State responsible for validating and selecting tools for execution."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: TOOL_SELECTION ---")

        proposed_tool_calls = context.proposed_tool_calls
        llm_text_response = context.llm_text_response
        extracted_calls = []

        if proposed_tool_calls:
            print(f"Using {len(proposed_tool_calls)} directly proposed tool calls.")
            extracted_calls = proposed_tool_calls
        elif llm_text_response:
            print("No direct tool calls, attempting to parse from text response...")
            try:
                cleaned_response = llm_text_response.strip()
                if cleaned_response.startswith('```json'):
                    cleaned_response = cleaned_response[7:]
                if cleaned_response.endswith('```'):
                    cleaned_response = cleaned_response[:-3]
                cleaned_response = cleaned_response.strip()

                if cleaned_response:
                    potential_calls = json_repair.loads(cleaned_response)
                    if isinstance(potential_calls, dict) and isinstance(potential_calls.get('tool_calls'), list):
                        print("Successfully parsed 'tool_calls' structure from text response.")
                        raw_calls = potential_calls['tool_calls']
                        for call_data in raw_calls:
                            func_name = None
                            args = None
                            if isinstance(call_data, dict):
                                func_name = call_data.get('name') or call_data.get('function')
                                args = call_data.get('arguments') or call_data.get('parameters')

                            if func_name and isinstance(args, dict):
                                extracted_calls.append({"name": func_name, "arguments": args})
                            else:
                                print(f"  [Warning] Skipping item in text due to unexpected format: {call_data}")
                    else:
                        print("Text response is JSON, but not the expected tool_calls structure.")
                else:
                     print("Cleaned text response is empty.")
            except (json.JSONDecodeError, Exception) as e:
                 print(f"Could not parse tool calls from text response: {e}")


        # 2. Validate and Select Tools
        context.selected_tools_for_execution = []
        if extracted_calls:
            print(f"Validating {len(extracted_calls)} extracted tool call(s)...")
            try:
                ready_tools = extracted_calls 
                context.selected_tools_for_execution = ready_tools
                print(f"Selected {len(ready_tools)} tools for execution.")

            except ValidationError as val_err:
                 print(f"Tool validation failed: {val_err}")
              
                 context.current_errors.append({
                    "method": "TOOL_SELECTION",
                    "error": f"Tool validation failed: {val_err}",
                    "arguments": extracted_calls
                })
                 print("Transitioning to FAILED due to validation error.")
                 return FailedState, context
            except Exception as e:
                print(f"Error during tool selection/validation: {e}")
                context.current_errors.append({
                    "method": "TOOL_SELECTION",
                    "error": f"Unexpected error during selection: {e}",
                    "arguments": extracted_calls
                })
                print("Transitioning to FAILED due to unexpected selection error.")
                return FailedState, context
        else:
             print("No valid tool calls proposed or extracted from text response.")
             print("Transitioning to PROCESSING_RESULTS to determine final outcome.")
             context.execution_results = [] 
             from .processing_results_state import ProcessingResultsState 

        # 3. Decide Next State
        if context.selected_tools_for_execution:
            print("Transitioning to EXECUTING")
            return ExecutingState, context
        else:
            print("No tools were selected for execution after validation/filtering.")
            print("Transitioning to PROCESSING_RESULTS to determine final outcome.")
            context.execution_results = []
            from .processing_results_state import ProcessingResultsState 
            return ProcessingResultsState, context
