# model/llm/claude_llm.py
import json
import traceback
from anthropic import AsyncAnthropic # Import Claude library
from typing import List, Dict, Any, Optional, Tuple

from .base_interface import BaseLLMInterface

def convert_to_claude_tools(openai_tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert OpenAI tool format to Claude tool format."""
    if not openai_tools:
        return []
    
    claude_tools = []
    for tool in openai_tools:
        func = tool.get("function")
        if not func:
            continue
        
        claude_tool = {
            "name": func.get("name"),
            "description": func.get("description", ""),
            "input_schema": func.get("parameters", {})
        }
        claude_tools.append(claude_tool)
    
    return claude_tools

def create_claude_messages(query: str, system_prompt: str, previous_errors: Optional[List[Dict[str, Any]]]) -> Tuple[str, List[Dict[str, str]]]:
    """Create Claude message format with separate system prompt."""
    messages = []
    
    if previous_errors:
        # Represent error feedback
        error_text = "The previous attempt failed. Please analyze the errors and correct the tool calls.\n"
        for err in previous_errors:
            err_args = json.dumps(err.get('arguments', {}))
            error_text += f"- Failed Call: {err.get('method')} with args {err_args}. Error: {err.get('error')}\n"
        error_text += f"\nOriginal query: {query}"
        messages.append({"role": "user", "content": error_text})
    else:
        messages.append({"role": "user", "content": query})
    
    return system_prompt, messages

class ClaudeLLM(BaseLLMInterface):
    """LLM interface implementation for Anthropic Claude models."""

    def _validate_config(self):
        if not self.config.get('anthropic_api_key'):
            raise ValueError("Anthropic API key ('anthropic_api_key') missing in configuration.")
        self.api_key = self.config['anthropic_api_key']
        self.model_name = self.config.get('claude_model', 'claude-3-5-sonnet-20241022')
        print(f"Claude Interface configured for model: {self.model_name}")
        
        # Initialize Claude client
        try:
            self.client = AsyncAnthropic(api_key=self.api_key)
            print(f"Claude client initialized for {self.model_name}.")
        except ImportError:
            raise RuntimeError("anthropic library not installed. Please install it: pip install anthropic")
        except Exception as e:
            raise RuntimeError(f"Error initializing Anthropic client: {e}")

    async def agenerate(self, messages: List[Dict[str, str]]) -> Any:
        """
        Generate a response from Claude using the provided messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            
        Returns:
            The raw response from Claude
        """
        try:
            # Claude expects system message to be separate
            system_content = ""
            claude_messages = []
            
            for msg in messages:
                if msg["role"] == "system":
                    system_content = msg["content"]
                else:
                    claude_messages.append(msg)
            
            response = await self.client.messages.create(
                model=self.model_name,
                max_tokens=4000,
                system=system_content if system_content else None,
                messages=claude_messages
            )
            
            # Convert Claude response to OpenAI-like format for compatibility
            class ClaudeResponse:
                def __init__(self, claude_resp):
                    self.choices = [ClaudeChoice(claude_resp)]
            
            class ClaudeChoice:
                def __init__(self, claude_resp):
                    self.message = ClaudeMessage(claude_resp)
            
            class ClaudeMessage:
                def __init__(self, claude_resp):
                    # Claude returns content as a list of content blocks
                    if claude_resp.content and len(claude_resp.content) > 0:
                        self.content = claude_resp.content[0].text
                    else:
                        self.content = ""
            
            return ClaudeResponse(response)
            
        except Exception as e:
            print(f"Error during Claude API call: {e}")
            raise

    async def get_tool_calls(
        self,
        query: str,
        system_prompt: str,
        tools: List[Dict[str, Any]],
        previous_errors: Optional[List[Dict[str, Any]]] = None
    ) -> Tuple[Optional[List[Dict[str, Any]]], Optional[str]]:
        """Calls Claude API to get tool calls."""
        
        claude_tools = convert_to_claude_tools(tools)
        system_content, claude_messages = create_claude_messages(query, system_prompt, previous_errors)
        print(f"Calling Claude API (Model: {self.model_name})...")
        
        try:
            response = await self.client.messages.create(
                model=self.model_name,
                max_tokens=4000,
                system=system_content if system_content else None,
                messages=claude_messages,
                tools=claude_tools if claude_tools else None
            )
            
            print("Received response from Claude.")
            
            tool_calls_list = []
            llm_text_response = None
            
            if response.content:
                for content_block in response.content:
                    if content_block.type == "tool_use":
                        print(f"  Claude proposed call: {content_block.name}")
                        print(f"    Arguments: {content_block.input}")
                        tool_calls_list.append({
                            "name": content_block.name,
                            "arguments": content_block.input
                        })
                    elif content_block.type == "text":
                        llm_text_response = content_block.text
                        print(f"Claude Response Text: {llm_text_response}")
            
            if not tool_calls_list and not llm_text_response:
                print("Warning: Claude response did not contain tool calls or text.")
                llm_text_response = "No response content from Claude."
            
            return tool_calls_list if tool_calls_list else None, llm_text_response
            
        except ImportError:
            print("Error: anthropic library not installed.")
            return None, "Error: Claude library not installed."
        except Exception as e:
            print(f"--- Error during Claude API call --- ")
            print(f"Error: {e}")
            traceback.print_exc()
            return None, None 