import os
import json
import asyncio
import traceback
import json_repair
import re # Import re for parsing
from pydantic import BaseModel, Field, ConfigDict # Keep Pydantic for potential future use, but ToolCall/ToolCalls are removed
from typing import List, Dict, Any, Optional, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

from .gcp_executor import GcloudExecutor
from model.llm.base_interface import BaseLLMInterface
from model.llm.openai_llm import OpenAILLM
from model.llm.gemini_llm import GeminiLLM
from model.llm.claude_llm import ClaudeLLM
from model.llm.mistral_llm import MistralLLM
from internal.state_recorder import RunStateLogger

# Import DAG utilities from the existing internal path
from internal.dag.dag import AcyclicGraph, Edge, ORDER_DOWN, ORDER_UP # Added ORDER_UP

# Import prompt templates
from .prompts import (
    PLANNING_SYSTEM_PROMPT_TEMPLATE,
    GCLOUD_STEP_SYSTEM_PROMPT_TEMPLATE,
    GCLOUD_STEP_ERROR_HANDLING_PROMPT_TEMPLATE
)

console = Console()

# --- Global variable for gcloud documentation ---
# In a more advanced system, this could be dynamically fetched based on the command/service.
GCLOUD_DOCS_CONTENT = ""

def load_gcloud_docs():
    """Loads a predefined gcloud documentation file."""
    global GCLOUD_DOCS_CONTENT
    try:
        # Using a common example doc, replace with a more general or dynamic loading if possible
        doc_path = 'internal/tools/gcloud_online_docs_markdown/compute/instances/create/index.md'
        doc_path2 = 'internal/tools/gcloud_online_docs_markdown/compute/machine-types/list/index.md'
        doc_path3 = 'internal/tools/gcloud_online_docs_markdown/compute/addresses/create/index.md'
        if os.path.exists(doc_path):
            with open(doc_path, 'r', encoding='utf-8') as f:
                GCLOUD_DOCS_CONTENT = f.read()
            with open(doc_path2, 'r', encoding='utf-8') as f:
                GCLOUD_DOCS_CONTENT += f.read()
            with open(doc_path3, 'r', encoding='utf-8') as f:
                GCLOUD_DOCS_CONTENT += f.read()
            console.print(f"[info]Successfully loaded gcloud docs from {doc_path}[/info]")
        else:
            console.print(f"[yellow]Warning: gcloud documentation file not found at {doc_path}[/yellow]")
            GCLOUD_DOCS_CONTENT = "No specific gcloud documentation was loaded."
    except Exception as e:
        console.print(f"[yellow]Warning: Could not read gcloud documentation: {e}[/yellow]")
        GCLOUD_DOCS_CONTENT = "Error loading gcloud documentation."

# --- Helper function to parse gcloud commands ---
# def _parse_gcloud_command(command_string: str) -> Dict[str, Any]:
#     """Parses a gcloud command string into a structured dictionary."""
#     parsed_command: Dict[str, Any] = {
#         "full_command": command_string,
#         "base_command": "",
#         "subcommands": [],
#         "flags": {},
#         "positional_args": [],
#         "parsing_error": None # Initialize parsing_error
#     }
# 
#     try:
#         # Regex to split by space while respecting quotes.
#         # Handles simple cases. For '[^']*', we use string concatenation for clarity.
#         tokens = re.findall(r'"[^"]*"|' + "'[^']*'" + r'|\S+', command_string)
#         
#         if not tokens:
#             return parsed_command 
# 
#         parsed_command["base_command"] = tokens.pop(0)
#         if parsed_command["base_command"] != "gcloud":
#             parsed_command["parsing_error"] = "Command does not start with gcloud"
#             return parsed_command
# 
#         idx = 0
#         temp_subcommands_and_positional = [] # Temporary list to hold non-flag tokens
# 
#         while idx < len(tokens):
#             token = tokens[idx]
#             if token.startswith("--"):
#                 flag_name = token
#                 if "=" in flag_name:
#                     parts = flag_name.split("=", 1)
#                     parsed_command["flags"][parts[0]] = parts[1].strip('\"'')
#                     idx += 1
#                 elif idx + 1 < len(tokens) and not tokens[idx+1].startswith("--") and not tokens[idx+1].startswith("-") :
#                     parsed_command["flags"][flag_name] = tokens[idx+1].strip('\"'')
#                     idx += 2
#                 else:
#                     parsed_command["flags"][flag_name] = True
#                     idx += 1
#             elif token.startswith("-") and not token.startswith("--"): # Basic short flags
#                 if len(token) > 1 and token[1] == '=': # -f=value
#                     parts = token.split("=", 1)
#                     parsed_command["flags"][parts[0]] = parts[1].strip('\"'')
#                     idx +=1
#                 elif idx + 1 < len(tokens) and not tokens[idx+1].startswith("--") and not tokens[idx+1].startswith("-") and len(token) == 2: # -f value 
#                     parsed_command["flags"][token] = tokens[idx+1].strip('\"'')
#                     idx += 2
#                 else: # boolean short flags like -v or grouped like -abc (not splitting grouped for now)
#                     parsed_command["flags"][token] = True
#                     idx += 1
#             else:
#                 temp_subcommands_and_positional.append(token.strip('\"''))
#                 idx += 1
#         
#         # Refine subcommands and positional arguments from temp_subcommands_and_positional
#         consuming_subcommands = True
#         for t_token in temp_subcommands_and_positional:
#             if consuming_subcommands and t_token.isalpha() and not any(char.isdigit() or char in '.=/' for char in t_token):
#                 is_likely_subcommand = True
#                 try:
#                     if re.match(r'^[a-zA-Z0-9][a-zA-Z0-9._/-]*$', t_token) and ('.' in t_token or '/' in t_token or any(c.isdigit() for c in t_token)):
#                          if len(parsed_command["subcommands"]) > 0: 
#                             is_likely_subcommand = False
#                 except re.error: 
#                     pass 
#                 
#                 if is_likely_subcommand:
#                     parsed_command["subcommands"].append(t_token)
#                 else:
#                     consuming_subcommands = False
#                     parsed_command["positional_args"].append(t_token)
#             else:
#                 consuming_subcommands = False
#                 parsed_command["positional_args"].append(t_token)
# 
#     except Exception as e:
#         parsed_command["parsing_error"] = f"Error during command parsing: {str(e)}"
#     
#     return parsed_command

# --- LLM Interface Loader (remains the same) ---
def get_llm_interface(config: Dict[str, Any]) -> BaseLLMInterface:
    provider = config.get('llm_provider', 'openai').lower()
    if provider == 'openai':
        return OpenAILLM(config)
    elif provider == 'gemini':
        return GeminiLLM(config)
    elif provider == 'claude':
        return ClaudeLLM(config)
    elif provider == 'mistral':
        return MistralLLM(config)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")

# --- DAG Planning and Execution Logic ---

async def _generate_plan_dag(
    user_query: str,
    llm_interface: BaseLLMInterface,
    state_logger: RunStateLogger
) -> Tuple[Optional[AcyclicGraph], Optional[Dict[str, Any]]]:
    """
    Calls the LLM to generate a multi-step plan and constructs a DAG.
    Returns a tuple of (AcyclicGraph, Dict_of_step_details) or (None, None) on failure.
    """
    console.print(Panel(f"Generating execution plan for query: [cyan]{user_query}[/cyan]", title="[bold blue]Planning Phase[/bold blue]"))
    # state_logger.record_event("plan_generation_start", {"query": user_query})

    planning_prompt = PLANNING_SYSTEM_PROMPT_TEMPLATE.format(user_query=user_query)
    
    try:
        response = await llm_interface.agenerate([
            {"role": "system", "content": "You are a planning assistant."},
            {"role": "user", "content": planning_prompt}
        ])
        raw_plan_str = response.choices[0].message.content.strip()
        console.print(f"Raw plan from LLM:\\n{raw_plan_str}")

        try:
            plan_steps = json.loads(raw_plan_str)
        except json.JSONDecodeError:
            console.print("[yellow]Initial JSON parsing failed, trying json_repair...[/yellow]")
            try:
                plan_steps = json_repair.loads(raw_plan_str)
            except Exception as repair_err:
                error_msg = f"Failed to parse plan JSON even with json_repair: {repair_err}"
                console.print(f"[bold red]Error:[/] {error_msg}")
                # state_logger.record_event("plan_generation_failed", {"error": error_msg, "raw_response": raw_plan_str})
                return None, None
        
        if not isinstance(plan_steps, list):
            error_msg = "LLM plan is not a list of steps."
            console.print(f"[bold red]Error:[/] {error_msg}")
            # state_logger.record_event("plan_generation_failed", {"error": error_msg, "parsed_plan": plan_steps})
            return None, None

        dag = AcyclicGraph()
        step_details_map = {}
        step_ids = set()

        for step in plan_steps:
            if not isinstance(step, dict) or not all(k in step for k in ["id", "description", "dependencies"]):
                error_msg = f"Invalid step structure in plan (missing id, description, or dependencies): {step}"
                console.print(f"[bold red]Error:[/] {error_msg}")
                # state_logger.record_event("plan_generation_failed", {"error": error_msg, "plan_steps": plan_steps})
                return None, None
            
            step_id = step["id"]
            if step_id in step_ids:
                error_msg = f"Duplicate step ID found in plan: {step_id}"
                console.print(f"[bold red]Error:[/] {error_msg}")
                # state_logger.record_event("plan_generation_failed", {"error": error_msg, "plan_steps": plan_steps})
                return None, None
            
            step_ids.add(step_id)
            dag.add(step_id) 
            step_details_map[step_id] = {
                "id": step_id,
                "description": step.get("description", ""),
                "dependencies": step.get("dependencies", []),
                "tool_to_use": step.get("tool_to_use", "gcloud_command_generation"),
                "pass_output_to_next": step.get("pass_output_to_next", True)
            }

        for step_id_key, details in step_details_map.items(): 
            for dep_id in details.get("dependencies", []):
                if dep_id not in step_details_map:
                    error_msg = f"Dependency '{dep_id}' for step '{step_id_key}' not found in plan."
                    console.print(f"[bold red]Error:[/] {error_msg}")
                    # state_logger.record_event("plan_generation_failed", {"error": error_msg, "plan_steps": plan_steps})
                    return None, None
                dag.connect(Edge(dep_id, step_id_key)) 

        try:
            dag.validate() 
            execution_order = dag.topo_order(ORDER_UP)
            
            # Log DAG structure using RunStateLogger
            dag_nodes_for_log = {}
            for sid, s_details in step_details_map.items():
                dag_nodes_for_log[sid] = {
                    "description": s_details.get("description"),
                    "dependencies": s_details.get("dependencies", []),
                    "tool_to_use": s_details.get("tool_to_use"),
                    "pass_output_to_next": s_details.get("pass_output_to_next")
                }
            
            state_logger.record_dag_structure({
                "nodes": dag_nodes_for_log,
                "edges": [str(e) for e in dag.edges],
                "execution_order": execution_order
            })
            # Initialize all planned nodes in the logger
            for step_id_to_init, details_to_init in step_details_map.items():
                 state_logger.record_node_initialization(
                     node_id=step_id_to_init,
                     tool_name=details_to_init.get("tool_to_use", "gcloud_command_generation"), 
                     attempt=0, # Will be incremented per execution attempt
                     args={}, # Args for gcloud are generated dynamically per step
                     initial_status="PLANNED" # New status to indicate it's from the plan
                 )

            console.print(f"Plan generated successfully. DAG has {len(dag.vertices)} nodes and {len(dag.edges)} edges.")
            console.print(f"Execution order: {' -> '.join(execution_order)}")
            return dag, step_details_map
        except Exception as dag_err: 
            error_msg = f"DAG validation failed: {dag_err}"
            console.print(f"[bold red]Error:[/] {error_msg}")
            # state_logger.record_event("plan_generation_failed", {"error": error_msg, "plan_steps": plan_steps})
            return None, None

    except Exception as e:
        error_msg = f"Error during plan generation: {str(e)}"
        console.print(f"[bold red]Error:[/] {error_msg}")
        if hasattr(e, 'response') and hasattr(e.response, 'text'): # type: ignore
            error_msg += f" LLM Response: {e.response.text}" # type: ignore
        # state_logger.record_event("plan_generation_failed", {"error": error_msg, "traceback": traceback.format_exc()})
        return None, None


async def _execute_dag_step(
    step_id: str,
    step_details: Dict[str, Any],
    llm_interface: BaseLLMInterface,
    gcp_executor: GcloudExecutor,
    state_logger: RunStateLogger,
    previous_step_outputs: Dict[str, Any],
    max_attempts: int = 3, 
    verbose: bool = False
) -> Tuple[bool, Any]:
    """
    Executes a single step from the DAG.
    Generates a gcloud command using LLM, executes it, and handles retries.
    """
    console.print(Panel(f"Executing Step: [cyan]{step_id}[/cyan] - {step_details.get('description', 'N/A')}", title="[bold blue]Step Execution[/bold blue]"))
    # state_logger.record_event("step_execution_start", {"step_id": step_id, "description": step_details.get('description')})
    state_logger.record_node_status_change(step_id, "RUNNING")

    context_str = "Context from previous steps (if any):\\n"
    if previous_step_outputs:
        for prev_step_id, output in previous_step_outputs.items():
            context_str += f"- Output of step '{prev_step_id}': {json.dumps(output, indent=2)}\\n"
    else:
        context_str += "No outputs from previous steps available.\\n"
    
    current_step_description = step_details.get('description', 'No description provided for this step.')
    
    attempt = 0
    last_error = ""
    command_to_execute = ""

    while attempt < max_attempts:
        attempt += 1
        console.print(f"Attempt {attempt}/{max_attempts} for step [cyan]{step_id}[/cyan]")
        # state_logger.record_event("step_attempt", {"step_id": step_id, "attempt_number": attempt})
        # Potentially log attempt start with state_logger.record_node_status_change if more granular status is needed

        try:
            if attempt == 1: 
                prompt_template = GCLOUD_STEP_SYSTEM_PROMPT_TEMPLATE
                user_content = prompt_template.format(
                    step_id=step_id,
                    step_description=current_step_description,
                    context_from_previous_steps=context_str,
                    gcloud_docs=GCLOUD_DOCS_CONTENT 
                )
            else: 
                prompt_template = GCLOUD_STEP_ERROR_HANDLING_PROMPT_TEMPLATE
                user_content = prompt_template.format(
                    step_id=step_id,
                    step_description=current_step_description,
                    previous_command=command_to_execute,
                    error_message=last_error,
                    context_from_previous_steps=context_str,
                    gcloud_docs=GCLOUD_DOCS_CONTENT
                )

            response = await llm_interface.agenerate([
                {"role": "system", "content": "You are a gcloud CLI expert."},
                {"role": "user", "content": user_content}
            ])
            command_to_execute = response.choices[0].message.content.strip()
            
            command_to_execute = command_to_execute.replace('`', '').replace('\\n', ' ').strip()
            
            if not command_to_execute:
                console.print("[yellow]Warning: LLM generated an empty command. Skipping execution for this attempt.[/yellow]")
                last_error = "LLM generated an empty command."
                # state_logger.record_event("step_attempt_failed_empty_command", {"step_id": step_id, "attempt": attempt})
                if attempt >= max_attempts: 
                     state_logger.record_node_result(step_id, False, {"error": last_error}, "FAILED_EMPTY_COMMAND")
                     return False, {"error": last_error, "step_id": step_id}
                continue

            console.print(f"Generated gcloud command for step {step_id} (Attempt {attempt}):\\n[bold magenta]{command_to_execute}[/bold magenta]")
            # state_logger.record_event("step_command_generated", {"step_id": step_id, "attempt": attempt, "command": command_to_execute})
            # We can store the command in the node's state if RunStateLogger is augmented or via a generic field

            success, result_or_error = await gcp_executor.execute(command_to_execute, console)

            if success:
                console.print(f"[bold green]Step {step_id} executed successfully![/bold green]")
                # parsed_cmd_dict = _parse_gcloud_command(command_to_execute) # Temporarily disabled parser
                success_payload = {
                    "result": result_or_error,
                    "executed_command_str": command_to_execute, 
                    # "parsed_command": parsed_cmd_dict # Temporarily disabled parser output
                }
                state_logger.record_node_result(step_id, True, success_payload, "COMPLETED_SUCCESS")
                return True, result_or_error # Return original result_or_error for internal orchestrator flow
            else:
                last_error = str(result_or_error)
                console.print(f"[bold red]Command for step {step_id} failed (Attempt {attempt}):[/bold red] {last_error}")
                # state_logger.record_event("step_execution_failure_attempt", {"step_id": step_id, "attempt": attempt, "command": command_to_execute, "error": last_error})
                # Error for this attempt is stored in last_error for the next LLM call
        
        except Exception as e:
            last_error = f"Exception during step {step_id} attempt {attempt}: {str(e)}"
            if verbose:
                console.print(f"[bold red]{last_error}[/bold red]\\n{traceback.format_exc()}")
            else:
                console.print(f"[bold red]{last_error}[/bold red]")
            # state_logger.record_event("step_execution_exception_attempt", {"step_id": step_id, "attempt": attempt, "error": last_error, "traceback": traceback.format_exc()})
            if command_to_execute: 
                last_error += f"\\nFailing command was: `{command_to_execute}`"

    console.print(f"[bold red]Step {step_id} failed after {max_attempts} attempts.[/bold red]")
    # parsed_cmd_dict_on_fail = _parse_gcloud_command(command_to_execute) # Temporarily disabled parser
    state_logger.record_node_result(step_id, False, {"error": last_error, "final_attempt_command_str": command_to_execute}, "FAILED_MAX_ATTEMPTS") # Removed parsed_command field
    return False, {"error": last_error, "step_id": step_id}


async def run_query_with_feedback(
    query: str,
    config: Dict[str, Any],
    gcp_executor: GcloudExecutor,
    max_total_attempts: int = 5, 
    verbose: bool = False
) -> None:
    console.print(Panel(f"Processing Query: [cyan]{query}[/cyan]", title="[bold blue]Saturn Orchestrator[/bold blue]", border_style="blue"))
    
    state_logger = RunStateLogger(query) 
    load_gcloud_docs() 

    final_status = "FAILED"
    accumulated_errors = [] 

    try:
        llm_interface = get_llm_interface(config)
        console.print("LLM interface initialized.")
    except (ValueError, RuntimeError) as e:
        console.print(f"[bold red]Error:[/] Failed initializing LLM interface: {e}")
        state_logger.set_final_run_status("LLM_INIT_FAILED", [{"error": f"LLM Init Failed: {str(e)}"}])
        state_logger.save_state()
        return

    dag, step_details_map = await _generate_plan_dag(query, llm_interface, state_logger)

    if not dag or not step_details_map:
        console.print("[bold red]Failed to generate a valid execution plan. Orchestrator cannot proceed.[/bold red]")
        state_logger.set_final_run_status("PLAN_GENERATION_FAILED", [{"error": "Failed to generate DAG plan"}])
        state_logger.save_state()
        return

    try:
        execution_order = dag.topo_order(ORDER_UP)
        console.print(f"DAG Execution Order: {' -> '.join(execution_order)}")
    except Exception as e: 
        error_msg = f"Failed to get execution order from DAG: {e}"
        console.print(f"[bold red]{error_msg}[/bold red]")
        state_logger.set_final_run_status("DAG_EXECUTION_ORDER_FAILED", [{"error": error_msg}])
        state_logger.save_state()
        return

    step_outputs: Dict[str, Any] = {}
    all_steps_succeeded = True

    for step_id in execution_order:
        if step_id not in step_details_map:
            console.print(f"[bold red]Error: Step ID '{step_id}' from execution order not found in step details. Skipping.[/bold red]")
            accumulated_errors.append({"step_id": step_id, "error": "Step details not found"})
            all_steps_succeeded = False
            break 
        
        current_step_details = step_details_map[step_id]
        
        step_dependencies = [edge.source for edge in dag.edges if edge.target == step_id]
        
        contextual_outputs = {}
        for dep_id in step_dependencies:
            if dep_id in step_outputs:
                dep_details = step_details_map.get(dep_id, {})
                if dep_details.get("pass_output_to_next", True):
                    if isinstance(step_outputs[dep_id], dict) and 'error' in step_outputs[dep_id]:
                        dep_error_info = step_outputs[dep_id]['error']
                        console.print(f"[yellow]Warning: Dependency '{dep_id}' (marked to pass output) for step '{step_id}' failed. Its error was: {dep_error_info}. Passing error as context.[/yellow]")
                        contextual_outputs[dep_id] = {"status": "FAILED", "output": dep_error_info}
                    else:
                        contextual_outputs[dep_id] = {"status": "SUCCESS", "output": step_outputs[dep_id]}
                else:
                    console.print(f"[info]Output of dependency '{dep_id}' for step '{step_id}' was not passed as per 'pass_output_to_next' flag.[/info]")

        step_success, step_result_or_error = await _execute_dag_step(
            step_id,
            current_step_details,
            llm_interface,
            gcp_executor,
            state_logger,
            contextual_outputs, 
            max_attempts=config.get('max_step_retries', 3), 
            verbose=verbose
        )
        
        step_outputs[step_id] = step_result_or_error 

        if not step_success:
            console.print(f"[bold red]Step {step_id} ultimately failed. Halting further execution.[/bold red]")
            all_steps_succeeded = False
            if isinstance(step_result_or_error, dict) and "error" in step_result_or_error:
                 accumulated_errors.append({"step_id": step_id, "command_failed": current_step_details.get("last_command", "N/A") , "error": step_result_or_error["error"]})
            else:
                 accumulated_errors.append({"step_id": step_id, "command_failed": current_step_details.get("last_command", "N/A"), "error": str(step_result_or_error)})
            break 

    if all_steps_succeeded and not accumulated_errors: 
        final_status = "COMPLETED_SUCCESSFULLY"
        console.print(Panel("[bold green]All steps completed successfully![/bold green]", border_style="green"))
    elif all_steps_succeeded and accumulated_errors: 
         final_status = "COMPLETED_WITH_UNHANDLED_ERRORS"
         console.print(Panel("[bold yellow]All steps reported success, but errors were accumulated. Please review logs.[/bold yellow]", border_style="yellow"))
    else:
        final_status = "FAILED_AT_STEP"
        console.print(Panel(f"[bold red]Orchestration failed. See errors above or in logs.[/bold red]", border_style="red"))

    state_logger.set_final_run_status(final_status, accumulated_errors) 
    # state_logger.add_event_to_log("run_step_outputs", {"outputs": step_outputs}) # Output per node is now in node state
    state_logger.save_state()

    console.print(f"Orchestrator finished with status: {final_status}")
    if accumulated_errors:
        console.print("[bold red]Final accumulated errors:[/bold red]")
        for err_idx, err_item in enumerate(accumulated_errors):
            console.print(f"  Error {err_idx + 1}: {json.dumps(err_item, indent=2)}")


# Example standalone usage (adapt as needed)
if __name__ == '__main__':
    console.print("[Example Main] Config should be loaded here.")
    config_example = {
        'llm_provider': os.getenv('LLM_PROVIDER', 'openai'), 
        'openai_api_key': os.getenv('OPENAI_API_KEY'),
        'gemini_api_key': os.getenv('GEMINI_API_KEY'), 
        'gcp_project_id': os.getenv('GCP_PROJECT_ID'),
        'max_step_retries': 2, 
    }
    
    current_llm_provider = config_example['llm_provider']
    api_key_name = f"{current_llm_provider}_api_key"
    if not config_example.get(api_key_name) and current_llm_provider != "mock": 
        console.print(f"[bold red]Error:[/] API key for {current_llm_provider} ({api_key_name}) not found in environment variables.")
        exit(1)
    if not config_example.get('gcp_project_id'):
        console.print("[bold red]Error:[/] GCP_PROJECT_ID not found in environment variables.")
        exit(1)
    
    console.print(f"Using LLM Provider: {current_llm_provider}")
    console.print(f"Using GCP Project ID: {config_example['gcp_project_id']}")

    try:
        gcp_executor_instance = GcloudExecutor(config_example)
        
        test_query = "Create a new Google Compute Engine instance named 'test-instance1' in zone 'us-central1-a' with machine type 'e2-medium' and image family 'debian-11' from project 'debian-cloud'. Then, stop this instance."

        console.print(f'Starting orchestrator for query: "{test_query}"') 
        asyncio.run(run_query_with_feedback(
            test_query, 
            config_example,
            gcp_executor_instance,
            verbose=True 
        ))
    except Exception as main_err:
        console.print(f"--- UNHANDLED ERROR IN MAIN --- ")
        console.print_exception(show_locals=True) 