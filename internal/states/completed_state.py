import json
from typing import Tuple, Type
from .base_state import BaseState, StateMachineContext

class CompletedState(BaseState):
    """Final state indicating successful completion."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: COMPLETED ---")
        print("Process finished successfully.")
        if context.node_outputs:
            print("Final node outputs:")
            try:
                print(json.dumps(context.node_outputs, indent=2))
            except TypeError:
                print(context.node_outputs)
        if context.llm_text_response:
             print(f"Final LLM text response: {context.llm_text_response}")

        return CompletedState, context 