import json
import shlex
import traceback
from typing import Any, Dict, Tuple, Type

from rich.panel import Panel
from rich.table import Table

from saturn.prompts import (AWS_STEP_ERROR_HANDLING_PROMPT_TEMPLATE,
                            AWS_STEP_SYSTEM_PROMPT_TEMPLATE,
                            GCLOUD_STEP_ERROR_HANDLING_PROMPT_TEMPLATE,
                            GCLOUD_STEP_SYSTEM_PROMPT_TEMPLATE)

from .base_state import BaseState, StateMachineContext
from .completed_state import CompletedState
from .failed_state import FailedState


def _parse_command(command_string: str) -> Dict[str, Any]:
    """Parses a gcloud command string into a structured dictionary using shlex."""
    parsed_command: Dict[str, Any] = {
        "original_command": command_string,
        "base_command": "",
        "subcommands": [],
        "flags": {},
        "positional_args": [],
        "parsing_error": None,
    }

    try:
        tokens = shlex.split(command_string)

        if not tokens:
            parsed_command["parsing_error"] = "Empty command string"
            return parsed_command

        if tokens[0] not in ["gcloud", "aws"]:
            parsed_command["parsing_error"] = (
                f"Command does not start with gcloud or aws: {tokens[0]}"
            )
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
                elif idx + 1 < len(tokens) and not tokens[idx + 1].startswith("-"):
                    parsed_command["flags"][flag_name] = tokens[idx + 1]
                    idx += 2
                else:
                    parsed_command["flags"][flag_name] = True  # Boolean flag
                    idx += 1
            elif token.startswith("-") and not token.startswith("--"):
                if "=" in token:
                    name, value = token.split("=", 1)
                    parsed_command["flags"][name] = value
                    idx += 1
                elif (
                    len(token) == 2
                    and idx + 1 < len(tokens)
                    and not tokens[idx + 1].startswith("-")
                ):
                    parsed_command["flags"][token] = tokens[idx + 1]
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


class ExecutingState(BaseState):
    """State responsible for executing DAG steps in topological order."""

    async def run(
        self, context: StateMachineContext
    ) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: EXECUTING ---")

        if not context.dag or not context.step_details_map:
            print("No DAG or step details available for execution.")
            context.current_errors.append(
                {
                    "method": "EXECUTING",
                    "error": "No DAG or step details available",
                    "arguments": {},
                }
            )
            return FailedState, context

        if not context.execution_order:
            print("No execution order available.")
            context.current_errors.append(
                {
                    "method": "EXECUTING",
                    "error": "No execution order available",
                    "arguments": {},
                }
            )
            return FailedState, context

        console = context.console
        if console:
            console.print(
                f"Executing DAG with {len(context.execution_order)} steps in order: {' -> '.join(context.execution_order)}"
            )

        all_steps_succeeded = True
        accumulated_errors = []

        for step_id in context.execution_order:
            if step_id not in context.step_details_map:
                error_msg = f"Step ID '{step_id}' from execution order not found in step details. Skipping."
                print(f"Error: {error_msg}")
                accumulated_errors.append(
                    {"step_id": step_id, "error": "Step details not found"}
                )
                all_steps_succeeded = False
                break

            current_step_details = context.step_details_map[step_id]

            step_dependencies = [
                edge.source for edge in context.dag.edges if edge.target == step_id
            ]
            contextual_outputs = {}
            for dep_id in step_dependencies:
                if dep_id in context.step_outputs:
                    dep_details = context.step_details_map.get(dep_id, {})
                    if dep_details.get("pass_output_to_next", True):
                        if (
                            isinstance(context.step_outputs[dep_id], dict)
                            and "error" in context.step_outputs[dep_id]
                        ):
                            dep_error_info = context.step_outputs[dep_id]["error"]
                            if console:
                                console.print(
                                    f"[yellow]Warning: Dependency '{dep_id}' (marked to pass output) for step '{step_id}' failed. Its error was: {dep_error_info}. Passing error as context.[/yellow]"
                                )
                            contextual_outputs[dep_id] = {
                                "status": "FAILED",
                                "output": dep_error_info,
                            }
                        else:
                            contextual_outputs[dep_id] = {
                                "status": "SUCCESS",
                                "output": context.step_outputs[dep_id],
                            }
                elif (
                    dep_id in context.step_details_map
                    and not context.step_details_map[dep_id].get(
                        "pass_output_to_next", True
                    )
                ):
                    if console:
                        console.print(
                            f"[info]Output of dependency '{dep_id}' for step '{step_id}' was not passed as per 'pass_output_to_next' flag.[/info]"
                        )

            tool_to_use = current_step_details.get("tool_to_use")
            cloud_provider = current_step_details.get("cloud_provider")

            if tool_to_use in [tool["name"] for tool in context.file_tools] or (
                cloud_provider is None or str(cloud_provider).lower() == "none"
            ):
                step_success, step_result = await self._execute_file_tool_step(
                    step_id, current_step_details, context, console
                )
            else:
                step_success, step_result = await self._execute_dag_step(
                    step_id, current_step_details, context, contextual_outputs, console
                )

            context.step_outputs[step_id] = step_result

            if not step_success:
                if console:
                    console.print(
                        f"[bold red]Step {step_id} ultimately failed. Halting further execution.[/bold red]"
                    )
                all_steps_succeeded = False
                if isinstance(step_result, dict) and "error" in step_result:
                    accumulated_errors.append(
                        {"step_id": step_id, "error": step_result["error"]}
                    )
                else:
                    accumulated_errors.append(
                        {"step_id": step_id, "error": str(step_result)}
                    )
                break

        if all_steps_succeeded and not accumulated_errors:
            if console:
                console.print(
                    Panel(
                        "[bold green]All steps completed successfully![/bold green]",
                        border_style="green",
                    )
                )
            context.state_recorder.set_final_run_status("COMPLETED_SUCCESSFULLY", [])
            return CompletedState, context
        else:
            if console:
                console.print(
                    Panel(
                        "[bold red]Execution failed. See errors above or in logs.[/bold red]",
                        border_style="red",
                    )
                )
            context.current_errors.extend(accumulated_errors)
            context.state_recorder.set_final_run_status(
                "FAILED_AT_STEP", accumulated_errors
            )
            return FailedState, context

    async def _execute_file_tool_step(
        self,
        step_id: str,
        step_details: Dict[str, Any],
        context: StateMachineContext,
        console,
    ) -> Tuple[bool, Any]:
        """Execute a file build tool step."""
        tool_to_use = step_details.get("tool_to_use")
        tool_args = step_details.get("tool_args", {})

        if console:
            console.print(
                Panel(
                    f"[File Tool] Executing file tool: [cyan]{tool_to_use}[/cyan] with args: {tool_args}",
                    title=f"Step: {step_id}",
                    border_style="blue",
                )
            )

        try:
            result = await context.file_build_executor.execute(
                tool_to_use, tool_args, console, f"exec_{tool_to_use}"
            )
            success = (
                result[0] if isinstance(result, tuple) else result.get("success", False)
            )
            actual_result = result[1] if isinstance(result, tuple) else result

            context.state_recorder.record_node_result(
                step_id,
                success,
                actual_result,
                "COMPLETED_FILE_TOOL" if success else "FAILED_FILE_TOOL",
            )

            if not success:
                error_msg = (
                    actual_result.get("error", "Unknown error")
                    if isinstance(actual_result, dict)
                    else str(actual_result)
                )
                if console:
                    console.print(
                        f"[bold red]File tool step {step_id} failed: {error_msg}[/bold red]"
                    )
                return False, {"error": error_msg, "step_id": step_id}
            else:
                if console:
                    console.print(
                        f"[green]File tool step {step_id} completed successfully.[/green]"
                    )
                return True, actual_result

        except Exception as file_exc:
            error_msg = f"Exception during file tool step {step_id}: {file_exc}"
            if console:
                console.print(f"[bold red]{error_msg}[/bold red]")
            context.state_recorder.record_node_result(
                step_id, False, {"error": error_msg}, "FAILED_FILE_TOOL_EXCEPTION"
            )
            return False, {"error": error_msg, "step_id": step_id}

    async def _execute_dag_step(
        self,
        step_id: str,
        step_details: Dict[str, Any],
        context: StateMachineContext,
        previous_step_outputs: Dict[str, Any],
        console,
        max_attempts: int = 3,
    ) -> Tuple[bool, Any]:
        """
        Executes a single step from the DAG using the orchestrator's logic.
        Generates a cloud command using LLM, executes it, and handles retries.
        """
        if console:
            console.print(
                Panel(
                    f"Executing Step: [cyan]{step_id}[/cyan] - {step_details.get('description', 'N/A')}",
                    title="[bold blue]Step Execution[/bold blue]",
                )
            )

        context.state_recorder.record_event(
            "step_execution_start",
            {"step_id": step_id, "description": step_details.get("description")},
        )
        context.state_recorder.record_node_status_change(step_id, "RUNNING")

        cloud_provider = step_details.get("cloud_provider")

        # Set up provider-specific variables
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
            if not context.gcp_executor:
                error_msg = f"GCP Executor not available for GCP step: {step_id}"
                if console:
                    console.print(f"[bold red]Error:[/] {error_msg}")
                context.state_recorder.record_node_result(
                    step_id, False, {"error": error_msg}, "FAILED_EXECUTOR_MISSING"
                )
                return False, {"error": error_msg, "step_id": step_id}
        elif cloud_provider == "aws":
            cli_name = "aws"
            system_prompt_template = AWS_STEP_SYSTEM_PROMPT_TEMPLATE
            error_prompt_template = AWS_STEP_ERROR_HANDLING_PROMPT_TEMPLATE
            doc_context_key = "aws_docs"
            provider_full_name = "Amazon Web Services (AWS)"
            if not context.aws_executor:
                error_msg = f"AWS Executor not available for AWS step: {step_id}"
                if console:
                    console.print(f"[bold red]Error:[/] {error_msg}")
                context.state_recorder.record_node_result(
                    step_id, False, {"error": error_msg}, "FAILED_EXECUTOR_MISSING"
                )
                return False, {"error": error_msg, "step_id": step_id}
        else:
            error_msg = f"Unknown cloud provider '{cloud_provider}' for step {step_id}."
            if console:
                console.print(f"[bold red]Error:[/] {error_msg}")
            context.state_recorder.record_node_result(
                step_id, False, {"error": error_msg}, "FAILED_UNKNOWN_PROVIDER"
            )
            return False, {"error": error_msg, "step_id": step_id}

        context_str = "Context from previous steps (if any):\n"
        if previous_step_outputs:
            for prev_step_id, output_info in previous_step_outputs.items():
                if isinstance(output_info, dict):
                    status = output_info.get("status", "UNKNOWN")
                    actual_output = output_info.get("output", "No output available")
                    context_str += f"- Output of step '{prev_step_id}' (Status: {status}): {json.dumps(actual_output, indent=2)}\n"
                else:
                    context_str += f"- Output of step '{prev_step_id}': {json.dumps(output_info, indent=2)}\n"
        else:
            context_str += "No outputs from previous steps available.\n"

        current_step_description = step_details.get(
            "description", "No description provided for this step."
        )

        rag_query_for_docs = (
            f"{provider_full_name} {cli_name} {current_step_description}"
        )
        cli_docs_context = "No specific documentation found by RAG."
        if context.rag_engine and context.rag_engine.query_engine:
            if console:
                console.print(
                    f"[RAG] Fetching docs for: '{rag_query_for_docs[:100]}...'"
                )
            cli_docs_context = await context.rag_engine.query_docs(rag_query_for_docs)
        elif not context.rag_engine:
            if console:
                console.print(
                    "[yellow]Warning: RAG engine instance not provided to step execution.[/yellow]"
                )
                cli_docs_context = f"Generic {provider_full_name} {cli_name} documentation context will be used."
        else:
            if console:
                console.print(
                    "[yellow]Warning: RAG engine query_engine not initialized. Using generic doc context.[/yellow]"
                )
                if hasattr(
                    context.rag_engine, "vector_store_choice"
                ) and context.rag_engine.vector_store_choice in ["chroma", "duckdb"]:
                    console.print(
                        f"[yellow]Hint: Run 'saturn ingest-docs --provider {cloud_provider}' to build the index for better documentation support.[/yellow]"
                    )
            cli_docs_context = f"Generic {provider_full_name} {cli_name} documentation context will be used. For better results, please run 'saturn ingest-docs --provider {cloud_provider}' to build the RAG index."

        attempt = 0
        last_error = ""
        command_to_execute = ""
        parsed_command_for_log: Dict[str, Any] = {}

        while attempt < max_attempts:
            attempt += 1
            if console:
                console.print(
                    f"Attempt {attempt}/{max_attempts} for step [cyan]{step_id}[/cyan] ({cloud_provider.upper()})"
                )
            context.state_recorder.record_event(
                "step_attempt", {"step_id": step_id, "attempt_number": attempt}
            )

            try:
                prompt_args = {
                    "step_id": step_id,
                    "step_description": current_step_description,
                    "context_from_previous_steps": context_str,
                    doc_context_key: cli_docs_context,
                }
                current_prompt_template_to_use = ""

                if attempt == 1:
                    current_prompt_template_to_use = system_prompt_template
                else:
                    current_prompt_template_to_use = error_prompt_template
                    prompt_args["previous_command"] = command_to_execute
                    prompt_args["error_message"] = last_error

                user_content = current_prompt_template_to_use.format(**prompt_args)

                response = await context.llm_interface.agenerate(
                    [
                        {
                            "role": "system",
                            "content": f"You are a {cli_name} CLI expert for {provider_full_name}.",
                        },
                        {"role": "user", "content": user_content},
                    ]
                )
                command_to_execute = response.choices[0].message.content.strip()

                command_to_execute = (
                    command_to_execute.replace("`", "").replace("\n", " ").strip()
                )

                if not command_to_execute:
                    if console:
                        console.print(
                            "[yellow]Warning: LLM generated an empty command. Skipping execution for this attempt.[/yellow]"
                        )
                    last_error = "LLM generated an empty command."
                    context.state_recorder.record_event(
                        "step_attempt_failed_empty_command",
                        {"step_id": step_id, "attempt": attempt},
                    )
                    if attempt >= max_attempts:
                        parsed_command_for_log = (
                            _parse_command(command_to_execute)
                            if command_to_execute
                            else {"original_command": "EMPTY"}
                        )
                        context.state_recorder.record_node_result(
                            step_id,
                            False,
                            {
                                "error": last_error,
                                "parsed_command": parsed_command_for_log,
                            },
                            "FAILED_EMPTY_COMMAND",
                        )
                        return False, {"error": last_error, "step_id": step_id}
                    continue

                parsed_command_for_log = _parse_command(command_to_execute)

                if console:
                    display_table = Table(
                        title=f"Command for Step: {step_id} ({cloud_provider.upper()}) (Attempt {attempt})",
                        show_header=True,
                        header_style="bold magenta",
                    )
                    display_table.add_column("Component", style="dim")
                    display_table.add_column("Details")

                    if parsed_command_for_log.get("base_command"):
                        display_table.add_row(
                            "Base", parsed_command_for_log["base_command"]
                        )

                    if parsed_command_for_log.get("flags"):
                        flags_display_list = []
                        for k, v in parsed_command_for_log["flags"].items():
                            display_key = k.lstrip("-")
                            flags_display_list.append(f"{display_key}: {v}")
                        flags_str = "\n".join(flags_display_list)
                        display_table.add_row("Flags", flags_str)
                    if parsed_command_for_log.get("positional_args"):
                        display_table.add_row(
                            "Positional Args",
                            ", ".join(parsed_command_for_log["positional_args"]),
                        )
                    if parsed_command_for_log.get("parsing_error"):
                        display_table.add_row(
                            "Parsing Error",
                            parsed_command_for_log["parsing_error"],
                            style="red",
                        )

                    console.print(display_table)

                # Execute the command
                if cloud_provider == "gcp":
                    success, result_or_error = await context.gcp_executor.execute(
                        command_to_execute, console, step_id
                    )
                elif cloud_provider == "aws":
                    success, result_or_error = await context.aws_executor.execute(
                        command_to_execute, console, step_id
                    )

                if success:
                    if console:
                        console.print(
                            f"[bold green]Step {step_id} ({cloud_provider.upper()}) executed successfully![/bold green]"
                        )

                        if isinstance(result_or_error, str) and result_or_error.strip():
                            console.print(
                                Panel(
                                    result_or_error,
                                    title=f"Result for Step: {step_id}",
                                    title_align="left",
                                    border_style="green",
                                )
                            )
                        elif result_or_error:
                            console.print(
                                Panel(
                                    str(result_or_error),
                                    title=f"Result for Step: {step_id}",
                                    title_align="left",
                                    border_style="green",
                                )
                            )

                    success_payload = {
                        "result": result_or_error,
                        "executed_command_str": command_to_execute,
                    }
                    context.state_recorder.record_node_result(
                        step_id, True, success_payload, "COMPLETED_SUCCESS"
                    )
                    return True, result_or_error
                else:
                    last_error = str(result_or_error)
                    if console:
                        console.print(
                            f"[bold red]Command for step {step_id} ({cloud_provider.upper()}) failed (Attempt {attempt}):[/bold red] {last_error}"
                        )

            except Exception as e:
                last_error = (
                    f"Exception during step {step_id} attempt {attempt}: {str(e)}"
                )
                if console:
                    console.print(f"[bold red]{last_error}[/bold red]")
                context.state_recorder.record_event(
                    "step_execution_exception_attempt",
                    {
                        "step_id": step_id,
                        "attempt": attempt,
                        "error": last_error,
                        "traceback": traceback.format_exc(),
                    },
                )
                if command_to_execute:
                    last_error += f"\nFailing command was: `{command_to_execute}`"

        if console:
            console.print(
                f"[bold red]Step {step_id} ({cloud_provider.upper()}) failed after {max_attempts} attempts.[/bold red]"
            )
        context.state_recorder.record_node_result(
            step_id,
            False,
            {
                "error": last_error,
                "final_attempt_command_str": command_to_execute,
                "parsed_command": parsed_command_for_log,
            },
            "FAILED_MAX_ATTEMPTS",
        )
        return False, {"error": last_error, "step_id": step_id}
