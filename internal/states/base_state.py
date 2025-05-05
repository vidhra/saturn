from abc import ABC, abstractmethod
from typing import Dict, Any, Type, Tuple, Optional, List

# Forward declaration for type hinting cycle
class StateMachineContext:
    pass

class BaseState(ABC):
    """Abstract base class for all states in the state machine."""

    @abstractmethod
    async def run(self, context: 'StateMachineContext') -> Tuple[Type['BaseState'], 'StateMachineContext']:
        """
        Executes the logic for this state.

        Args:
            context: The current state machine context containing all necessary data
                     (e.g., DAG, node states, LLM interface, executor).

        Returns:
            A tuple containing:
            - The class of the next state to transition to.
            - The updated state machine context.
        """
        pass

    def __repr__(self) -> str:
        return self.__class__.__name__

# Define the context structure here or in a separate file
# For now, defining it here for simplicity
class StateMachineContext:
    def __init__(self,
                 original_query: str,
                 llm_interface: Any, # Replace Any with actual LLM Interface type
                 gcp_executor: Any,  # Replace Any with actual GCP Executor type
                 knowledge_base: Any, # Replace Any with actual KB type
                 system_prompt: str,
                 max_retries: int = 5):
        self.original_query: str = original_query
        self.llm_interface: Any = llm_interface
        self.gcp_executor: Any = gcp_executor
        self.knowledge_base: Any = knowledge_base
        self.system_prompt: str = system_prompt
        self.max_retries: int = max_retries

        # State-dependent fields (initialized or updated by states)
        self.current_attempt: int = 0
        self.dag_definition: Optional[Dict[str, Any]] = None # Or a dedicated DAG class
        self.node_states: Dict[str, str] = {} # e.g., {'node1': 'PENDING', 'node2': 'READY'}
        self.node_outputs: Dict[str, Any] = {} # Store results of completed nodes
        self.current_errors: List[Dict[str, Any]] = [] # Errors from the last execution attempt
        self.proposed_tool_calls: Optional[List[Dict[str, Any]]] = None # From LLM
        self.llm_text_response: Optional[str] = None # From LLM
        self.selected_tools_for_execution: List[Dict[str, Any]] = [] # Tools ready to run
        self.execution_results: List[Tuple[str, bool, Any]] = [] # [(tool_name, success, result)]

    def reset_for_new_attempt(self):
        """Resets fields that should be cleared before a planning/execution cycle."""
        self.proposed_tool_calls = None
        self.llm_text_response = None
        self.selected_tools_for_execution = []
        self.execution_results = []
        # Keep current_errors from the *previous* attempt for feedback
        # Keep node_states and node_outputs as they represent progress

    def increment_attempt(self):
        self.current_attempt += 1 