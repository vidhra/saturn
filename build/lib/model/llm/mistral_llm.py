# model/llm/mistral_llm.py
import json
import traceback
from mistralai import Mistral # Updated import for new client
from typing import List, Dict, Any, Optional, Tuple

from .base_interface import BaseLLMInterface

# Helper to convert OpenAI tool format to Mistral tool format
# (New Mistral client uses a different tool format)
def convert_to_mistral_tools(openai_tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not openai_tools:
        return []
    
    mistral_tools = []
    for tool in openai_tools:
        func = tool.get("function")
        if not func:
            continue
        
        # New Mistral client uses this format for tools
        mistral_tool = {
            "type": "function",
            "function": {
                "name": func.get("name"),
                "description": func.get("description", ""),
                "parameters": func.get("parameters", {})
            }
        }
        mistral_tools.append(mistral_tool)
    
    return mistral_tools

# Helper to create Mistral message history
def create_mistral_messages(query: str, system_prompt: str, previous_errors: Optional[List[Dict[str, Any]]]) -> List[Dict[str, str]]:
    messages = []
    # New Mistral client handles system prompts properly
    if system_prompt:
         messages.append({"role": "system", "content": system_prompt})
         
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
        
    return messages

class MistralLLM(BaseLLMInterface):
    """LLM interface implementation for Mistral AI models using the new v1.x client."""

    def _validate_config(self):
        if not self.config.get('mistral_api_key'):
            raise ValueError("Mistral API key ('mistral_api_key') missing in configuration.")
        self.api_key = self.config['mistral_api_key']
        self.model_name = self.config.get('mistral_model', 'mistral-large-latest')
        print(f"Mistral Interface configured for model: {self.model_name}")
        # Initialize new Mistral client
        try:
            self.client = Mistral(api_key=self.api_key)
            print(f"Mistral client initialized for {self.model_name}.")
        except ImportError:
             raise RuntimeError("mistralai library not installed. Please install it: pip install mistralai>=1.0.0")
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
            # Use the new client's chat.complete method
            response = await self.client.chat.complete_async(
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
        """Calls Mistral API to get tool calls using the new v1.x client."""
        
        mistral_tools = convert_to_mistral_tools(tools)
        messages = create_mistral_messages(query, system_prompt, previous_errors)
        print(f"Calling Mistral API (Model: {self.model_name})...")
        
        try:
            # Use the new client API with proper async method
            response = await self.client.chat.complete_async(
                model=self.model_name,
                messages=messages,
                tools=mistral_tools if mistral_tools else None
            )
            
            print("Received response from Mistral.")
            message = response.choices[0].message

            tool_calls_list = []
            llm_text_response = None

            if hasattr(message, 'tool_calls') and message.tool_calls:
                print(f"Mistral proposed {len(message.tool_calls)} tool call(s):")
                for tool_call_obj in message.tool_calls:
                     # New Mistral client tool call format
                    if hasattr(tool_call_obj, 'function'):
                         print(f"  - Name: {tool_call_obj.function.name}")
                         print(f"    Arguments: {tool_call_obj.function.arguments}")
                         try:
                            # Arguments might be already parsed or JSON strings
                            if isinstance(tool_call_obj.function.arguments, str):
                                args_dict = json.loads(tool_call_obj.function.arguments)
                            else:
                                args_dict = tool_call_obj.function.arguments
                            
                            tool_calls_list.append({
                                "name": tool_call_obj.function.name,
                                "arguments": args_dict
                            })
                         except json.JSONDecodeError as json_err:
                            print(f"  [Error] Invalid JSON arguments from LLM: {json_err}")
                            pass # Skipping invalid call
                    else:
                        print(f"  [Warning] Received unexpected tool call format: {tool_call_obj}")
            else:
                 print("Mistral did not propose any tool calls.")
                 if hasattr(message, 'content') and message.content:
                    print(f"Mistral Response Content: {message.content}")
                    llm_text_response = message.content
            
            return tool_calls_list if tool_calls_list else None, llm_text_response

        except ImportError:
             print("Error: mistralai library not installed or wrong version.")
             return None, "Error: Mistral library not installed or needs update to v1.x."
        except Exception as e:
            print(f"--- Error during Mistral API call --- ")
            print(f"Error: {e}")
            traceback.print_exc()
            return None, None

        # Placeholder implementation removed
        # ... 