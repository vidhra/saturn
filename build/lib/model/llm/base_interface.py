# model/llm/base_interface.py
import abc
from typing import List, Dict, Any, Optional, Tuple

class BaseLLMInterface(abc.ABC):
    """Abstract base class for LLM interaction interfaces."""

    def __init__(self, config: Dict[str, Any]):
        """Initialize with configuration containing API keys etc."""
        self.config = config
        self._validate_config()

    @abc.abstractmethod
    def _validate_config(self):
        """Validate that necessary configuration (like API keys) is present."""
        pass

    @abc.abstractmethod
    async def agenerate(self, messages: List[Dict[str, str]]) -> Any:
        """
        Generate a response from the LLM using the provided messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            
        Returns:
            The raw response from the LLM
        """
        pass

    @abc.abstractmethod
    async def get_tool_calls(
        self,
        query: str,
        system_prompt: str,
        tools: List[Dict[str, Any]],
        previous_errors: Optional[List[Dict[str, Any]]] = None
    ) -> Tuple[Optional[List[Dict[str, Any]]], Optional[str]]:
        """
        Sends the request to the LLM and processes the response to extract tool calls.

        Args:
            query: The user's natural language query.
            system_prompt: The system prompt guiding the LLM.
            tools: A list of tool definitions in the format expected by the specific LLM.
            previous_errors: Optional list of errors from previous attempts for feedback.

        Returns:
            A tuple containing:
            - A list of proposed tool calls (e.g., [{"name": "...", "arguments": {...}}]), or None if none proposed or error.
            - An optional string containing the LLM's text response if no tool calls were made, or None.
        """
        pass 