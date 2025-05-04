# Contains logic refactored from call.py related to OpenAI API interaction
import json
import asyncio
from openai import AsyncOpenAI # Use AsyncOpenAI
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Dict, Any, Optional
import traceback

# Import actual components from the package
from .knowledge_base import KnowledgeBase 
from .gcp_executor import GcpExecutor 

# Remove Placeholder/Stubs
# class KnowledgeBase: ...
# class GcpExecutor: ...

# --- Pydantic Models for Tool Calls --- (Copied from call.py)
class ToolCall(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str = Field(..., description="The name of the function to call")
    arguments: Dict[str, Any] = Field(..., description="The arguments to pass to the function")

class ToolCalls(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    tool_calls: List[ToolCall] = Field(..., description="List of tool calls to make")

# --- Core Logic (Refactored from call.py) --- 

# Define instructions (consider moving to config or constants file)
task_instruction = """
You are an expert in composing Google Cloud Platform (GCP) API function calls based on user requests. Your goal is to understand the user's natural language query and translate it into one or more precise GCP API calls using the available tools. Ensure all required parameters for the chosen function(s) are included in the arguments. If the user does not specify a value for a required parameter, attempt to use a sensible default or minimum valid value based on the parameter description or common GCP practices (e.g., 'default' network, minimum throughput, basic CIDR ranges like /28 if a range is needed but unspecified). Only omit required parameters if it's impossible to determine a valid value. Handle errors gracefully by analyzing feedback and correcting the calls.
""".strip()

format_instruction = """
Output *only* the required JSON tool calls. Use the exact function names provided in the available tools list (e.g., 'vpcaccess_v1.create_connector'). If no function call is needed, return `{"tool_calls": []}`. Ensure parameter types match the tool definitions.
""".strip()

error_handling_instruction = """
When a function call fails, you will receive the error message and the arguments you previously used. Analyze the error (e.g., missing parameters, invalid values, permission issues, resource conflicts) and the API definition. Modify the function call arguments to fix the error while preserving the user's original intent. If the error is unrecoverable, explain why.
""".strip()

def build_system_prompt():
    # Simplified system prompt
    return f"{task_instruction}\n\n{format_instruction}\n\n{error_handling_instruction}"

def create_error_feedback_prompt(query: str, errors: List[Dict[str, Any]]) -> str:
    """Builds a prompt incorporating previous errors for correction."""
    prompt = f"""{build_system_prompt()}

Original Query: {query}

The previous attempt resulted in the following errors:
"""
    for error_info in errors:
        prompt += f"- Function: {error_info['method']}\n"
        prompt += f"  Arguments Used: {json.dumps(error_info['arguments'], indent=2)}\n"
        prompt += f"  Error Received: {error_info['error']}\n"
    prompt += "\nPlease analyze the errors and provide corrected function calls in the required JSON format."
    return prompt

async def run_query_with_feedback(
    query: str,
    config: Dict[str, Any],
    knowledge_base: KnowledgeBase, # Use the real KnowledgeBase
    gcp_executor: GcpExecutor,     # Use the real GcpExecutor
    max_attempts: int = 5
) -> None:
    """
    Main loop to process query, call OpenAI, execute GCP calls, and handle errors.
    Refactored from tool_call_with_feedback_loop in call.py.
    """
    openai_api_key = config.get('openai_api_key')
    if not openai_api_key:
        print("Error: OpenAI API key missing in config.")
        return

    # Initialize Async OpenAI Client
    try:
        client = AsyncOpenAI(api_key=openai_api_key)
    except Exception as e:
        print(f"Error initializing AsyncOpenAI client: {e}")
        return

    attempt = 0
    previous_errors = []
    system_prompt = build_system_prompt()

    while attempt < max_attempts:
        current_errors = [] # Initialize for each attempt
        print(f"\n--- Attempt {attempt + 1}/{max_attempts} ---")

        try:
            # --- Get Tools from Knowledge Base --- 
            available_tools = knowledge_base.get_formatted_tools(query) # Use real KB method
            if not available_tools:
                 print("Warning: No tools found/formatted by Knowledge Base.")
                 available_tools = []
            else:
                 tool_names = [t.get('function', {}).get('name', 'UnknownTool') for t in available_tools]
                 print(f"Using tools: {tool_names}")

            # --- Prepare messages for OpenAI --- 
            messages = []
            if previous_errors:
                error_prompt = create_error_feedback_prompt(query, previous_errors)
                messages.append({"role": "system", "content": error_prompt})
                print("Sending error feedback to OpenAI...")
            else:
                messages.append({"role": "system", "content": system_prompt})
                messages.append({"role": "user", "content": query})
                print("Sending initial query to OpenAI...")

            # --- Call OpenAI (using Async client) --- 
            print("Calling OpenAI API...")
            response = await client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=available_tools,
                tool_choice="auto" if available_tools else None
            )
            print("Received response from OpenAI.")
            message = response.choices[0].message

            # --- Process OpenAI Response (Tool Calls) --- 
            tool_calls_list = []
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
                            print(f"  [Error] Invalid JSON arguments from LLM: {json_err}")
                            current_errors.append({
                                "method": tool_call_obj.function.name,
                                "error": f"Invalid arguments JSON from LLM: {json_err}",
                                "arguments": tool_call_obj.function.arguments
                            })
                    else:
                        print(f"  [Warning] Received non-function tool call type: {tool_call_obj.type}")

            else:
                print("OpenAI did not propose any tool calls.")
                if message.content:
                    print(f"OpenAI Response Content: {message.content}")
                    if not previous_errors:
                         print("Processing finished successfully (no tool calls needed/returned).")
                         return
                elif previous_errors:
                     print("OpenAI did not provide corrected tool calls despite errors.")
                     current_errors.append({
                         "method": "N/A",
                         "error": "LLM failed to provide tool calls after errors.",
                         "arguments": {}
                     })

            # --- Validate and Execute Tool Calls --- 
            if tool_calls_list and not current_errors:
                try:
                    tools_data = {"tool_calls": tool_calls_list}
                    validated_tools = ToolCalls.model_validate(tools_data)
                    print("Tool calls validated.")

                    for call in validated_tools.tool_calls:
                        print(f"Executing call: {call.name}")
                        # Pass the knowledge_base instance to the executor
                        success, result = await gcp_executor.execute(call.name, call.arguments, knowledge_base)

                        if not success:
                            print(f"  [Error] Execution failed: {result}")
                            current_errors.append({
                                "method": call.name,
                                "error": str(result),
                                "arguments": call.arguments
                            })
                        else:
                            print(f"  [Success] Execution successful: {result}")
                            # (Phase 2) Update state manager here

                except Exception as validation_or_exec_err:
                     print(f"Error during tool validation or execution: {validation_or_exec_err}")
                     current_errors.append({
                        "method": "N/A",
                        "error": f"Tool validation/execution failed: {validation_or_exec_err}",
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
            else:
                 print("Retrying after fatal error...")

    print(f"\n--- Failed after {max_attempts} attempts --- ")
    print("Last recorded errors:")
    print(json.dumps(previous_errors, indent=2))


# Example standalone usage (for testing, replace with CLI call)
# if __name__ == '__main__':
#     test_config = load_config()
#     kb = KnowledgeBase('api_defs')
#     executor = GcpExecutor(test_config)
#     test_query = "Create a serverless vpc access connector..." # Your test query
#     asyncio.run(run_query_with_feedback(test_query, test_config, kb, executor)) 