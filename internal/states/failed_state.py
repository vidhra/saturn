import json
from typing import Tuple, Type
from .base_state import BaseState, StateMachineContext

class FailedState(BaseState):
    """Final state indicating the process failed."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: FAILED ---")
        print(f"Process failed after {context.current_attempt} attempts.")
        if context.current_errors:
            print("Last recorded errors:")
            try:
                print(json.dumps(context.current_errors, indent=2))
            except TypeError:
                 print(context.current_errors)
        else:
            print("No specific errors were recorded, but process terminated in FAILED state.")
        
        return FailedState, context 