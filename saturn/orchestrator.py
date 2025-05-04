import json
import asyncio
import traceback
# Removed OpenAI specific import: from openai import AsyncOpenAI
from pydantic import BaseModel, Field, ConfigDict # Keep Pydantic for validation
from typing import List, Dict, Any, Optional, Tuple

# Import core components
from .knowledge_base import KnowledgeBase
from .gcp_executor import GcpExecutor

# Import the LLM interfaces from the new location
from model.llm.base_interface import BaseLLMInterface
from model.llm.openai_llm import OpenAILLM
from model.llm.gemini_llm import GeminiLLM
from model.llm.claude_llm import ClaudeLLM
from model.llm.mistral_llm import MistralLLM

# --- Pydantic Models for Tool Calls --- (Keep as is)
class ToolCall(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str = Field(..., description="The name of the function to call")
    arguments: Dict[str, Any] = Field(..., description="The arguments to pass to the function")

class ToolCalls(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    tool_calls: List[ToolCall] = Field(..., description="List of tool calls to make")

# --- System Prompt Definitions --- (Keep as is, moved task instruction update here)
task_instruction = """
Your are an expert in composing Google Cloud Platform (GCP) API function calls based on user requests. Your goal is to understand the user's natural language query and translate it into one or more precise GCP API calls using the available tools.
Ensure all required parameters for the chosen function(s) are included in the arguments. If the user does not specify a value for a required parameter, attempt to use a sensible default or minimum valid value based on the parameter description or common GCP practices (e.g., 'default' network, minimum throughput, basic CIDR ranges like /28 if a range is needed but unspecified). Only omit required parameters if it's impossible to determine a valid value.
Handle errors gracefully by analyzing feedback and correcting the calls.
""".strip()

format_instruction = """
Output *only* the required JSON tool calls in the format specified by the function calling API for the model you are using. Use the exact function names provided in the available tools list (e.g., 'vpcaccess_v1.create_connector'). If no function call is needed, return the appropriate empty response (e.g., `{"tool_calls": []}` for OpenAI). Ensure parameter types match the tool definitions.
""".strip()

error_handling_instruction = """
When a function call fails, you will receive the error message and the arguments you previously used. Analyze the error (e.g., missing parameters, invalid values, permission issues, resource conflicts) and the API definition. Modify the function call arguments to fix the error while preserving the user's original intent. If the error is unrecoverable, explain why.
""".strip()

def build_system_prompt():
    # System prompt might need slight variations per LLM, but keep generic for now
    return f"{task_instruction}\n\n{format_instruction}\n\n{error_handling_instruction}"

# --- LLM Interface Loader --- 
def get_llm_interface(config: Dict[str, Any]) -> BaseLLMInterface:
    """Instantiates the correct LLM interface based on configuration."""
    provider = config.get('llm_provider', 'openai').lower() # Default to openai
    
    if provider == 'openai':
        return OpenAILLM(config)
    elif provider == 'gemini':
        return GeminiLLM(config)
    elif provider == 'claude':
        return ClaudeLLM(config)
    elif provider == 'mistral':
        return MistralLLM(config)
    else:
        raise ValueError(f"Unsupported LLM provider specified in config: {provider}")

# --- Core Orchestration Logic --- 
async def run_query_with_feedback(
    query: str,
    config: Dict[str, Any],
    knowledge_base: KnowledgeBase, 
    gcp_executor: GcpExecutor,    
    max_attempts: int = 5
) -> None:
    """
    Main loop to process query, call selected LLM, execute GCP calls, and handle errors.
    """
    # --- Initialize LLM Interface --- 
    try:
        llm_interface = get_llm_interface(config)
    except (ValueError, RuntimeError) as e:
        print(f"Error initializing LLM interface: {e}")
        return

    attempt = 0
    previous_errors = []
    system_prompt = build_system_prompt()

    while attempt < max_attempts:
        current_errors = [] # Initialize for each attempt
        print(f"\n--- Attempt {attempt + 1}/{max_attempts} ---")

        try:
            # --- Get Tools from Knowledge Base --- 
            # Note: Tool format might need adjustment per LLM *before* sending.
            # The get_formatted_tools might need to accept a target_format parameter.
            # For now, assume KnowledgeBase provides OpenAI format, and interfaces adapt if needed.
            available_tools = knowledge_base.get_formatted_tools(query)
            if not available_tools:
                 print("Warning: No tools found/formatted by Knowledge Base.")
                 available_tools = [] # Ensure it's a list
            else:
                 tool_names = [t.get('function', {}).get('name', 'UnknownTool') for t in available_tools]
                 print(f"Using tools: {tool_names}")

            # --- Call selected LLM Interface --- 
            # The interface handles prompt construction (initial vs error)
            proposed_tool_calls, llm_text_response = await llm_interface.get_tool_calls(
                query=query,
                system_prompt=system_prompt,
                tools=available_tools, 
                previous_errors=previous_errors
            )

            # --- Process LLM Response --- 
            if proposed_tool_calls:
                 # --- Validate and Execute Tool Calls --- 
                try:
                    # Use Pydantic models for basic validation of name/arguments format
                    tools_data = {"tool_calls": proposed_tool_calls}
                    validated_tools = ToolCalls.model_validate(tools_data)
                    print("Tool calls validated structurally.")

                    for call in validated_tools.tool_calls:
                        print(f"Executing call: {call.name}")
                        # Pass the knowledge_base instance to the executor
                        success, result = await gcp_executor.execute(call.name, call.arguments, knowledge_base)

                        if not success:
                            print(f"  [Error] Execution failed: {result}")
                            current_errors.append({
                                "method": call.name,
                                "error": str(result),
                                "arguments": call.arguments # Use the validated dict
                            })
                        else:
                            print(f"  [Success] Execution successful.") # Don't log potentially large results here
                            # print(f"  [Success] Execution successful: {result}")
                            # (Phase 2) Update state manager here

                except Exception as validation_or_exec_err:
                     print(f"Error during tool validation or execution: {validation_or_exec_err}")
                     current_errors.append({
                        "method": "N/A",
                        "error": f"Tool validation/execution failed: {validation_or_exec_err}",
                        "arguments": proposed_tool_calls # Log the raw proposed calls on validation error
                    })
            elif llm_text_response:
                 print(f"LLM provided text response instead of tool calls: {llm_text_response}")
                 # If we had previous errors, this means LLM failed to correct them
                 if previous_errors:
                     print("LLM did not provide corrected tool calls despite errors.")
                     current_errors.append({ 
                        "method": "N/A", 
                        "error": "LLM failed to provide tool calls after errors.", 
                        "arguments": {}
                    })
                 else:
                      # No previous errors, LLM just gave text -> Success (no action needed)
                      print("Processing finished successfully (no tool calls needed/returned).")
                      return 
            else:
                 # This case means the LLM call itself failed (e.g., API error)
                 print("LLM call failed or returned no usable response.")
                 current_errors.append({
                     "method": "N/A",
                     "error": "LLM call failed or returned empty response.",
                     "arguments": {}
                 })

            # --- Check for Completion or Retry --- 
            if not current_errors:
                print("\nAll operations completed successfully in this attempt!")
                return

            previous_errors = current_errors
            attempt += 1
            print(f"\nAttempt {attempt} failed. Errors:")
            for error in previous_errors:
                print(f"  Method: {error['method']}")
                print(f"  Error: {error['error']}")
            if attempt < max_attempts:
                print("Retrying with error feedback...")
            else:
                print("Max attempts reached.")

        except Exception as e:
            print(f"\n--- Unexpected Error during attempt {attempt + 1} --- ")
            print(f"Error: {e}")
            traceback.print_exc()
            # Ensure current_errors is defined before appending
            if 'current_errors' not in locals():
                current_errors = []
            current_errors.append({
                "method": "N/A",
                "error": f"Overall loop exception: {e}",
                "arguments": {}
            })
            previous_errors = current_errors
            attempt += 1
            if attempt >= max_attempts:
                 print("Max attempts reached due to fatal error.")
                 # break # Exit loop immediately
            else:
                 print("Retrying after fatal error...")

    print(f"\n--- Failed after {max_attempts} attempts --- ")
    # Use the latest errors accumulated before exiting the loop
    if previous_errors:
         print("Last recorded errors:")
         print(json.dumps(previous_errors, indent=2))
    else:
         print("No specific errors recorded, but loop terminated.")


# Example standalone usage (replace with actual CLI entry point)
# if __name__ == '__main__':
#     # Load combined config (CLI args + config file)
#     # config = load_combined_config()
#     config = {
#         'llm_provider': 'openai', # Or 'gemini', 'claude', 'mistral'
#         'openai_api_key': 'sk-...', 
#         # Add other keys: 'gemini_api_key', 'anthropic_api_key', 'mistral_api_key'
#         'gcp_project_id': 'your-gcp-project',
#         'gcp_credentials_path': None # Or path to service account key
#     }
#     kb = KnowledgeBase('api_defs')
#     executor = GcpExecutor(config)
#     test_query = "Create a serverless vpc access connector named test-conn in us-central1 using default network and cidr 10.8.0.0/28" 
#     asyncio.run(run_query_with_feedback(test_query, config, kb, executor)) 