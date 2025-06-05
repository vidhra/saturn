# model/llm/base_interface.py
import abc
from typing import Any, Dict, List


class BaseLLMInterface(abc.ABC):
    """Abstract base class for LLM interaction interfaces."""

    def __init__(self, config: Dict[str, Any]):
        """Initialize with configuration containing API keys etc."""
        self.config = config
        self._validate_config()

    @abc.abstractmethod
    def _validate_config(self):
        """Validate the configuration."""
        pass

    @abc.abstractmethod
    async def agenerate(self, messages: List[Dict[str, str]]) -> Any:
        """Generate a response from the LLM."""
        pass


def get_llm_interface(config: Dict[str, Any]) -> BaseLLMInterface:
    """
    Factory function to return the appropriate LLM interface based on the provider in config.
    Imports are local to avoid circular dependencies.
    """
    provider = config.get("llm_provider", "openai").lower()
    if provider == "openai":
        from .openai_llm import OpenAILLM

        return OpenAILLM(config)
    elif provider == "gemini":
        from .gemini_llm import GeminiLLM

        return GeminiLLM(config)
    elif provider == "claude":
        from .claude_llm import ClaudeLLM

        return ClaudeLLM(config)
    elif provider == "mistral":
        from .mistral_llm import MistralLLM

        return MistralLLM(config)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
