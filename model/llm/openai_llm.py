# model/llm/openai_llm.py
import json
import traceback
from openai import AsyncOpenAI # Use AsyncOpenAI
from typing import List, Dict, Any, Optional, Tuple

# Import the base class from the same directory
from .base_interface import BaseLLMInterface

# Keep helper functions local or move to a utils file if shared
def create_openai_error_feedback_prompt(query: str, system_prompt: str, errors: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    """Builds messages incorporating previous errors for OpenAI correction."""
    messages = [
        {"role": "system", "content": system_prompt} # Start with the base system prompt
    ]
    error_description = "Original Query: \n{}\n\nThe previous attempt resulted in the following errors:\n".format(query)
    for error_info in errors:
        error_description += f"- Function: {error_info['method']}\n"
        # Attempt to pretty-print arguments if they are dicts
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
        self.model = self.config.get('openai_model', 'gpt-4o') # Default to gpt-4o
        print(f"OpenAI Interface configured for model: {self.model}")
        try:
            self.client = AsyncOpenAI(api_key=self.api_key)
        except Exception as e:
            raise RuntimeError(f"Error initializing AsyncOpenAI client: {e}")

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
            # Pass the base system_prompt to the helper
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
                tools=tools if tools else None, # Pass tools only if they exist
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
                            # Arguments are expected to be JSON strings
                            args_dict = json.loads(tool_call_obj.function.arguments)
                            tool_calls_list.append({
                                "name": tool_call_obj.function.name,
                                "arguments": args_dict
                            })
                        except json.JSONDecodeError as json_err:
                            print(f"  [Error] Invalid JSON arguments from LLM: {json_err}")
                            # How to handle this error? Return it? For now, maybe just skip the call.
                            # Or potentially add it to a list of processing errors?
                            # We might need a different return type to signal this kind of issue.
                            pass # Skipping this invalid tool call for now
                    else:
                        print(f"  [Warning] Received non-function tool call type: {tool_call_obj.type}")
            else:
                print("OpenAI did not propose any tool calls.")
                if message.content:
                    print(f"OpenAI Response Content: {message.content}")
                    llm_text_response = message.content

            # Return None for tool calls list if it's empty
            return tool_calls_list if tool_calls_list else None, llm_text_response

        except Exception as e:
            print(f"--- Error during OpenAI API call --- ")
            print(f"Error: {e}")
            traceback.print_exc()
            # Return None, None to indicate failure
            return None, None 