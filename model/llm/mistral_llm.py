# model/llm/mistral_llm.py
import json
import traceback
from mistralai.async_client import MistralAsyncClient # Import Mistral library
# Remove the problematic ChatMessage import
# from mistralai.models.chat_completion import ChatMessage 
# from mistralai.models import ChatMessage
# from mistralai import ChatMessage
from typing import List, Dict, Any, Optional, Tuple

from .base_interface import BaseLLMInterface

# Helper to convert OpenAI tool format to Mistral tool format
# (Mistral uses OpenAI format, so minimal conversion needed)
def convert_to_mistral_tools(openai_tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Mistral generally accepts OpenAI format directly
    return openai_tools if openai_tools else []

# Helper to create Mistral message history as simple dicts
def create_mistral_messages(query: str, system_prompt: str, previous_errors: Optional[List[Dict[str, Any]]]) -> List[Dict[str, str]]:
    messages = []
    # Mistral can use a system prompt as the first message
    if system_prompt:
         messages.append({"role": "system", "content": system_prompt})
         
    if previous_errors:
        # Represent error feedback
        print("Warning: Mistral error feedback message construction not fully implemented. Sending simplified error description.")
        error_text = "The previous attempt failed. Please analyze the errors and correct the tool calls.\n"
        for err in previous_errors:
            err_args = json.dumps(err.get('arguments', {}))
            error_text += f"- Failed Call: {err.get('method')} with args {err_args}. Error: {err.get('error')}\n"
        error_text += f"\nOriginal query: {query}"
        messages.append({"role": "user", "content": error_text})
        # Need to reconstruct history properly if previous calls existed
    else:
        messages.append({"role": "user", "content": query})
        
    # TODO: Handle proper reconstruction of multi-turn history with tool calls/results if needed
    return messages

class MistralLLM(BaseLLMInterface):
    """LLM interface implementation for Mistral AI models."""

    def _validate_config(self):
        if not self.config.get('mistral_api_key'):
            raise ValueError("Mistral API key ('mistral_api_key') missing in configuration.")
        self.api_key = self.config['mistral_api_key']
        self.model_name = self.config.get('mistral_model', 'mistral-large-latest')
        print(f"Mistral Interface configured for model: {self.model_name}")
        # Initialize Mistral client
        try:
            self.client = MistralAsyncClient(api_key=self.api_key)
            print(f"Mistral client initialized for {self.model_name}.")
        except ImportError:
             raise RuntimeError("mistralai library not installed. Please install it: pip install mistralai")
        except Exception as e:
            raise RuntimeError(f"Error initializing Mistral client: {e}")

    async def agenerate(self, messages: List[Dict[str, str]]) -> Any:
        """
        Generate a response from Mistral using the provided messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            
        Returns:
            The raw response from Mistral
        """
        try:
            response = await self.client.chat(
                model=self.model_name,
                messages=messages
            )
            return response
        except Exception as e:
            print(f"Error during Mistral API call: {e}")
            raise

    async def get_tool_calls(
        self,
        query: str,
        system_prompt: str,
        tools: List[Dict[str, Any]],
        previous_errors: Optional[List[Dict[str, Any]]] = None
    ) -> Tuple[Optional[List[Dict[str, Any]]], Optional[str]]:
        """Calls Mistral API to get tool calls."""
        
        mistral_tools = convert_to_mistral_tools(tools)
        # Get messages as list of dicts
        messages: List[Dict[str, str]] = create_mistral_messages(query, system_prompt, previous_errors)
        print(f"Calling Mistral API (Model: {self.model_name})...")
        
        try:
            response = await self.client.chat(
                model=self.model_name,
                messages=messages, # Pass the list of dicts
                tools=mistral_tools if mistral_tools else None,
                tool_choice="auto" # Or "any" or specific tool
            )
            print("Received response from Mistral.")
            message = response.choices[0].message

            tool_calls_list = []
            llm_text_response = None

            if message.tool_calls:
                print(f"Mistral proposed {len(message.tool_calls)} tool call(s):")
                for tool_call_obj in message.tool_calls:
                     # Mistral tool call format is similar to OpenAI's
                    if tool_call_obj.type == 'function':
                         print(f"  - Name: {tool_call_obj.function.name}")
                         print(f"    Arguments: {tool_call_obj.function.arguments}")
                         try:
                            # Arguments should be JSON strings
                            args_dict = json.loads(tool_call_obj.function.arguments)
                            tool_calls_list.append({
                                "name": tool_call_obj.function.name,
                                "arguments": args_dict
                            })
                         except json.JSONDecodeError as json_err:
                            print(f"  [Error] Invalid JSON arguments from LLM: {json_err}")
                            pass # Skipping invalid call
                    else:
                        print(f"  [Warning] Received non-function tool call type: {tool_call_obj.type}")
            else:
                 print("Mistral did not propose any tool calls.")
                 if message.content:
                    print(f"Mistral Response Content: {message.content}")
                    llm_text_response = message.content
            
            return tool_calls_list if tool_calls_list else None, llm_text_response

        except ImportError:
             print("Error: mistralai library not installed.")
             return None, "Error: Mistral library not installed."
        except Exception as e:
            print(f"--- Error during Mistral API call --- ")
            print(f"Error: {e}")
            traceback.print_exc()
            return None, None

        # Placeholder implementation removed
        # ... 