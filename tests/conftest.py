import pytest
import asyncio
from unittest.mock import Mock, AsyncMock
from typing import Dict, Any, List

# Import project modules
from internal.states.base_state import StateMachineContext


@pytest.fixture
def mock_llm_interface():
    """Mock LLM interface for testing."""
    mock = AsyncMock()
    mock.get_tool_calls.return_value = ([], "Mock response")
    return mock


@pytest.fixture
def mock_gcp_executor():
    """Mock GCP executor for testing."""
    mock = AsyncMock()
    mock.execute_tools.return_value = []
    return mock


@pytest.fixture
def mock_knowledge_base():
    """Mock knowledge base for testing."""
    mock = Mock()
    mock.get_formatted_tools.return_value = [
        {
            "type": "function",
            "function": {
                "name": "test_tool",
                "description": "A test tool",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param1": {"type": "string", "description": "Test parameter"}
                    }
                }
            }
        }
    ]
    return mock


@pytest.fixture
def sample_context(mock_llm_interface, mock_gcp_executor, mock_knowledge_base):
    """Create a sample StateMachineContext for testing."""
    return StateMachineContext(
        original_query="Test query",
        llm_interface=mock_llm_interface,
        gcp_executor=mock_gcp_executor,
        knowledge_base=mock_knowledge_base,
        system_prompt="Test system prompt",
        max_retries=3
    )


@pytest.fixture
def sample_tool_calls():
    """Sample tool calls for testing."""
    return [
        {
            "id": "call_1",
            "type": "function",
            "function": {
                "name": "test_tool",
                "arguments": '{"param1": "value1"}'
            }
        }
    ]


@pytest.fixture
def sample_execution_results():
    """Sample execution results for testing."""
    return [
        ("test_tool", True, {"result": "success"}),
        ("another_tool", False, {"error": "Tool failed"})
    ]


@pytest.fixture
def context_with_errors(sample_context):
    """Context with some errors for testing error handling."""
    sample_context.current_errors = [
        {
            "method": "test_method",
            "error": "Test error",
            "arguments": {"param": "value"}
        }
    ]
    return sample_context


@pytest.fixture
def context_with_dag(sample_context):
    """Context with DAG definition for testing."""
    sample_context.dag_definition = {
        "nodes": {
            "node1": {"tool": "test_tool", "dependencies": []},
            "node2": {"tool": "another_tool", "dependencies": ["node1"]}
        }
    }
    sample_context.node_states = {"node1": "PENDING", "node2": "PENDING"}
    return sample_context 