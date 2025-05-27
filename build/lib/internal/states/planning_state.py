import traceback
from typing import Tuple, Type, List, Dict, Any
from .base_state import BaseState, StateMachineContext

class PlanningState(BaseState):
    """State responsible for interacting with the LLM to get tool calls."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print(f"--- State: PLANNING (Attempt {context.current_attempt + 1}/{context.max_retries}) ---")
        context.increment_attempt()

        # Move imports here to avoid circular import
        from .tool_selection_state import ToolSelectionState
        from .failed_state import FailedState
        from .completed_state import CompletedState

        if context.current_attempt > context.max_retries:
            print("Max attempts reached. Transitioning to FAILED.")
            return FailedState, context

        # Reset attempt-specific fields
        context.reset_for_new_attempt()

        try:
            # --- Get Available Tools (Potentially filtered based on DAG/query) ---
            # This might involve more complex logic in the future based on context.dag_definition
            print("Fetching available tools from Knowledge Base...")
            available_tools = context.knowledge_base.get_formatted_tools(context.original_query)
            if not available_tools:
                 print("Warning: No tools found/formatted by Knowledge Base.")
                 available_tools = [] # Ensure it's a list
            else:
                 tool_names = [t.get('function', {}).get('name', 'UnknownTool') for t in available_tools]
                 print(f"Using tools: {tool_names}")

            # --- Call LLM --- 
            # Pass current_errors from the *previous* failed attempt as feedback
            print("Calling LLM for tool proposals...")
            proposed_calls, llm_response = await context.llm_interface.get_tool_calls(
                query=context.original_query, # Or a refined query based on DAG state
                system_prompt=context.system_prompt,
                tools=available_tools,
                previous_errors=context.current_errors # Provide feedback from last attempt
            )

            context.proposed_tool_calls = proposed_calls
            context.llm_text_response = llm_response
            # Clear errors for the *next* attempt; executor/processing will populate if needed
            # We keep the errors from the *previous* attempt in context.current_errors until reset_for_new_attempt
            # Let's move the clearing step to after a successful cycle or before starting a new one.
            # context.current_errors = [] # Removing this line here

            if context.proposed_tool_calls:
                print(f"LLM proposed {len(context.proposed_tool_calls)} tool calls.")
                # TODO: Add logic to handle text responses that contain JSON tool calls (as done in orchestrator before)
                # This might involve calling json_repair here or passing raw text to ToolSelectionState
                print("Transitioning to TOOL_SELECTION")
                context.current_errors = [] # Clear previous errors before selecting/executing
                return ToolSelectionState, context
            elif context.llm_text_response:
                # Handle case where LLM provides text response instead of tools
                print(f"LLM provided text response: {context.llm_text_response!r}")
                # Option 1: Try to parse text response for tools (like in previous orchestrator)
                # This logic should ideally live in ToolSelectionState now.
                # For now, let's transition to ToolSelection to handle potential JSON in text.
                print("LLM provided text, transitioning to TOOL_SELECTION to check for embedded JSON.")
                context.current_errors = [] # Clear previous errors before potentially selecting/executing
                return ToolSelectionState, context
            else:
                # LLM call failed or returned nothing
                print("LLM call failed or returned no usable response. Adding error.")
                # Store the failure as an error for this attempt
                current_attempt_errors = [{
                    "method": "N/A",
                    "error": "LLM call failed or returned empty response.",
                    "arguments": {}
                }]
                context.current_errors = current_attempt_errors # Assign errors for this attempt

                # Decide whether to retry or fail immediately based on overall attempts
                if context.current_attempt < context.max_retries:
                    print("Retrying PLANNING due to LLM failure.")
                    # Keep errors and retry planning immediately
                    # No need to transition to ErrorHandlingState if we retry Planning directly
                    return PlanningState, context
                else:
                    print("Max attempts reached after LLM failure. Transitioning to FAILED.")
                    return FailedState, context

        except Exception as e:
            print(f"--- Unexpected Error during PLANNING state --- ")
            print(f"Error: {e}")
            traceback.print_exc()
            context.current_errors = [{
                "method": "PLANNING_STATE",
                "error": f"Overall planning exception: {e}",
                "arguments": {}
            }]
            print("Transitioning to FAILED due to unexpected error.")
            return FailedState, context 