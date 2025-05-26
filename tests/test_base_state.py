import pytest
from unittest.mock import Mock, AsyncMock
from internal.states.base_state import BaseState, StateMachineContext


class TestStateMachineContext:
    """Test cases for StateMachineContext class."""

    def test_context_initialization(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test that context initializes with correct default values."""
        context = StateMachineContext(
            original_query="test query",
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt="test prompt",
            max_retries=5
        )
        
        assert context.original_query == "test query"
        assert context.llm_interface == mock_llm_interface
        assert context.gcp_executor == mock_gcp_executor
        assert context.knowledge_base == mock_knowledge_base
        assert context.system_prompt == "test prompt"
        assert context.max_retries == 5
        
        # Check default values
        assert context.current_attempt == 0
        assert context.dag_definition is None
        assert context.node_states == {}
        assert context.node_outputs == {}
        assert context.current_errors == []
        assert context.proposed_tool_calls is None
        assert context.llm_text_response is None
        assert context.selected_tools_for_execution == []
        assert context.execution_results == []

    def test_context_default_max_retries(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test that context uses default max_retries when not specified."""
        context = StateMachineContext(
            original_query="test query",
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt="test prompt"
        )
        assert context.max_retries == 5

    def test_reset_for_new_attempt(self, sample_context):
        """Test that reset_for_new_attempt clears the correct fields."""
        # Set up some state
        sample_context.proposed_tool_calls = [{"test": "data"}]
        sample_context.llm_text_response = "test response"
        sample_context.selected_tools_for_execution = [{"tool": "test"}]
        sample_context.execution_results = [("tool", True, {})]
        sample_context.current_errors = [{"error": "test"}]
        sample_context.node_states = {"node1": "COMPLETED"}
        
        # Reset
        sample_context.reset_for_new_attempt()
        
        # Check cleared fields
        assert sample_context.proposed_tool_calls is None
        assert sample_context.llm_text_response is None
        assert sample_context.selected_tools_for_execution == []
        assert sample_context.execution_results == []
        
        # Check preserved fields
        assert sample_context.current_errors == [{"error": "test"}]  # Should be preserved
        assert sample_context.node_states == {"node1": "COMPLETED"}  # Should be preserved

    def test_increment_attempt(self, sample_context):
        """Test that increment_attempt correctly increments the counter."""
        initial_attempt = sample_context.current_attempt
        sample_context.increment_attempt()
        assert sample_context.current_attempt == initial_attempt + 1
        
        sample_context.increment_attempt()
        assert sample_context.current_attempt == initial_attempt + 2


class TestBaseState:
    """Test cases for BaseState abstract class."""

    def test_base_state_is_abstract(self):
        """Test that BaseState cannot be instantiated directly."""
        with pytest.raises(TypeError):
            BaseState()

    def test_base_state_repr(self):
        """Test the __repr__ method works for state subclasses."""
        class TestState(BaseState):
            async def run(self, context):
                return TestState, context
        
        state = TestState()
        assert repr(state) == "TestState"

    def test_base_state_run_is_abstract(self):
        """Test that run method must be implemented by subclasses."""
        class IncompleteState(BaseState):
            pass
        
        with pytest.raises(TypeError):
            IncompleteState()

    @pytest.mark.asyncio
    async def test_base_state_run_signature(self, sample_context):
        """Test that run method has correct signature in subclasses."""
        class TestState(BaseState):
            async def run(self, context):
                return TestState, context
        
        state = TestState()
        next_state, returned_context = await state.run(sample_context)
        
        assert next_state == TestState
        assert returned_context == sample_context 