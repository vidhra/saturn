import json
import json_repair
from typing import Tuple, Type, List, Dict, Any
from pydantic import ValidationError

from .base_state import BaseState, StateMachineContext

# Import other state classes for transitions
from .executing_state import ExecutingState
from .completed_state import CompletedState
from .failed_state import FailedState

# Assuming Pydantic models are defined elsewhere (e.g., in orchestrator.py or a models file)
# You might need to import ToolCall, ToolCalls from your models definition
# from saturn.orchestrator import ToolCall, ToolCalls # Example import

class ToolSelectionState(BaseState):
    """State responsible for validating and selecting tools for execution."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: TOOL_SELECTION ---")

        proposed_tool_calls = context.proposed_tool_calls
        llm_text_response = context.llm_text_response
        extracted_calls = []

        # 1. Extract Tool Calls (from direct proposal or text response)
        if proposed_tool_calls:
            print(f"Using {len(proposed_tool_calls)} directly proposed tool calls.")
            extracted_calls = proposed_tool_calls
        elif llm_text_response:
            print("No direct tool calls, attempting to parse from text response...")
            try:
                # Clean and repair JSON from text (similar to previous orchestrator logic)
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
                        # Adapt structure: look for 'name'/'function' and 'arguments'/'parameters'
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
            except (json.JSONDecodeError, Exception) as e: # Broader exception for json_repair
                 print(f"Could not parse tool calls from text response: {e}")
                 # Fall through - extracted_calls remains empty

        # 2. Validate and Select Tools
        context.selected_tools_for_execution = []
        if extracted_calls:
            print(f"Validating {len(extracted_calls)} extracted tool call(s)...")
            try:
                # Basic Pydantic validation (assuming ToolCalls model exists)
                # tools_data = {"tool_calls": extracted_calls}
                # validated_tools = ToolCalls.model_validate(tools_data) # Uncomment if using Pydantic
                # print("Tool calls validated structurally.")

                # --- DAG/Dependency Logic Placeholder --- 
                # Here, you would implement logic to check dependencies based on
                # context.dag_definition and context.node_states.
                # For now, assume all proposed tools are ready.
                # Example: ready_tools = self._filter_ready_tools(validated_tools.tool_calls, context)
                
                # Using extracted_calls directly for now, assuming structure matches Pydantic/executor needs
                ready_tools = extracted_calls # Replace with actual filtering logic
                
                context.selected_tools_for_execution = ready_tools
                print(f"Selected {len(ready_tools)} tools for execution.")

            except ValidationError as val_err:
                 print(f"Tool validation failed: {val_err}")
                 # Treat validation error as a failure for this attempt
                 context.current_errors.append({
                    "method": "TOOL_SELECTION",
                    "error": f"Tool validation failed: {val_err}",
                    "arguments": extracted_calls
                })
                 # Decide how to handle validation errors - fail or maybe replan?
                 # For now, transition to Failed state if validation fails.
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
             # If Planning had errors, this means LLM didn't fix them
             # If Planning had no errors, this means the query didn't need tools or LLM thinks it's done
             # We need context to differentiate. Let ProcessingResults handle the final decision.
             # Transitioning to ProcessingResults with empty execution list.
             print("Transitioning to PROCESSING_RESULTS to determine final outcome.")
             # Make sure execution_results is empty
             context.execution_results = [] 
             from .processing_results_state import ProcessingResultsState # Import here to avoid circularity if needed
             return ProcessingResultsState, context

        # 3. Decide Next State
        if context.selected_tools_for_execution:
            print("Transitioning to EXECUTING")
            return ExecutingState, context
        else:
            print("No tools were selected for execution after validation/filtering.")
            # Similar to the case where no tools were extracted - let ProcessingResults decide.
            print("Transitioning to PROCESSING_RESULTS to determine final outcome.")
            context.execution_results = []
            from .processing_results_state import ProcessingResultsState # Import here to avoid circularity if needed
            return ProcessingResultsState, context

    # Placeholder for future DAG/dependency checking logic
    # def _filter_ready_tools(self, proposed_tools: List[Dict[str, Any]], context: StateMachineContext) -> List[Dict[str, Any]]:
    #    # Implement logic to check context.dag_definition and context.node_states
    #    # Return only the tools whose dependencies are met (nodes are 'COMPLETED')
    #    return proposed_tools # Placeholder 