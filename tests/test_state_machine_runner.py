import pytest
from unittest.mock import Mock, AsyncMock, patch
from internal.state_machine_runner import StateMachineRunner
from internal.states.start_state import StartState
from internal.states.completed_state import CompletedState
from internal.states.failed_state import FailedState


class TestStateMachineRunner:
    """Test cases for StateMachineRunner class."""

    def test_runner_initialization(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test that runner initializes correctly with all components."""
        system_prompt = "Test system prompt"
        config = {"max_retries": 3, "custom_setting": "value"}
        
        runner = StateMachineRunner(
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt=system_prompt,
            config=config
        )
        
        assert runner.llm_interface == mock_llm_interface
        assert runner.gcp_executor == mock_gcp_executor
        assert runner.knowledge_base == mock_knowledge_base
        assert runner.system_prompt == system_prompt
        assert runner.config == config
        assert runner.max_retries == 3

    def test_runner_default_config(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test that runner uses default config when none provided."""
        runner = StateMachineRunner(
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt="Test prompt"
        )
        
        assert runner.config == {}
        assert runner.max_retries == 5  # Default value

    @pytest.mark.asyncio
    async def test_process_query_success_flow(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test successful query processing that reaches CompletedState."""
        runner = StateMachineRunner(
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt="Test prompt"
        )
        
        # Mock a simple flow: Start -> Completed
        with patch('internal.state_machine_runner.StartState') as mock_start_state:
            mock_start_instance = AsyncMock()
            mock_start_state.return_value = mock_start_instance
            mock_start_instance.run.return_value = (CompletedState, Mock())
            
            with patch('internal.state_machine_runner.CompletedState') as mock_completed_state:
                mock_completed_instance = AsyncMock()
                mock_completed_state.return_value = mock_completed_instance
                mock_completed_instance.run.return_value = (CompletedState, Mock())
                
                context = await runner.process_query("Test query")
                
                assert context is not None
                assert context.original_query == "Test query"
                mock_start_instance.run.assert_called_once()
                mock_completed_instance.run.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_query_failure_flow(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test query processing that reaches FailedState."""
        runner = StateMachineRunner(
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt="Test prompt"
        )
        
        # Mock a failure flow: Start -> Failed
        with patch('internal.state_machine_runner.StartState') as mock_start_state:
            mock_start_instance = AsyncMock()
            mock_start_state.return_value = mock_start_instance
            mock_start_instance.run.return_value = (FailedState, Mock())
            
            with patch('internal.state_machine_runner.FailedState') as mock_failed_state:
                mock_failed_instance = AsyncMock()
                mock_failed_state.return_value = mock_failed_instance
                mock_failed_instance.run.return_value = (FailedState, Mock())
                
                context = await runner.process_query("Test query")
                
                assert context is not None
                mock_start_instance.run.assert_called_once()
                mock_failed_instance.run.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_query_exception_handling(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test that unhandled exceptions are caught and transition to FailedState."""
        runner = StateMachineRunner(
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt="Test prompt"
        )
        
        # Mock StartState to raise an exception
        with patch('internal.state_machine_runner.StartState') as mock_start_state:
            mock_start_instance = AsyncMock()
            mock_start_state.return_value = mock_start_instance
            mock_start_instance.run.side_effect = Exception("Test exception")
            
            with patch('internal.state_machine_runner.FailedState') as mock_failed_state:
                mock_failed_instance = AsyncMock()
                mock_failed_state.return_value = mock_failed_instance
                mock_failed_instance.run.return_value = (FailedState, Mock())
                
                context = await runner.process_query("Test query")
                
                assert context is not None
                # Should have added error to context
                assert len(context.current_errors) > 0
                assert "Unhandled state execution error" in context.current_errors[0]["error"]
                mock_failed_instance.run.assert_called_once()

    @pytest.mark.asyncio
    async def test_context_initialization_in_process_query(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test that context is properly initialized in process_query."""
        runner = StateMachineRunner(
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt="Test prompt",
            config={"max_retries": 7}
        )
        
        # Mock to immediately complete
        with patch('internal.state_machine_runner.StartState') as mock_start_state:
            mock_start_instance = AsyncMock()
            mock_start_state.return_value = mock_start_instance
            
            def capture_context(context):
                # Capture the context to verify its initialization
                assert context.original_query == "Test initialization"
                assert context.llm_interface == mock_llm_interface
                assert context.gcp_executor == mock_gcp_executor
                assert context.knowledge_base == mock_knowledge_base
                assert context.system_prompt == "Test prompt"
                assert context.max_retries == 7
                return (CompletedState, context)
            
            mock_start_instance.run.side_effect = capture_context
            
            with patch('internal.state_machine_runner.CompletedState') as mock_completed_state:
                mock_completed_instance = AsyncMock()
                mock_completed_state.return_value = mock_completed_instance
                mock_completed_instance.run.return_value = (CompletedState, Mock())
                
                await runner.process_query("Test initialization")

    @pytest.mark.asyncio
    async def test_multiple_state_transitions(self, mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
        """Test multiple state transitions before reaching terminal state."""
        runner = StateMachineRunner(
            llm_interface=mock_llm_interface,
            gcp_executor=mock_gcp_executor,
            knowledge_base=mock_knowledge_base,
            system_prompt="Test prompt"
        )
        
        # Create a mock state that transitions through multiple states
        class MockState1:
            def __repr__(self):
                return "MockState1"
        
        class MockState2:
            def __repr__(self):
                return "MockState2"
        
        call_count = 0
        
        def mock_run_sequence(context):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                return (MockState2, context)
            elif call_count == 2:
                return (CompletedState, context)
            else:
                return (CompletedState, context)
        
        with patch('internal.state_machine_runner.StartState') as mock_start_state:
            mock_start_instance = AsyncMock()
            mock_start_state.return_value = mock_start_instance
            mock_start_instance.run.side_effect = mock_run_sequence
            
            with patch.object(runner, 'MockState2', MockState2):
                mock_state2_instance = AsyncMock()
                MockState2.return_value = mock_state2_instance
                mock_state2_instance.run.side_effect = mock_run_sequence
                
                with patch('internal.state_machine_runner.CompletedState') as mock_completed_state:
                    mock_completed_instance = AsyncMock()
                    mock_completed_state.return_value = mock_completed_instance
                    mock_completed_instance.run.return_value = (CompletedState, Mock())
                    
                    # This test is simplified - in real implementation, would need more complex mocking
                    # for dynamic state instantiation
                    context = await runner.process_query("Multi-transition test")
                    assert context is not None 