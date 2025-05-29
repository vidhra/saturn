# model/llm/openai_llm.py
import json
import traceback
from openai import AsyncOpenAI # Use AsyncOpenAI
from typing import List, Dict, Any, Optional, Tuple

from .base_interface import BaseLLMInterface

def create_openai_error_feedback_prompt(query: str, system_prompt: str, errors: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Builds messages incorporating previous errors for OpenAI correction."""
    messages = [
        {"role": "system", "content": system_prompt} 
    ]
    error_description = "Original Query: \n{}\n\nThe previous attempt resulted in the following errors:\n".format(query)
    for error_info in errors:
        error_description += f"- Function: {error_info['method']}\n"
        try:
             args_str = json.dumps(error_info.get('arguments', '{}'), indent=2)
        except Exception:
             args_str = str(error_info.get('arguments', '{}')) # Fallback to string representation
        error_description += f"  Arguments Used: {args_str}\n"
        error_description += f"  Error Received: {error_info['error']}\n"
    error_description += "\nPlease analyze the errors and provide corrected function calls in the required JSON format."
    messages.append({"role": "user", "content": error_description})
    return messages

class OpenAILLM(BaseLLMInterface):
    """LLM interface implementation for OpenAI models."""

    def _validate_config(self):
        if not self.config.get('openai_api_key'):
            raise ValueError("OpenAI API key ('openai_api_key') missing in configuration.")
        self.api_key = self.config['openai_api_key']
        self.model = self.config.get('openai_model', 'gpt-4.1') # Default to gpt-4o
        print(f"OpenAI Interface configured for model: {self.model}")
        try:
            self.client = AsyncOpenAI(api_key=self.api_key)
        except Exception as e:
            raise RuntimeError(f"Error initializing AsyncOpenAI client: {e}")

    async def agenerate(self, messages: List[Dict[str, str]]) -> Any:
        """
        Generate a response from the LLM using the provided messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            
        Returns:
            The raw response from the LLM
        """
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            return response
        except Exception as e:
            print(f"Error during OpenAI API call: {e}")
            raise

    async def get_tool_calls(
        self,
        query: str,
        system_prompt: str,
        tools: List[Dict[str, Any]],
        previous_errors: Optional[List[Dict[str, Any]]] = None
    ) -> Tuple[Optional[List[Dict[str, Any]]], Optional[str]]:
        """Calls OpenAI API to get tool calls."""
        messages = []
        if previous_errors:
            print("Preparing OpenAI error feedback prompt...")

            messages = create_openai_error_feedback_prompt(query, system_prompt, previous_errors)
        else:
            print("Preparing initial OpenAI prompt...")
            messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": query})

        print(f"Calling OpenAI API (Model: {self.model})...")
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools if tools else None, 
                tool_choice="auto" if tools else None
            )
            print("Received response from OpenAI.")
            message = response.choices[0].message

            tool_calls_list = []
            llm_text_response = None

            if message.tool_calls:
                print(f"OpenAI proposed {len(message.tool_calls)} tool call(s):")
                for tool_call_obj in message.tool_calls:
                    if tool_call_obj.type == 'function':
                        print(f"  - Name: {tool_call_obj.function.name}")
                        print(f"    Arguments: {tool_call_obj.function.arguments}")
                        try:
                            args_dict = json.loads(tool_call_obj.function.arguments)
                            tool_calls_list.append({
                                "name": tool_call_obj.function.name,
                                "arguments": args_dict
                            })
                        except json.JSONDecodeError as json_err:
                            print(f"  [Error] Invalid JSON arguments from LLM tool_call object: {json_err}")
                            pass 
                    else:
                        print(f"  [Warning] Received non-function tool call type: {tool_call_obj.type}")
            elif message.content:
                print("OpenAI did not propose tool calls directly. Checking message content for JSON...")
                try:
                    tool_calls = json.loads(message.content.strip())
                    if isinstance(tool_calls, dict) and isinstance(tool_calls.get('tool_calls'), list):
                        print("Found 'tool_calls' structure in message content. Processing...")
                        llm_text_response = None 
                        calls_in_content = tool_calls['tool_calls']
                        print(f"Found {len(calls_in_content)} potential tool call(s) in content:")
                        for call_data in calls_in_content:
                            if isinstance(call_data, dict) and 'name' in call_data and 'parameters' in call_data:
                                func_name = call_data['name']
                                args_dict = call_data['parameters'] 
                                print(f"  - Name: {func_name}")
                                print(f"    Arguments (from 'parameters'): {args_dict}")
                                tool_calls_list.append({
                                    "name": func_name,
                                    "arguments": args_dict 
                                })
                            else:
                                print(f"  [Warning] Skipping item in content's tool_calls list due to unexpected format: {call_data}")
                    else:
                      
                        print("Message content is JSON, but not the expected tool_calls structure.")
                        llm_text_response = message.content
                except json.JSONDecodeError:
                    print("Message content is not valid JSON. Treating as text response.")
                    llm_text_response = message.content
                except Exception as parse_err:
                    print(f"[Error] Failed to process message content for tool calls: {parse_err}")
                    llm_text_response = message.content 

            if not tool_calls_list and message.content and not llm_text_response:
                 print("Assigning original message content as text response.")
                 llm_text_response = message.content
            elif not tool_calls_list and not message.content:
                 print("OpenAI did not propose any tool calls and provided no text content.")

            return tool_calls_list if tool_calls_list else None, llm_text_response

        except Exception as e:
            print(f"--- Error during OpenAI API call --- ")
            print(f"Error: {e}")
            traceback.print_exc()
            return None, None 