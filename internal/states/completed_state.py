import json
from typing import Tuple, Type
from .base_state import BaseState, StateMachineContext

class CompletedState(BaseState):
    """Final state indicating successful completion."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: COMPLETED ---")
        print("Process finished successfully.")
        # Log final outputs or state if needed
        if context.node_outputs:
            print("Final node outputs:")
            try:
                print(json.dumps(context.node_outputs, indent=2))
            except TypeError:
                print(context.node_outputs) # Fallback if not JSON serializable
        if context.llm_text_response:
             print(f"Final LLM text response: {context.llm_text_response}")

        # This is a terminal state, it doesn't transition further
        # In a real application, it might return a specific signal or result object
        return CompletedState, context # Return itself and context 