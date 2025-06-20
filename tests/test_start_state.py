import pytest
pytestmark = pytest.mark.asyncio

from internal.states.planning_state import PlanningState
from internal.states.start_state import StartState


class TestStartState:
    """Test cases for StartState class."""

    @pytest.mark.asyncio
    async def test_start_state_run(self, sample_context):
        """Test that StartState properly initializes context and transitions to PlanningState."""
        # Modify context to have some existing state
        sample_context.current_attempt = 5
        sample_context.node_states = {"existing": "state"}
        sample_context.node_outputs = {"existing": "output"}
        sample_context.current_errors = [{"existing": "error"}]

        state = StartState()
        next_state_class, returned_context = await state.run(sample_context)

        # Check state transition
        assert next_state_class == PlanningState
        assert returned_context == sample_context

        # Check context reset
        assert returned_context.current_attempt == 0
        assert returned_context.node_states == {}
        assert returned_context.node_outputs == {}
        assert returned_context.current_errors == []

    @pytest.mark.asyncio
    async def test_start_state_preserves_core_context(self, sample_context):
        """Test that StartState preserves core context properties."""
        original_query = sample_context.original_query
        original_llm = sample_context.llm_interface
        original_executor = sample_context.gcp_executor
        original_kb = sample_context.knowledge_base
        original_prompt = sample_context.system_prompt
        original_retries = sample_context.max_retries

        state = StartState()
        next_state_class, returned_context = await state.run(sample_context)

        # Verify core properties are preserved
        assert returned_context.original_query == original_query
        assert returned_context.llm_interface == original_llm
        assert returned_context.gcp_executor == original_executor
        assert returned_context.knowledge_base == original_kb
        assert returned_context.system_prompt == original_prompt
        assert returned_context.max_retries == original_retries

    def test_start_state_repr(self):
        """Test StartState string representation."""
        state = StartState()
        assert repr(state) == "StartState"

    @pytest.mark.asyncio
    async def test_start_state_always_transitions_to_planning(self, sample_context):
        """Test that StartState always transitions to PlanningState regardless of context state."""
        contexts_to_test = [
            sample_context,
        ]

        context_with_errors = sample_context
        context_with_errors.current_errors = [{"error": "test"}]
        contexts_to_test.append(context_with_errors)

        context_with_outputs = sample_context
        context_with_outputs.node_outputs = {"node1": "result"}
        contexts_to_test.append(context_with_outputs)

        for context in contexts_to_test:
            state = StartState()
            next_state_class, _ = await state.run(context)
            assert next_state_class == PlanningState

    @pytest.mark.asyncio
    async def test_start_state_idempotent(self, sample_context):
        """Test that running StartState multiple times produces consistent results."""
        state = StartState()

        next_state1, context1 = await state.run(sample_context)
        next_state2, context2 = await state.run(sample_context)

        assert next_state1 == next_state2 == PlanningState
        assert context1.current_attempt == context2.current_attempt == 0
        assert context1.node_states == context2.node_states == {}
        assert context1.node_outputs == context2.node_outputs == {}
        assert context1.current_errors == context2.current_errors == []
