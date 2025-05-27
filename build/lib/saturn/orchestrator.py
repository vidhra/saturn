import os
import json
import asyncio
import traceback
import json_repair
import re # Import re for parsing
import shlex # Import shlex for robust command splitting
from pydantic import BaseModel, Field, ConfigDict # Keep Pydantic for potential future use, but ToolCall/ToolCalls are removed
from typing import List, Dict, Any, Optional, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table # Import Table for better display

from .gcp_executor import GcloudExecutor
from .aws_executor import AWSExecutor # Added AWSExecutor
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
    GCLOUD_STEP_SYSTEM_PROMPT_TEMPLATE, # Reverted to GCLOUD specific
    GCLOUD_STEP_ERROR_HANDLING_PROMPT_TEMPLATE, # Reverted to GCLOUD specific
    AWS_STEP_SYSTEM_PROMPT_TEMPLATE,    # Added AWS specific
    AWS_STEP_ERROR_HANDLING_PROMPT_TEMPLATE # Added AWS specific
)
from .rag_engine import RAGEngine, DEFAULT_EMBED_MODEL_NAME # Import new default
from .file_build_tools import FileBuildToolCaller

console = Console()



# --- Helper function to parse gcloud commands (Simplified Version using shlex) ---
def _parse_gcloud_command(command_string: str) -> Dict[str, Any]:
    """Parses a gcloud command string into a structured dictionary using shlex."""
    # This function is gcloud specific. If aws parsing is needed, a more generic one or aws specific one would be required.
    # For now, it's kept as is, as the primary command parsing is for logging/display and not critical for execution logic if command is opaque.
    parsed_command: Dict[str, Any] = {
        "original_command": command_string,
        "base_command": "",
        "subcommands": [],
        "flags": {},
        "positional_args": [],
        "parsing_error": None
    }
    
    try:
        tokens = shlex.split(command_string)
        
        if not tokens:
            parsed_command["parsing_error"] = "Empty command string"
            return parsed_command

        # Make it slightly more generic: check if first token is gcloud or aws
        if tokens[0] not in ["gcloud", "aws"]:
            parsed_command["parsing_error"] = f"Command does not start with gcloud or aws: {tokens[0]}"
            parsed_command["base_command"] = tokens[0] if tokens else ""
            parsed_command["subcommands"] = tokens[1:] if len(tokens) > 1 else []
            return parsed_command
        
        parsed_command["base_command"] = tokens.pop(0)
        
        idx = 0
        while idx < len(tokens):
            token = tokens[idx]
            if token.startswith("--"):
                flag_name = token
                if "=" in flag_name:
                    name, value = flag_name.split("=", 1)
                    parsed_command["flags"][name] = value
                    idx += 1
                elif idx + 1 < len(tokens) and not tokens[idx+1].startswith("-"):
                    parsed_command["flags"][flag_name] = tokens[idx+1]
                    idx += 2
                else:
                    parsed_command["flags"][flag_name] = True # Boolean flag
                    idx += 1
            elif token.startswith("-") and not token.startswith("--"):
                if "=" in token:
                    name, value = token.split("=",1)
                    parsed_command["flags"][name] = value
                    idx += 1
                elif len(token) == 2 and idx + 1 < len(tokens) and not tokens[idx+1].startswith("-"):
                    parsed_command["flags"][token] = tokens[idx+1]
                    idx += 2
                else: 
                    parsed_command["flags"][token] = True 
                    idx += 1
            else:
                if not parsed_command["flags"]:
                    parsed_command["subcommands"].append(token)
                else:
                    parsed_command["positional_args"].append(token)
                idx += 1
                
    except Exception as e:
        parsed_command["parsing_error"] = f"Error during command parsing: {str(e)}"
        if not parsed_command.get("subcommands"):
             parsed_command["subcommands"] = [command_string]
    return parsed_command

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
        # console.print(f"Raw plan from LLM:\n{raw_plan_str}") # Old raw JSON print

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

        # Display the plan in a more readable format
        plan_display_table = Table(title="LLM Generated Plan", show_header=True, header_style="bold blue")
        plan_display_table.add_column("Step ID", style="cyan", no_wrap=True)
        plan_display_table.add_column("Provider", style="green") # Added Provider column
        plan_display_table.add_column("Description", style="white")
        plan_display_table.add_column("Dependencies", style="yellow")
        plan_display_table.add_column("Pass Output", style="magenta")

        if not plan_steps: # Handle empty plan from LLM
            console.print("[yellow]LLM returned an empty plan.[/yellow]")
        else:
            for i, step_data in enumerate(plan_steps):
                if isinstance(step_data, dict):
                    step_id_disp = step_data.get("id", f"Step {i+1} (ID missing)")
                    provider_disp = step_data.get("cloud_provider", "N/A").upper()
                    description_disp = step_data.get("description", "N/A")
                    dependencies_disp = ", ".join(step_data.get("dependencies", [])) or "-"
                    pass_output_disp = str(step_data.get("pass_output_to_next", "True")) # Default to True for display
                    plan_display_table.add_row(step_id_disp, provider_disp, description_disp, dependencies_disp, pass_output_disp)
                else:
                    plan_display_table.add_row(f"Step {i+1}", "N/A", "Invalid step data format", "-", "-")
            console.print(plan_display_table)

        dag = AcyclicGraph()
        step_details_map = {}
        step_ids = set()

        for step in plan_steps:
            # Added validation for cloud_provider
            if not isinstance(step, dict) or not all(k in step for k in ["id", "description", "dependencies", "cloud_provider"]):
                error_msg = f"Invalid step structure (missing id, description, dependencies, or cloud_provider): {step}"
                console.print(f"[bold red]Error:[/] {error_msg}")
                # state_logger.record_event("plan_generation_failed", {"error": error_msg, "plan_steps": plan_steps})
                return None, None
            
            if step["cloud_provider"] not in ["gcp", "aws"]:
                error_msg = f"Invalid cloud_provider '{step['cloud_provider']}' in step {step['id']}. Must be 'gcp' or 'aws'."
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
                "cloud_provider": step["cloud_provider"], # Store cloud_provider
                "dependencies": step.get("dependencies", []),
                "tool_to_use": step.get("tool_to_use", "cli_command_generation"),
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
                    "cloud_provider": s_details.get("cloud_provider"),
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
                     tool_name=details_to_init.get("tool_to_use", "cli_command_generation"), 
                     attempt=0, # Will be incremented per execution attempt
                     args={ "cloud_provider": details_to_init.get("cloud_provider") }, # Log provider here
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
    gcp_executor: Optional[GcloudExecutor], # Now optional
    aws_executor: Optional[AWSExecutor],   # Added AWSExecutor, optional
    state_logger: RunStateLogger,
    rag_engine: RAGEngine,
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

    cloud_provider = step_details.get("cloud_provider")
    
    # Determine CLI name, prompt templates, and doc context key based on provider
    cli_name = ""
    system_prompt_template = ""
    error_prompt_template = ""
    doc_context_key = ""
    provider_full_name = ""

    if cloud_provider == "gcp":
        cli_name = "gcloud"
        system_prompt_template = GCLOUD_STEP_SYSTEM_PROMPT_TEMPLATE
        error_prompt_template = GCLOUD_STEP_ERROR_HANDLING_PROMPT_TEMPLATE
        doc_context_key = "gcloud_docs"
        provider_full_name = "Google Cloud Platform (GCP)"
        if not gcp_executor:
            error_msg = f"GCP Executor not available for GCP step: {step_id}"
            console.print(f"[bold red]Error:[/] {error_msg}")
            state_logger.record_node_result(step_id, False, {"error": error_msg}, "FAILED_EXECUTOR_MISSING")
            return False, {"error": error_msg, "step_id": step_id}
    elif cloud_provider == "aws":
        cli_name = "aws"
        system_prompt_template = AWS_STEP_SYSTEM_PROMPT_TEMPLATE
        error_prompt_template = AWS_STEP_ERROR_HANDLING_PROMPT_TEMPLATE
        doc_context_key = "aws_docs"
        provider_full_name = "Amazon Web Services (AWS)"
        if not aws_executor:
            error_msg = f"AWS Executor not available for AWS step: {step_id}"
            console.print(f"[bold red]Error:[/] {error_msg}")
            state_logger.record_node_result(step_id, False, {"error": error_msg}, "FAILED_EXECUTOR_MISSING")
            return False, {"error": error_msg, "step_id": step_id}
    else:
        error_msg = f"Unknown cloud provider '{cloud_provider}' for step {step_id}."
        console.print(f"[bold red]Error:[/] {error_msg}")
        state_logger.record_node_result(step_id, False, {"error": error_msg}, "FAILED_UNKNOWN_PROVIDER")
        return False, {"error": error_msg, "step_id": step_id}

    context_str = "Context from previous steps (if any):\n"
    if previous_step_outputs:
        for prev_step_id, output_info in previous_step_outputs.items(): # output_info is now a dict
             if isinstance(output_info, dict):
                status = output_info.get("status", "UNKNOWN")
                actual_output = output_info.get("output", "No output available")
                context_str += f"- Output of step '{prev_step_id}' (Status: {status}): {json.dumps(actual_output, indent=2)}\n"
             else: # Fallback for older format or direct string output
                context_str += f"- Output of step '{prev_step_id}': {json.dumps(output_info, indent=2)}\n"

    else:
        context_str += "No outputs from previous steps available.\n"
    
    current_step_description = step_details.get('description', 'No description provided for this step.')
    
    # Fetch RAG context for the current step description
    rag_query_for_docs = f"{provider_full_name} {cli_name} {current_step_description}"
    cli_docs_context = "No specific documentation found by RAG."
    if rag_engine and rag_engine.query_engine:
        console.print(f"[RAG] Fetching docs for: '{rag_query_for_docs[:100]}...'")
        cli_docs_context = rag_engine.query_docs(rag_query_for_docs)
        if verbose:
            console.print(Panel(cli_docs_context, title=f"RAG Context for {step_id} ({cloud_provider.upper()})", border_style="dim yellow"))
    elif not rag_engine:
        console.print("[yellow]Warning: RAG engine instance not provided to _execute_dag_step.[/yellow]")
    else: # rag_engine exists but query_engine is None
        console.print("[yellow]Warning: RAG engine query_engine not initialized. Using generic doc context.[/yellow]")

    attempt = 0
    last_error = ""
    command_to_execute = ""
    parsed_command_for_log: Dict[str, Any] = {}


    while attempt < max_attempts:
        attempt += 1
        console.print(f"Attempt {attempt}/{max_attempts} for step [cyan]{step_id}[/cyan] ({cloud_provider.upper()})")
        # state_logger.record_event("step_attempt", {"step_id": step_id, "attempt_number": attempt})
        # Potentially log attempt start with state_logger.record_node_status_change if more granular status is needed

        try:
            prompt_args = {
                "step_id": step_id,
                "step_description": current_step_description,
                "context_from_previous_steps": context_str,
                doc_context_key: cli_docs_context # e.g., gcloud_docs or aws_docs
            }
            current_prompt_template_to_use = ""

            if attempt == 1: 
                current_prompt_template_to_use = system_prompt_template
            else: 
                current_prompt_template_to_use = error_prompt_template
                prompt_args["previous_command"] = command_to_execute
                prompt_args["error_message"] = last_error
            
            user_content = current_prompt_template_to_use.format(**prompt_args)

            response = await llm_interface.agenerate([
                {"role": "system", "content": f"You are a {cli_name} CLI expert for {provider_full_name}."},
                {"role": "user", "content": user_content}
            ])
            command_to_execute = response.choices[0].message.content.strip()
            
            command_to_execute = command_to_execute.replace('`', '').replace('\n', ' ').strip()
            
            if not command_to_execute:
                console.print("[yellow]Warning: LLM generated an empty command. Skipping execution for this attempt.[/yellow]")
                last_error = "LLM generated an empty command."
                # state_logger.record_event("step_attempt_failed_empty_command", {"step_id": step_id, "attempt": attempt})
                if attempt >= max_attempts: 
                     parsed_command_for_log = _parse_gcloud_command(command_to_execute) if command_to_execute else {"original_command": "EMPTY"}
                     state_logger.record_node_result(step_id, False, {"error": last_error, "parsed_command": parsed_command_for_log }, "FAILED_EMPTY_COMMAND")
                     return False, {"error": last_error, "step_id": step_id}
                continue

            # Parse and display the command before execution
            parsed_command_for_log = _parse_gcloud_command(command_to_execute)
            
            display_table = Table(title=f"Command for Step: {step_id} ({cloud_provider.upper()}) (Attempt {attempt})", show_header=True, header_style="bold magenta")
            display_table.add_column("Component", style="dim")
            display_table.add_column("Details")
            
            # display_table.add_row("Full Command", Syntax(parsed_command_for_log.get("original_command", command_to_execute), "bash", theme="monokai", line_numbers=False)) # Removed Full Command row
            if parsed_command_for_log.get("base_command"):
                 display_table.add_row("Base", parsed_command_for_log["base_command"])
            # if parsed_command_for_log.get("subcommands"):
            #      display_table.add_row("Subcommands", ", ".join(parsed_command_for_log["subcommands"])) # Removed Subcommands row
            if parsed_command_for_log.get("flags"):
                flags_display_list = []
                for k,v in parsed_command_for_log["flags"].items():
                    # Remove leading hyphens for display
                    display_key = k.lstrip('-')
                    flags_display_list.append(f"{display_key}: {v}")
                flags_str = "\n".join(flags_display_list)
                display_table.add_row("Flags", flags_str)
            if parsed_command_for_log.get("positional_args"):
                display_table.add_row("Positional Args", ", ".join(parsed_command_for_log["positional_args"]))
            if parsed_command_for_log.get("parsing_error"):
                display_table.add_row("Parsing Error", parsed_command_for_log["parsing_error"], style="red")
            
            console.print(display_table)


            if cloud_provider == "gcp":
                success, result_or_error = await gcp_executor.execute(command_to_execute, console, step_id)
            elif cloud_provider == "aws":
                success, result_or_error = await aws_executor.execute(command_to_execute, console, step_id)
            # else case already handled by checks at the start of the function

            if success:
                console.print(f"[bold green]Step {step_id} ({cloud_provider.upper()}) executed successfully![/bold green]")
                # Display the result in the console
                if isinstance(result_or_error, str) and result_or_error.strip(): # Check if it's a non-empty string
                    console.print(Panel(result_or_error, title=f"Result for Step: {step_id}", title_align="left", border_style="green"))
                elif result_or_error: # For other types of results (e.g. dicts, lists if parser produced them)
                    console.print(Panel(str(result_or_error), title=f"Result for Step: {step_id}", title_align="left", border_style="green"))
                
                success_payload = {
                    "result": result_or_error,
                    "executed_command_str": command_to_execute, 
                    # "parsed_command": parsed_cmd_dict # Temporarily disabled parser output
                }
                state_logger.record_node_result(step_id, True, success_payload, "COMPLETED_SUCCESS")
                return True, result_or_error # Return original result_or_error for internal orchestrator flow
            else:
                last_error = str(result_or_error)
                console.print(f"[bold red]Command for step {step_id} ({cloud_provider.upper()}) failed (Attempt {attempt}):[/bold red] {last_error}")

        except Exception as e:
            last_error = f"Exception during step {step_id} attempt {attempt}: {str(e)}"
            if verbose:
                console.print(f"[bold red]{last_error}[/bold red]\n{traceback.format_exc()}")
            else:
                console.print(f"[bold red]{last_error}[/bold red]")
            # state_logger.record_event("step_execution_exception_attempt", {"step_id": step_id, "attempt": attempt, "error": last_error, "traceback": traceback.format_exc()})
            if command_to_execute: 
                last_error += f"\nFailing command was: `{command_to_execute}`"

    console.print(f"[bold red]Step {step_id} ({cloud_provider.upper()}) failed after {max_attempts} attempts.[/bold red]")
    # parsed_cmd_dict_on_fail = _parse_gcloud_command(command_to_execute) # Temporarily disabled parser
    state_logger.record_node_result(step_id, False, {"error": last_error, "final_attempt_command_str": command_to_execute, "parsed_command": parsed_command_for_log}, "FAILED_MAX_ATTEMPTS") # Removed parsed_command field
    return False, {"error": last_error, "step_id": step_id}


async def run_query_with_feedback(
    query: str,
    config: Dict[str, Any],
    rag_engine: RAGEngine, 
    max_total_attempts: int = 5, 
    verbose: bool = False
) -> None:
    console.print(Panel(f"Processing Query: [cyan]{query}[/cyan]", title="[bold blue]Saturn Orchestrator[/bold blue]", border_style="blue"))
    
    state_logger = RunStateLogger(query)
    final_status = "FAILED"
    accumulated_errors = [] 
    
    gcp_executor_instance: Optional[GcloudExecutor] = None
    aws_executor_instance: Optional[AWSExecutor] = None
    
    # --- File tool integration ---
    file_tool_caller = FileBuildToolCaller(working_directory=config.get('working_directory', '.'))
    file_tool_schemas = file_tool_caller.get_tools_schema()
    file_tool_names = set([tool['function']['name'] for tool in file_tool_schemas])
    
    # If you use KnowledgeBase elsewhere, merge file tools into it here (example):
    # from .knowledge_base import KnowledgeBase
    # kb = KnowledgeBase(api_defs_dir, external_tools=file_tool_schemas)
    
    # --- Cloud executors as before ---
    if config.get('gcp_project_id'):
        gcp_executor_instance = GcloudExecutor(config)
        console.print("GCP Executor initialized.")
    if config.get('aws_region') or config.get('aws_profile'):
        aws_executor_instance = AWSExecutor(config)
        console.print("AWS Executor initialized.")
    if not gcp_executor_instance and not aws_executor_instance:
        console.print("[bold red]Error:[/] No cloud executor could be initialized. Check GCP/AWS configurations.")
        state_logger.set_final_run_status("EXECUTOR_INIT_FAILED", [{"error": "No executor initialized"}])
        state_logger.save_state()
        return
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
            elif dep_id in step_details_map and not step_details_map[dep_id].get("pass_output_to_next", True):
                 console.print(f"[info]Output of dependency '{dep_id}' for step '{step_id}' was not passed as per 'pass_output_to_next' flag.[/info]")
        # --- File tool step execution ---
        tool_to_use = current_step_details.get("tool_to_use")
        cloud_provider = current_step_details.get("cloud_provider")
        if tool_to_use in file_tool_names or (cloud_provider is None or str(cloud_provider).lower() == "none"):
            tool_args = current_step_details.get("tool_args", {})
            console.print(Panel(f"[File Tool] Executing file tool: [cyan]{tool_to_use}[/cyan] with args: {tool_args}", title=f"Step: {step_id}", border_style="blue"))
            try:
                result = await file_tool_caller.call_tool(tool_to_use, tool_args)
                step_outputs[step_id] = result
                state_logger.record_node_result(step_id, result.get("success", False), result, "COMPLETED_FILE_TOOL" if result.get("success", False) else "FAILED_FILE_TOOL")
                if not result.get("success", False):
                    console.print(f"[bold red]File tool step {step_id} failed: {result.get('error', 'Unknown error')}[/bold red]")
                    accumulated_errors.append({"step_id": step_id, "error": result.get("error", "Unknown error")})
                    all_steps_succeeded = False
                    break
                else:
                    console.print(f"[green]File tool step {step_id} completed successfully.[/green]")
                    continue  # Skip cloud executor logic for this step
            except Exception as file_exc:
                console.print(f"[bold red]Exception during file tool step {step_id}: {file_exc}[/bold red]")
                accumulated_errors.append({"step_id": step_id, "error": str(file_exc)})
                all_steps_succeeded = False
                break
        # --- End file tool step execution ---
        step_success, step_result_or_error = await _execute_dag_step(
            step_id,
            current_step_details,
            llm_interface,
            gcp_executor_instance, # Pass the potentially None GCP executor
            aws_executor_instance, # Pass the potentially None AWS executor
            state_logger,
            rag_engine, # Pass the RAG engine instance
            contextual_outputs, 
            max_attempts=config.get('max_step_retries', 3), 
            verbose=verbose
        )
        step_outputs[step_id] = step_result_or_error 
        if not step_success:
            console.print(f"[bold red]Step {step_id} ultimately failed. Halting further execution.[/bold red]")
            all_steps_succeeded = False
            if isinstance(step_result_or_error, dict) and "error" in step_result_or_error:
                 accumulated_errors.append({"step_id": step_id, "error": step_result_or_error["error"]})
            else:
                 accumulated_errors.append({"step_id": step_id, "error": str(step_result_or_error)})
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
    state_logger.save_state()
    console.print(f"Orchestrator finished with status: {final_status}")
    if accumulated_errors:
        console.print("[bold red]Final accumulated errors for the run:[/bold red]")
        for err_idx, err_item in enumerate(accumulated_errors):
            console.print(f"  Error {err_idx + 1}: {json.dumps(err_item, indent=2)}")


# Example standalone usage (adapt as needed)
if __name__ == '__main__':
    console.print("[Example Main] Config should be loaded here.")
    # --- Configuration for the example ---
    default_docs_path = os.path.join(os.path.dirname(__file__), '..' , 'internal', 'tools', 'gcloud_online_docs_markdown')
    docs_path_for_rag_init = os.getenv("GCLOUD_DOCS_PATH", default_docs_path)

    vector_store_type = os.getenv("VECTOR_STORE", "chroma").lower()
    db_configuration = None

    if vector_store_type == "chroma":
        db_configuration = {
            "chroma_path": os.getenv("CHROMA_DB_PATH", "./db/chroma_db"),
            "chroma_collection_name": os.getenv("CHROMA_COLLECTION", "gclouddocs_main")
        }
    elif vector_store_type == "duckdb":
        db_configuration = {
            "duckdb_path": os.getenv("DUCKDB_PATH", "./db/duckdb_store"),
            "duckdb_file_name": os.getenv("DUCKDB_FILE_NAME", "gclouddocs_vector_store.duckdb"),
            "duckdb_table_name": os.getenv("DUCKDB_TABLE_NAME", "gclouddocs_embeddings")
        }
    
    # For the 'run' command context (this __main__ block), 
    # we want RAGEngine to load from persistent store if it exists.
    # It should only build on init if it's an in-memory store AND docs are provided.
    # The RAGEngine.__init__ itself handles this logic now with documents_path_for_init.
    # So, for persistent stores, rag_build_on_init should be False here.
    # For "default" (in-memory), RAGEngine will build if documents_path_for_init is valid.
    rag_build_on_init_for_main = False 
    if vector_store_type == "default" and os.path.isdir(docs_path_for_rag_init):
        rag_build_on_init_for_main = True
    # If persistent store is chosen, this example __main__ assumes `ingest-docs` was run prior.
    # RAGEngine.__init__ will try to load from the persistent store.

    config_example = {
        'llm_provider': os.getenv('LLM_PROVIDER', 'openai'), 
        'openai_api_key': os.getenv('OPENAI_API_KEY'),
        'gemini_api_key': os.getenv('GEMINI_API_KEY'), 
        'google_api_key': os.getenv('GOOGLE_API_KEY'), # For Gemini Embeddings / Google AI Studio
        'anthropic_api_key': os.getenv('ANTHROPIC_API_KEY'), # For Claude
        'mistral_api_key': os.getenv('MISTRAL_API_KEY'), # For Mistral
        'gcp_project_id': os.getenv('GCP_PROJECT_ID'),
        'aws_region': os.getenv('AWS_REGION', 'us-east-1'), # Added AWS region to config
        'aws_profile': os.getenv('AWS_PROFILE'),           # Added AWS profile to config
        'max_step_retries': 2,
        'rag_docs_path_for_init': docs_path_for_rag_init, # Path for RAGEngine, primarily for in-memory or if build_on_init is true
        'rag_embedding_model': os.getenv("RAG_EMBED_MODEL", DEFAULT_EMBED_MODEL_NAME), # Use new default
        'vector_store_choice': vector_store_type,
        'db_config': db_configuration,
        'rag_build_on_init': rag_build_on_init_for_main # Use the refined flag
    }
    
    current_llm_provider = config_example['llm_provider']
    api_key_name = f"{current_llm_provider}_api_key"
    if not config_example.get(api_key_name) and current_llm_provider != "mock": 
        console.print(f"[bold red]Error:[/] API key for {current_llm_provider} ({api_key_name}) not found in environment variables.")
        exit(1)
    if not config_example.get('gcp_project_id') and not (config_example.get('aws_region') or config_example.get('aws_profile')):
        console.print("[bold red]Error:[/] Neither GCP_PROJECT_ID nor AWS configuration (AWS_REGION/AWS_PROFILE) found. At least one cloud provider must be configured.")
        exit(1)
    
    console.print(f"Using LLM Provider: {current_llm_provider}")
    console.print(f"GCP Project ID (if configured): {config_example.get('gcp_project_id')}")
    console.print(f"AWS Region (if configured): {config_example.get('aws_region')}")
    console.print(f"AWS Profile (if configured): {config_example.get('aws_profile')}")
    console.print(f"RAG Docs Path for Init: {config_example['rag_docs_path_for_init']}")
    console.print(f"RAG Embedding Model: {config_example['rag_embedding_model']}")
    console.print(f"RAG Vector Store: {config_example['vector_store_choice']}")
    if config_example['db_config']:
        console.print(f"RAG DB Config: {config_example['db_config']}")
    console.print(f"RAG Build on Init (for this example run): {config_example['rag_build_on_init']}")


    try:
        gcp_executor_instance = GcloudExecutor(config_example)
        aws_executor_instance = AWSExecutor(config_example)
        rag_engine_instance = RAGEngine(
            vector_store_choice=config_example['vector_store_choice'],
            db_config=config_example['db_config'],
            embed_model_name=config_example['rag_embedding_model'],
            google_api_key=config_example.get('google_api_key'), # Pass Google API key
            documents_path_for_init=config_example['rag_docs_path_for_init'],
            build_index_on_init=config_example['rag_build_on_init'],
            llm_for_settings=None 
        )
        
        test_query = "Create a GCP VPC network named my-vpc-`date +%s` and an AWS S3 bucket named my-saturn-test-bucket-`date +%s`."

        if not rag_engine_instance.query_engine:
            console.print("[bold yellow]Warning:[/] RAG query engine not initialized after RAGEngine setup.")
            console.print("For persistent stores (Chroma/DuckDB), ensure you have run 'saturn ingest-docs' first.")
            console.print("For in-memory store, ensure 'rag_docs_path_for_init' is valid and contains documents.")

        console.print(f'Starting orchestrator for query: "{test_query}"') 
        asyncio.run(run_query_with_feedback(
            test_query, 
            config_example,
            rag_engine_instance, 
            verbose=True 
        ))
    except Exception as main_err:
        console.print(f"--- UNHANDLED ERROR IN MAIN --- ")
        console.print_exception(show_locals=True) 