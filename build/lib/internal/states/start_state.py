from typing import Tuple, Type
from .base_state import BaseState, StateMachineContext

class StartState(BaseState):
    """Initial state of the machine."""

    async def run(self, context: StateMachineContext) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: START ---")
        # Perform any initial setup if needed
        context.current_attempt = 0
        context.node_states = {} # Initialize node states if not already done
        context.node_outputs = {}
        context.current_errors = []
        print("Transitioning to PLANNING")
        from .planning_state import PlanningState  # moved import here
        # Always transition to Planning state first
        return PlanningState, context 