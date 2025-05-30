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

class StateMachineContext:
    def __init__(self,
                 original_query: str,
                 llm_interface: Any,
                 gcp_executor: Any,
                 aws_executor: Any,
                 knowledge_base: Any,
                 system_prompt: str,
                 max_retries: int = 5,
                 console: Optional[Any] = None,
                 rag_engine: Optional[Any] = None,
                 state_recorder: Optional[Any] = None,
                 file_build_executor: Optional[Any] = None):
        self.original_query: str = original_query
        self.llm_interface: Any = llm_interface
        self.gcp_executor: Any = gcp_executor
        self.aws_executor: Any = aws_executor
        self.knowledge_base: Any = knowledge_base
        self.system_prompt: str = system_prompt
        self.max_retries: int = max_retries
        self.console: Optional[Any] = console
        self.rag_engine: Optional[Any] = rag_engine
        self.state_recorder: Optional[Any] = state_recorder
        self.file_build_executor: Optional[Any] = file_build_executor

        self.current_attempt: int = 0
        

        self.dag: Optional[Any] = None  # AcyclicGraph instance
        self.step_details_map: Dict[str, Any] = {}  # Step details from planning
        self.execution_order: List[str] = []  # Topological order of steps
        self.step_outputs: Dict[str, Any] = {}  # Results from completed steps
        self.file_tool_names: set = set()  # Set of file build tool names
        
        # Legacy state machine fields
        self.node_states: Dict[str, str] = {} 
        self.node_outputs: Dict[str, Any] = {} 
        self.current_errors: List[Dict[str, Any]] = []
        self.proposed_tool_calls: Optional[List[Dict[str, Any]]] = None
        self.llm_text_response: Optional[str] = None
        self.selected_tools_for_execution: List[Dict[str, Any]] = []
        self.execution_results: List[Tuple[str, bool, Any]] = []

    def reset_for_new_attempt(self):
        """Resets fields that should be cleared before a planning/execution cycle."""
        self.proposed_tool_calls = None
        self.llm_text_response = None
        self.selected_tools_for_execution = []
        self.execution_results = []

    def increment_attempt(self):
        self.current_attempt += 1 