import os
import json
import asyncio
import traceback
import json_repair
# from datetime import datetime # Removed
from pydantic import BaseModel, Field, ConfigDict, ValidationError # Keep Pydantic for validation
from typing import List, Dict, Any, Optional, Tuple

# Rich console for better logging
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

# Import core components
from .knowledge_base import KnowledgeBase
from .gcp_executor import GcpExecutor

# Import the LLM interfaces from the new location
from model.llm.base_interface import BaseLLMInterface
from model.llm.openai_llm import OpenAILLM
from model.llm.gemini_llm import GeminiLLM
from model.llm.claude_llm import ClaudeLLM
from model.llm.mistral_llm import MistralLLM

# Import the state recorder
from internal.state_recorder import RunStateLogger

# Initialize Rich Console
console = Console()

# --- Pydantic Models for Tool Calls --- 
class ToolCall(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    name: str = Field(..., description="The name of the function to call")
    arguments: Dict[str, Any] = Field(..., description="The arguments to pass to the function")

class ToolCalls(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    tool_calls: List[ToolCall] = Field(..., description="List of tool calls to make")

# --- System Prompt Definitions --- 
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

# --- Core Orchestration Logic (Loop + Node State Management) --- 

NODE_PENDING = "PENDING"
NODE_READY = "READY"
NODE_RUNNING = "RUNNING"
NODE_COMPLETED = "COMPLETED"
NODE_FAILED = "FAILED"

# --- State File --- 
# STATE_FILE_PATH = "saturn_run_state.json"

async def run_query_with_feedback(
    query: str,
    config: Dict[str, Any],
    knowledge_base: KnowledgeBase, 
    gcp_executor: GcpExecutor,    
    max_attempts: int = 5,
    verbose: bool = False
) -> None:
    """
    Main loop: Process query, call LLM, manage execution of planned tool calls 
    using node states, log state via RunStateLogger, handle errors, and retry.
    """
    console.print(Panel(f"Processing Query: [cyan]{query}[/cyan]", title="[bold blue]Saturn Orchestrator[/bold blue]", border_style="blue"))
    
    # Initialize the state logger
    state_logger = RunStateLogger(query)
    
    final_status = "FAILED" # Default to failure unless explicitly completed
    final_errors = []
    
    try:
        llm_interface = get_llm_interface(config)
    except (ValueError, RuntimeError) as e:
        console.print(f"[bold red]Error:[/] Failed initializing LLM interface: {e}")
        final_status = "INIT_FAILED"
        final_errors = [{"error": f"LLM Init Failed: {e}"}]
        state_logger.set_final_run_status(final_status, final_errors)
        state_logger.save_state()
        return

    system_prompt = build_system_prompt()
    attempt = 0
    previous_run_errors = [] 

    while attempt < max_attempts:
        console.print(Panel(f"Starting Attempt {attempt + 1}/{max_attempts}", style="bold blue"))
        state_logger.set_attempts(attempt + 1)
        current_attempt_errors = [] 
        node_states: Dict[str, str] = {}
        node_outputs: Dict[str, Any] = {}
        node_args: Dict[str, Dict[str, Any]] = {}
        plan_nodes = [] 

        try:
            # 1. Get Available Tools (Logging adjusted with Rich)
            console.print("[info]Fetching available tools...[/info]")
            available_tools = knowledge_base.get_formatted_tools(query)
            if not available_tools: 
                console.print("[bold yellow]Warning:[/] No tools found/formatted by Knowledge Base.")
                available_tools = []
            else: 
                tool_names = [t.get('function', {}).get('name', '?') for t in available_tools]
                console.print(f"[info]Using tools:[/] {tool_names}")

            # 2. Call LLM for Plan (Logging adjusted with Rich)
            console.print("[info]Calling LLM for plan...[/info]")
            if previous_run_errors:
                console.print("[info]Providing previous errors as feedback to LLM:[/info]")
                console.print(previous_run_errors) # Rich nicely formats dicts/lists
                
            proposed_tool_calls, llm_text_response = await llm_interface.get_tool_calls(
                query=query, 
                system_prompt=system_prompt,
                tools=available_tools, 
                previous_errors=previous_run_errors 
            )
            previous_run_errors = [] # Clear errors after passing them

            # 3. Process LLM Response (Extract & Initialize Nodes)
            extracted_calls = []
            if proposed_tool_calls:
                console.print(f"[info]LLM proposed {len(proposed_tool_calls)} tool calls directly.[/info]")
                extracted_calls = proposed_tool_calls
            elif llm_text_response:
                console.print(f"[info]LLM provided text response, attempting to parse JSON...[/info]")
                console.print(Syntax(llm_text_response, "json", theme="default", line_numbers=False)) # Print potential JSON with syntax highlighting
                try:
                    cleaned = llm_text_response.strip().removeprefix('```json').removesuffix('```').strip()
                    if cleaned:
                        parsed = json_repair.loads(cleaned)
                        if isinstance(parsed, dict) and isinstance(parsed.get('tool_calls'), list):
                            raw_calls = parsed['tool_calls']
                            console.print(f"[info]Successfully parsed {len(raw_calls)} potential calls from text.[/info]")
                            for item in parsed['tool_calls']:
                                # Handle variations in tool name key
                                name = item.get('name') or item.get('function') or item.get('tool_name') or item.get('tool') or item.get('recipient_name')
                                # Handle variations in arguments key
                                args = item.get('arguments') or item.get('parameters')
                                
                                # Strip potential prefix like 'functions.' from recipient_name
                                if name and name.startswith('functions.'):
                                     name = name.split('.', 1)[1]
                                
                                if name and isinstance(args, dict):
                                    extracted_calls.append({'name': name, 'arguments': args})
                                else: 
                                    console.print(f"  [bold yellow]Warning:[/] Skipping item in text due to format: {item}")
                        else: 
                            console.print("[info]Parsed JSON, but not the expected 'tool_calls' structure.[/info]")
                    else: 
                        console.print("[info]Cleaned text response is empty.[/info]")
                except Exception as e: 
                    console.print(f"[bold yellow]Warning:[/] Could not parse tool calls from text: {e}")
            
            # Initialize node states and record with logger
            if extracted_calls:
                console.print(f"[info]Initializing {len(extracted_calls)} nodes from plan...[/info]")
                for i, tool_call in enumerate(extracted_calls): 
                    tool_name = tool_call.get('name')
                    tool_args_dict = tool_call.get('arguments', {})
                    if not tool_name:
                        console.print(f"  [bold red]Error:[/] Skipping node with missing name in plan.")
                        current_attempt_errors.append({"method":"PLAN_VALIDATION", "error":"Tool missing name"})
                        break 
                    
                    node_id = f"{attempt}_{i}_{tool_name}" # Keep ID unique across attempts
                    plan_nodes.append(node_id)
                    node_args[node_id] = tool_args_dict
                    initial_state = NODE_READY if i == 0 else NODE_PENDING
                    node_states[node_id] = initial_state
                    node_outputs[node_id] = None
                    console.print(f"  Node '{node_id}' initialized as {initial_state}")
                    
                    # --- Use Logger --- 
                    state_logger.record_node_initialization(
                        node_id=node_id, 
                        tool_name=tool_name, 
                        attempt=attempt + 1, 
                        args=tool_args_dict, 
                        initial_status=initial_state
                    )
                    # --- End Use --- 

                if current_attempt_errors: 
                    raise Exception("Invalid plan received from LLM (missing tool names).")
            else:
                # Handle case where no calls were extracted
                if llm_text_response:
                    console.print("[bold green]LLM provided only text response. Assuming completion.[/bold green]")
                    console.print(Panel(llm_text_response, title="Final Text Response"))
                    final_status = "COMPLETED_TEXT_RESPONSE"
                    state_logger.set_final_run_status(final_status) # Record status before exiting
                    state_logger.save_state()
                    return # Exit loop successfully
                else:
                    console.print("[bold yellow]Warning:[/] LLM provided no tool calls and no text response.")
                    current_attempt_errors.append({"method": "N/A", "error": "LLM returned empty response", "arguments": {}})
                    # Go to end of try block to handle retry/failure

            # 4. Execute Nodes based on State (Inner Loop)
            active_nodes = True
            execution_cycle = 0
            while active_nodes and extracted_calls: 
                execution_cycle += 1
                ready_nodes = [nid for nid, state in node_states.items() if state == NODE_READY]
                
                if not ready_nodes:
                    # Check if still processing or finished
                    running_or_pending = any(s in [NODE_RUNNING, NODE_PENDING] for s in node_states.values())
                    if not running_or_pending:
                        console.print(f"[info]Execution Cycle {execution_cycle}: No more READY, RUNNING, or PENDING nodes.[/info]")
                        active_nodes = False # All done or failed
                        break # Exit inner execution loop
                    else:
                        # Should not happen with asyncio.gather unless logic error
                        console.print(f"[bold yellow]Warning:[/] Cycle {execution_cycle}: No READY nodes, but RUNNING/PENDING exist. Waiting briefly...")
                        await asyncio.sleep(0.1) # Avoid busy-waiting
                        continue

                console.print(Panel(f"Execution Cycle {execution_cycle}: Running {len(ready_nodes)} READY Node(s)", style="blue"))
                tasks = []
                for node_id in ready_nodes:
                    node_states[node_id] = NODE_RUNNING
                    # --- Use Logger --- 
                    state_logger.record_node_status_change(node_id, NODE_RUNNING)
                    # --- End Use ---
                    tool_name = node_id.split('_', 2)[2] # Use correct split for unique ID
                    args = node_args[node_id]
                    console.print(f"  Queueing [cyan]{node_id}[/cyan] (Tool: {tool_name})")
                    tasks.append(_execute_single_node(gcp_executor, knowledge_base, node_id, tool_name, args, console))
                
                execution_results = await asyncio.gather(*tasks, return_exceptions=True)
                
                # Process results and update states 
                console.print(f"[info]Processing {len(execution_results)} results for cycle {execution_cycle}...[/info]")
                failed_in_batch = False
                for result_data in execution_results:
                    if isinstance(result_data, Exception):
                        console.print(f"  [bold bright_red]Fatal Error:[/] Gather returned exception: {result_data}")
                        # How to record this error state? Add general error for now.
                        error_info = {"method":"NODE_EXECUTION_GATHER", "error":f"Unhandled task exception: {result_data}", "arguments":{}}
                        current_attempt_errors.append(error_info)
                        failed_in_batch = True
                        continue # Don't try to process node result further

                    node_id, success, result_val = result_data
                    final_node_state = NODE_COMPLETED if success else NODE_FAILED
                    node_states[node_id] = final_node_state
                    
                    # --- Use Logger --- 
                    state_logger.record_node_result(node_id, success, result_val, final_node_state)
                    # --- End Use --- 
                    
                    if success:
                         console.print(f"  [bold green]Success:[/] Node [cyan]{node_id}[/cyan] completed.")
                         node_outputs[node_id] = result_val
                    else:
                        console.print(f"  [bold red]Error:[/] Node [cyan]{node_id}[/cyan] failed.")
                        error_msg = str(result_val)
                        console.print(f"    Reason: {error_msg}")
                        current_attempt_errors.append({
                            "method": node_id.split('_', 2)[2], # Use correct split 
                            "error": error_msg,
                            "arguments": node_args[node_id]
                        })
                        failed_in_batch = True
                    
                if failed_in_batch:
                    console.print("[bold red]Error occurred during node execution. Stopping this attempt.[/bold red]")
                    break # Exit the inner execution loop for this attempt

                # Update READY states for next iteration (simple sequential)
                for i, node_id in enumerate(plan_nodes):
                    if node_states[node_id] == NODE_PENDING:
                        if i > 0 and node_states[plan_nodes[i-1]] == NODE_COMPLETED:
                            console.print(f"[info]Node [cyan]{node_id}[/cyan] is now READY.[/info]")
                            node_states[node_id] = NODE_READY
                            # --- Use Logger --- 
                            state_logger.record_node_status_change(node_id, NODE_READY)
                            # --- End Use ---
            # --- End Inner Execution Loop --- 

            # 5. Check for Completion or Retry
            if not current_attempt_errors:
                # Verify all nodes actually completed (handles cases with no plan initially)
                all_completed = all(s == NODE_COMPLETED for s in node_states.values()) if node_states else True
                if all_completed:
                    console.print("\n[bold green]All planned nodes completed successfully in this attempt![/bold green]")
                    if node_outputs:
                        console.print(Panel(node_outputs, title="Final Node Outputs"))
                    final_status = "COMPLETED" # Mark overall run as completed
                    state_logger.set_final_run_status(final_status)
                    state_logger.save_state()
                    return # SUCCESSFUL COMPLETION
                else:
                    # Should not happen if loop exited correctly without errors
                    console.print(f"[bold yellow]Warning:[/] Attempt finished with no errors, but not all nodes COMPLETED. State:", {node_states})
                    current_attempt_errors.append({"method":"POST_EXECUTION_CHECK", "error":"Inconsistent final state"}) # Add error
            
            # If we reach here, errors occurred in this attempt
            previous_run_errors = current_attempt_errors # Save errors for next attempt's feedback
            # (Outer loop handles retry logic)

        except Exception as e:
            # Catch unexpected errors in the main attempt logic
            console.print(f"\n--- Unexpected Error during attempt {attempt + 1} --- ")
            console.print_exception(show_locals=False) # Use Rich exception formatting
            # Assign error to be passed to next attempt if retrying
            previous_run_errors = current_attempt_errors + [{"method": "Orchestrator Loop", "error": str(e), "arguments": {}}]
            # (Outer loop handles retry logic)
        
        # --- Increment attempt and check retry limit --- 
        attempt += 1
        if attempt < max_attempts and previous_run_errors: # Only print retry if errors occurred
            console.print(Panel(f"Attempt {attempt} Failed. Errors will be sent for correction.", style="yellow"))
            console.print("Errors for next attempt:")
            console.print(previous_run_errors)
            console.print("[info]Retrying...[/info]")
        elif attempt >= max_attempts:
            console.print(Panel("Maximum attempts reached. Orchestrator failed.", style="bold red"))
            # Loop terminates
        # else: loop terminates (no errors)

    # End of while loop
    final_errors = previous_run_errors # Errors from the last failed attempt
    # --- Set final status and save state --- 
    state_logger.set_final_run_status(final_status, final_errors)
    state_logger.save_state()
    # --- End Save --- 

    console.print(Panel(f"Orchestrator finished after {attempt} attempts.", border_style="red"))
    if final_errors: 
        console.print("[bold red]Last recorded errors:[/bold red]")
        console.print(final_errors)
    else:
        console.print("[info]Loop finished without recorded errors (check completion status).[/info]")

    # ... (final failure logging) ...

# Updated helper to use console.print (remains the same)
async def _execute_single_node(
    gcp_executor: GcpExecutor,
    knowledge_base: KnowledgeBase,
    node_id: str,
    tool_name: str,
    args: Dict[str, Any],
    console: Console
) -> Tuple[str, bool, Any]:
    """Helper to execute one node and return structured result/error."""
    try:
        console.print(f"    Starting execution: [cyan]{node_id}[/cyan] ({tool_name})")
        success, result = await gcp_executor.execute(tool_name, args, knowledge_base, console)
        console.print(f"    Finished execution: {node_id} (Success: {success})")
        return (node_id, success, result)
    except Exception as exec_err:
        console.print(f"    [bold bright_red]Fatal Error:[/] Unexpected exception during [cyan]{node_id}[/cyan] execution:")
        console.print_exception(show_locals=False)
        return (node_id, False, f"Unexpected executor error: {exec_err}")

# Example standalone usage (adapt as needed)
if __name__ == '__main__':
    # This block is for example purposes. 
    # In real usage, config loading and component initialization 
    # should happen in your application's entry point (e.g., cli.py)
    # before calling run_query_with_feedback.
    
    # --- Placeholder: Assume config loaded from YAML/Env Vars --- 
    # Example: config = load_config_from_yaml_or_env() 
    # Ensure config contains required keys like 'llm_provider', API keys, 'gcp_project_id'
    console.print("[Example Main] Config should be loaded here.")
    config = { # Dummy config for demonstration structure
        'llm_provider': 'openai', # Replace with actual loaded value
        'openai_api_key': os.getenv('OPENAI_API_KEY'), # Replace with actual loaded value
        'gcp_project_id': os.getenv('GCP_PROJECT_ID'), # Replace with actual loaded value
        'max_retries': 3
    }
    # --- End Placeholder ---
    
    # Basic check (repeat from real entry point if needed)
    if not config.get(f"{config['llm_provider']}_api_key") or not config.get('gcp_project_id'):
        console.print(f"Error: Required config keys missing (API key for {config['llm_provider']} or GCP Project ID).")
        exit(1)
    
    kb_path = 'api_defs' # Or load from config
    try:
        # --- Placeholder: Assume components initialized --- 
        console.print("[Example Main] Components (KB, Executor) should be initialized here.")
        kb = KnowledgeBase(kb_path)
        kb.build_definitions()
        executor = GcpExecutor(config)
        # --- End Placeholder ---

        test_query = "Create a serverless vpc access connector named test-conn in us-central1 using default network and cidr 10.8.0.0/28"
        console.print("Starting query processing loop (Example).")
        asyncio.run(run_query_with_feedback(
            test_query, 
            config,       # Use the loaded config
            kb,           # Use the initialized KB
            executor,     # Use the initialized Executor
            config.get('max_retries', 5)
        ))
    except FileNotFoundError:
        console.print(f"ERROR: API definition directory '{kb_path}' not found.")
    except Exception as main_err:
        console.print(f"\n--- ERROR during main execution --- ")
        console.print_exception(show_locals=False) 