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

# Import for JSON Schema validation
import jsonschema
from jsonschema import ValidationError as JsonSchemaValidationError

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

        try:
            # 1. Get Available Tools
            console.print("[info]Fetching available tools...[/info]")
            available_tools = knowledge_base.get_formatted_tools(query)
            if not available_tools: 
                console.print("[bold yellow]Warning:[/] No tools found/formatted by Knowledge Base.")
                available_tools = []
            else: 
                tool_names = [t.get('function', {}).get('name', '?') for t in available_tools]
                console.print(f"[info]Using tools:[/] {tool_names}")

            # 2. Call LLM for Plan
            console.print("[info]Calling LLM for plan...[/info]")
            if previous_run_errors:
                console.print("[info]Providing previous errors as feedback to LLM:[/info]")
                console.print(previous_run_errors)
                
            proposed_tool_calls, llm_text_response = await llm_interface.get_tool_calls(
                query=query, 
                system_prompt=system_prompt,
                tools=available_tools, 
                previous_errors=previous_run_errors 
            )
            previous_run_errors = [] # Clear errors after passing them

            # 3. Process LLM Response and Build DAG
            dag_definition = {
                "nodes": {},
                "edges": [],
                "execution_order": []
            }
            
            if proposed_tool_calls:
                console.print(f"[info]LLM proposed {len(proposed_tool_calls)} tool calls.[/info]")
                
                # Create nodes for each tool call
                for i, tool_call in enumerate(proposed_tool_calls):
                    node_id = f"step_{i}"
                    tool_name = tool_call.get('name')
                    tool_args = tool_call.get('arguments', {})
                    
                    if not tool_name:
                        console.print(f"  [bold red]Error:[/] Skipping node with missing name in plan.")
                        current_attempt_errors.append({"method":"PLAN_VALIDATION", "error":"Tool missing name"})
                        continue
                    
                    # Validate parameters
                    param_schema = knowledge_base.get_tool_parameter_json_schema(tool_name)
                    if param_schema:
                        try:
                            jsonschema.validate(instance=tool_args, schema=param_schema)
                            console.print(f"  [green]OK:[/] Arguments for '{tool_name}' passed JSON schema validation.")
                        except JsonSchemaValidationError as e_schema:
                            console.print(f"  [bold red]Validation Error:[/] Arguments for '{tool_name}' failed JSON schema validation.")
                            validation_error_summary = f"Schema validation failed for {tool_name}: {e_schema.message}"
                            current_attempt_errors.append({
                                "method": tool_name,
                                "error_type": "SCHEMA_VALIDATION",
                                "error": validation_error_summary,
                                "arguments": tool_args
                            })
                            continue
                    
                    # Add node to DAG
                    dag_definition["nodes"][node_id] = {
                        "tool": tool_name,
                        "parameters": tool_args,
                        "description": f"Execute {tool_name}",
                        "dependencies": [] if i == 0 else [f"step_{i-1}"]  # Sequential dependencies
                    }
                    
                    # Add edge for sequential execution
                    if i > 0:
                        dag_definition["edges"].append(f"step_{i-1} -> {node_id}")
                    
                    # Add to execution order
                    dag_definition["execution_order"].append(node_id)
                    
                    # Log node initialization
                    state_logger.record_node_initialization(
                        node_id=node_id,
                        tool_name=tool_name,
                        attempt=attempt + 1,
                        args=tool_args,
                        initial_status="PENDING"
                    )
            
            elif llm_text_response:
                console.print("[bold green]LLM provided only text response. Assuming completion.[/bold green]")
                console.print(Panel(llm_text_response, title="Final Text Response"))
                final_status = "COMPLETED_TEXT_RESPONSE"
                state_logger.set_final_run_status(final_status)
                state_logger.save_state()
                return
            else:
                console.print("[bold yellow]Warning:[/] LLM provided no tool calls and no text response.")
                current_attempt_errors.append({"method": "N/A", "error": "LLM returned empty response", "arguments": {}})

            # 4. Execute DAG if we have nodes
            if dag_definition["nodes"]:
                console.print("\n[bold cyan]Executing DAG...[/bold cyan]")
                state_logger.record_dag_structure(dag_definition)
                
                # Execute the DAG
                step_results = await gcp_executor.execute_dag(
                    dag_definition=dag_definition,
                    knowledge_base=knowledge_base,
                    console=console
                )
                
                # Process results
                all_success = True
                for step_id, (success, result) in step_results.items():
                    if success:
                        state_logger.record_node_result(
                            node_id=step_id,
                            success=True,
                            result_or_error=result,
                            final_status="COMPLETED"
                        )
                    else:
                        all_success = False
                        state_logger.record_node_result(
                            node_id=step_id,
                            success=False,
                            result_or_error=result,
                            final_status="FAILED"
                        )
                        current_attempt_errors.append({
                            "method": dag_definition["nodes"][step_id]["tool"],
                            "error": str(result),
                            "arguments": dag_definition["nodes"][step_id]["parameters"]
                        })
                
                if all_success:
                    console.print("\n[bold green]All steps completed successfully![/bold green]")
                    final_status = "COMPLETED"
                    state_logger.set_final_run_status(final_status)
                    state_logger.save_state()
                    return
                
            previous_run_errors = current_attempt_errors

        except Exception as e:
            console.print(f"\n--- Unexpected Error during attempt {attempt + 1} --- ")
            console.print_exception(show_locals=False)
            previous_run_errors = current_attempt_errors + [{"method": "Orchestrator Loop", "error": str(e), "arguments": {}}]
        
        attempt += 1
        if attempt < max_attempts and previous_run_errors:
            console.print(Panel(f"Attempt {attempt} Failed. Errors will be sent for correction.", style="yellow"))
            console.print("Errors for next attempt:")
            console.print(previous_run_errors)
            console.print("[info]Retrying...[/info]")
        elif attempt >= max_attempts:
            console.print(Panel("Maximum attempts reached. Orchestrator failed.", style="bold red"))

    final_errors = previous_run_errors
    state_logger.set_final_run_status(final_status, final_errors)
    state_logger.save_state()

    console.print(Panel(f"Orchestrator finished after {attempt} attempts.", border_style="red"))
    if final_errors: 
        console.print("[bold red]Last recorded errors:[/bold red]")
        console.print(final_errors)
    else:
        console.print("[info]Loop finished without recorded errors (check completion status).[/info]")

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