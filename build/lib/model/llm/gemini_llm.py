# model/llm/gemini_llm.py
import json
import traceback
import asyncio # Might be needed for SDK interaction
import google.generativeai as genai # Import Gemini library
from google.generativeai.types import GenerationConfig, HarmCategory, FunctionDeclaration, Tool
from typing import List, Dict, Any, Optional, Tuple

from .base_interface import BaseLLMInterface

# Helper to convert OpenAI tool format to Gemini FunctionDeclaration
# (This is a basic example, might need more sophisticated mapping)
def convert_to_gemini_tools(openai_tools: List[Dict[str, Any]]) -> Optional[Tool]:
    if not openai_tools:
        return None
    function_declarations = []
    for tool in openai_tools:
        func = tool.get("function")
        if not func:
            continue
        # Basic mapping - assumes OpenAI schema is compatible enough
        # Gemini schema uses OpenAPI format directly
        function_declarations.append(
            FunctionDeclaration(
                name=func.get("name"),
                description=func.get("description", ""),
                parameters=func.get("parameters") # Assuming parameters is already in OpenAPI schema format
            )
        )
    if not function_declarations:
         return None
    return Tool(function_declarations=function_declarations)

# Helper to create Gemini message history
def create_gemini_history(query: str, system_prompt: str, previous_errors: Optional[List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    history = []
    # Note: Gemini handles system prompts differently (via system_instruction in GenerativeModel)
    # We might need to pass the system_prompt during model initialization instead.
    # For history, we primarily add user/model turns.
    
    if previous_errors:
        # Represent the error feedback as part of the history
        error_text = "The previous attempt failed with errors:\n"
        for err in previous_errors:
            err_args = json.dumps(err.get('arguments', {}))
            error_text += f"- Call: {err.get('method')}, Args: {err_args}, Error: {err.get('error')}\n"
        error_text += f"\nPlease analyze and correct. Original query was: {query}"
        # How to represent this? Maybe as a user turn asking for correction?
        history.append({'role': 'user', 'parts': [error_text]})
        # Need a preceding model turn that presumably made the failed call - difficult to reconstruct accurately.
        # This error feedback loop needs careful mapping to Gemini's chat history format.
        print("Warning: Gemini error feedback history construction is complex and needs refinement.")
    else:
        history.append({'role': 'user', 'parts': [query]})
        
    return history

class GeminiLLM(BaseLLMInterface):
    """LLM interface implementation for Google Gemini models."""

    def _validate_config(self):
        if not self.config.get('gemini_api_key'):
            raise ValueError("Gemini API key ('gemini_api_key') missing in configuration.")
        self.api_key = self.config['gemini_api_key']
        self.model_name = self.config.get('gemini_model', 'gemini-1.5-pro-latest')
        print(f"Gemini Interface configured for model: {self.model_name}")
        # Configure Gemini client
        try:
            genai.configure(api_key=self.api_key)
            # System prompt can be passed here
            system_instruction = self.config.get('gemini_system_prompt') # Allow specific system prompt override
            self.model = genai.GenerativeModel(
                self.model_name,
                system_instruction=system_instruction 
                # generation_config=generation_config, # Add if needed
                # safety_settings=safety_settings # Add if needed
            )
            print(f"Gemini client initialized for {self.model_name}.")
        except ImportError:
             raise RuntimeError("google.generativeai library not installed. Please install it: pip install google-generativeai")
        except Exception as e:
            raise RuntimeError(f"Error initializing Gemini client: {e}")

    async def agenerate(self, messages: List[Dict[str, str]]) -> Any:
        """
        Generate a response from Gemini using the provided messages.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            
        Returns:
            The raw response from Gemini
        """
        try:
            # Convert messages to Gemini format
            gemini_history = []
            system_instruction = None
            
            for msg in messages:
                if msg["role"] == "system":
                    system_instruction = msg["content"]
                elif msg["role"] == "user":
                    gemini_history.append({'role': 'user', 'parts': [msg["content"]]})
                elif msg["role"] == "assistant":
                    gemini_history.append({'role': 'model', 'parts': [msg["content"]]})
            
            # Create a new model instance with system instruction if provided
            model_to_use = self.model
            if system_instruction:
                model_to_use = genai.GenerativeModel(
                    self.model_name,
                    system_instruction=system_instruction
                )
            
            # Use asyncio.to_thread for synchronous Gemini API
            response = await asyncio.to_thread(
                model_to_use.generate_content,
                gemini_history
            )
            
            # Convert Gemini response to OpenAI-like format for compatibility
            class GeminiResponse:
                def __init__(self, gemini_resp):
                    self.choices = [GeminiChoice(gemini_resp)]
            
            class GeminiChoice:
                def __init__(self, gemini_resp):
                    self.message = GeminiMessage(gemini_resp)
            
            class GeminiMessage:
                def __init__(self, gemini_resp):
                    if gemini_resp.candidates and gemini_resp.candidates[0].content.parts:
                        # Get text from the first part
                        first_part = gemini_resp.candidates[0].content.parts[0]
                        if hasattr(first_part, 'text'):
                            self.content = first_part.text
                        else:
                            self.content = str(first_part)
                    else:
                        self.content = ""
            
            return GeminiResponse(response)
            
        except Exception as e:
            print(f"Error during Gemini API call: {e}")
            raise

    async def get_tool_calls(
        self,
        query: str,
        system_prompt: str,
        tools: List[Dict[str, Any]],
        previous_errors: Optional[List[Dict[str, Any]]] = None
    ) -> Tuple[Optional[List[Dict[str, Any]]], Optional[str]]:
        """Calls Gemini API to get tool calls."""
        
        gemini_tools = convert_to_gemini_tools(tools)
        history = create_gemini_history(query, system_prompt, previous_errors)
        print(f"Calling Gemini API (Model: {self.model_name})...")
        
        try:
            # Create model with system instruction if available
            model_to_use = self.model
            if system_prompt:
                model_to_use = genai.GenerativeModel(
                    self.model_name,
                    system_instruction=system_prompt
                )
            
            # Use asyncio.to_thread since Gemini API is synchronous
            response = await asyncio.to_thread(
                model_to_use.generate_content,
                history,
                tools=gemini_tools
            )

            print("Received response from Gemini.")
            
            # Parse response for FunctionCall parts
            tool_calls_list = []
            llm_text_response = None
            if response.candidates and response.candidates[0].content.parts:
                 for part in response.candidates[0].content.parts:
                    if hasattr(part, 'function_call') and part.function_call:
                        fc = part.function_call
                        print(f"  Gemini proposed call: {fc.name}")
                        # Args are already dicts in Gemini response
                        args_dict = dict(fc.args) 
                        print(f"    Arguments: {args_dict}")
                        tool_calls_list.append({
                             "name": fc.name,
                             "arguments": args_dict
                        })
                    elif hasattr(part, 'text'):
                        llm_text_response = part.text
                        print(f"Gemini Response Text: {llm_text_response}")
                        
            if not tool_calls_list and not llm_text_response:
                 print("Warning: Gemini response did not contain tool calls or text.")
                 # Consider checking response.prompt_feedback for blocking reasons
                 if hasattr(response, 'prompt_feedback') and response.prompt_feedback:
                      print(f"Prompt Feedback: {response.prompt_feedback}")
                      llm_text_response = f"Request blocked or failed. Feedback: {response.prompt_feedback}"
                 else:
                      llm_text_response = "No response content from Gemini."
                      
            return tool_calls_list if tool_calls_list else None, llm_text_response
        
        except ImportError:
             print("Error: google.generativeai library not installed.")
             return None, "Error: Gemini library not installed."
        except Exception as e:
            print(f"--- Error during Gemini API call --- ")
            print(f"Error: {e}")
            traceback.print_exc()
            return None, None

        # Placeholder implementation removed
        # ... 