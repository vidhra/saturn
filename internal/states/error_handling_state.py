from typing import Tuple, Type
import json

from .base_state import BaseState, StateMachineContext

# Import other state classes for transitions
from .planning_state import PlanningState
from .failed_state import FailedState

class ErrorHandlingState(BaseState):
    """State responsible for deciding whether to retry planning after errors."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: ERROR_HANDLING ---")

        if not context.current_errors:
            print("No errors found, but entered ERROR_HANDLING state. This should not happen. Transitioning to PLANNING.")
            return PlanningState, context

        print(f"Handling {len(context.current_errors)} error(s) from last execution attempt:")
        try:
            print(json.dumps(context.current_errors, indent=2))
        except TypeError:
            print(context.current_errors) # Fallback

        # Check if max retries for planning/execution cycle have been reached
        if context.current_attempt >= context.max_retries:
            print(f"Max attempts ({context.max_retries}) reached. Transitioning to FAILED.")
            return FailedState, context
        else:
            print(f"Attempt {context.current_attempt}/{context.max_retries}. Transitioning back to PLANNING for correction.")
            # Keep context.current_errors - PlanningState will use them as feedback
            return PlanningState, context 