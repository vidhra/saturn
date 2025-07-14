import asyncio
import json
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
    """
    Parse a command string to extract the command and its arguments.
    Handles both JSON format and plain string commands.
    """
    command_string = command_string.strip()

    if command_string.startswith("{") and command_string.endswith("}"):
        try:
            parsed = json.loads(command_string)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            pass

    return {"command": command_string}


class ExecutingState(BaseState):
    """State responsible for executing DAG steps with parallel execution support."""

    async def run(
        self, context: StateMachineContext
    ) -> Tuple[Type[BaseState], StateMachineContext]:

        if not context.dag or not context.step_details_map:
            context.current_errors.append(
                {
                    "method": "EXECUTING",
                    "error": "No DAG or step details available",
                    "arguments": {},
                }
            )
            return FailedState, context

        console = context.console
        parallel_execution = context.config.get("parallel_execution", True)
        max_parallel_tasks = context.config.get("max_parallel_tasks", 3)

        if parallel_execution:
            return await self._execute_parallel(context, console, max_parallel_tasks)
        else:
            return await self._execute_sequential(context, console)

    async def _execute_parallel(
        self, context: StateMachineContext, console, max_parallel_tasks: int
    ):
        """Execute DAG steps in parallel where possible."""
        if console:
            console.print(
                f"[cyan]Executing DAG with parallel execution (max {max_parallel_tasks} concurrent tasks)[/cyan]"
            )

        completed_nodes = set()
        failed_nodes = set()  # Track failed nodes to prevent infinite loops
        all_steps_succeeded = True
        accumulated_errors = []
        
        # Circuit breaker to detect infinite loops
        consecutive_failed_rounds = 0
        max_failed_rounds = 3  # Allow 3 rounds of all failures before giving up
        last_ready_nodes = set()

        while len(completed_nodes) + len(failed_nodes) < len(context.step_details_map):
            # Get immediately ready nodes, excluding both completed and failed nodes
            ready_nodes = context.dag.get_immediately_ready_nodes(completed_nodes)
            ready_nodes = ready_nodes - failed_nodes  # Exclude failed nodes

            if not ready_nodes:
                # Check if we're stuck (circular dependency or other issue)
                remaining_nodes = set(context.step_details_map.keys()) - completed_nodes - failed_nodes
                if remaining_nodes:
                    error_msg = f"No nodes are ready to execute, but {len(remaining_nodes)} remain: {remaining_nodes}"
                    if console:
                        console.print(f"[bold red]Error: {error_msg}[/bold red]")
                    accumulated_errors.append({"error": error_msg})
                    all_steps_succeeded = False
                break

            # Circuit breaker: if we're trying the same nodes repeatedly and they keep failing
            if ready_nodes == last_ready_nodes and consecutive_failed_rounds >= max_failed_rounds:
                error_msg = f"Circuit breaker triggered: Same nodes failing repeatedly ({consecutive_failed_rounds} rounds). Stopping execution to prevent infinite loop."
                if console:
                    console.print(f"[bold red]Error: {error_msg}[/bold red]")
                    console.print(f"[red]Problematic nodes: {', '.join(ready_nodes)}[/red]")
                accumulated_errors.append({"error": error_msg, "problematic_nodes": list(ready_nodes)})
                all_steps_succeeded = False
                break

            # Limit parallel execution
            ready_nodes_list = list(ready_nodes)[:max_parallel_tasks]

            if console:
                if len(ready_nodes_list) > 1:
                    console.print(
                        f"[yellow]Executing {len(ready_nodes_list)} steps in parallel: {', '.join(ready_nodes_list)}[/yellow]"
                    )
                else:
                    console.print(f"[blue]Executing step: {ready_nodes_list[0]}[/blue]")

            # Execute ready nodes in parallel
            tasks = []
            for step_id in ready_nodes_list:
                task = self._execute_single_step(step_id, context, console)
                tasks.append(task)

            # Wait for all parallel tasks to complete
            round_had_failures = False
            try:
                results = await asyncio.gather(*tasks, return_exceptions=True)

                # Process results
                for i, (step_id, result) in enumerate(zip(ready_nodes_list, results)):
                    if isinstance(result, Exception):
                        if console:
                            console.print(
                                f"[bold red]Step {step_id} failed with exception: {result}[/bold red]"
                            )
                        accumulated_errors.append(
                            {"step_id": step_id, "error": str(result)}
                        )
                        all_steps_succeeded = False
                        context.step_outputs[step_id] = {"error": str(result)}
                        failed_nodes.add(step_id)  # Mark as failed to prevent retry
                        round_had_failures = True
                    else:
                        step_success, step_result = result
                        context.step_outputs[step_id] = step_result

                        if step_success:
                            completed_nodes.add(step_id)
                            if console:
                                console.print(
                                    f"[green]✓ Step {step_id} completed successfully[/green]"
                                )
                        else:
                            if console:
                                console.print(
                                    f"[bold red]✗ Step {step_id} failed[/bold red]"
                                )
                            accumulated_errors.append(
                                {
                                    "step_id": step_id,
                                    "error": step_result.get("error", "Unknown error"),
                                }
                            )
                            all_steps_succeeded = False
                            failed_nodes.add(step_id)  # Mark as failed to prevent retry
                            round_had_failures = True

            except Exception as e:
                if console:
                    console.print(
                        f"[bold red]Error in execution: {e}[/bold red]"
                    )
                accumulated_errors.append({"error": f" execution error: {e}"})
                all_steps_succeeded = False
                round_had_failures = True
                break

            # Update circuit breaker state
            if round_had_failures and ready_nodes == last_ready_nodes:
                consecutive_failed_rounds += 1
            else:
                consecutive_failed_rounds = 0
            last_ready_nodes = ready_nodes.copy()

            # Early termination on critical failures
            if accumulated_errors and context.config.get("fail_fast", False):
                if console:
                    console.print(
                        "[bold red]Fail-fast mode: Stopping execution due to errors[/bold red]"
                    )
                break

            # Additional safety check: if we have failed nodes and no more can be executed
            if failed_nodes and not ready_nodes:
                remaining_nodes = set(context.step_details_map.keys()) - completed_nodes - failed_nodes
                if not remaining_nodes:  # All nodes are either completed or failed
                    if console:
                        console.print(
                            f"[yellow]Execution complete: {len(completed_nodes)} succeeded, {len(failed_nodes)} failed[/yellow]"
                        )
                    break

        return await self._process_execution_results(
            context, console, all_steps_succeeded, accumulated_errors
        )

    async def _execute_sequential(self, context: StateMachineContext, console):
        """Execute DAG steps sequentially (original behavior)."""
        if not context.execution_order:
            context.current_errors.append(
                {
                    "method": "EXECUTING",
                    "error": "No execution order available",
                    "arguments": {},
                }
            )
            return FailedState, context

        if console:
            console.print(
                f"Executing DAG with {len(context.execution_order)} steps in order: {' -> '.join(context.execution_order)}"
            )

        all_steps_succeeded = True
        accumulated_errors = []

        for step_id in context.execution_order:
            if step_id not in context.step_details_map:
                error_msg = f"Step ID '{step_id}' from execution order not found in step details. Skipping."
                accumulated_errors.append(
                    {"step_id": step_id, "error": "Step details not found"}
                )
                all_steps_succeeded = False
                break

            step_success, step_result = await self._execute_single_step(
                step_id, context, console
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

        return await self._process_execution_results(
            context, console, all_steps_succeeded, accumulated_errors
        )

    async def _execute_single_step(
        self, step_id: str, context: StateMachineContext, console
    ) -> Tuple[bool, Any]:
        """Execute a single step and return success status and result."""
        current_step_details = context.step_details_map[step_id]

        # Collect dependency outputs
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

        tool_to_use = current_step_details.get("tool_to_use")
        cloud_provider = current_step_details.get("cloud_provider")

        # Route to appropriate execution method
        # Check if this is a loaded workflow with stored commands for any tool type
        if getattr(context, 'is_loaded_workflow', False) and current_step_details.get('executed_command'):
            return await self._execute_stored_command(
                step_id, current_step_details, context, console
            )
        elif tool_to_use.startswith("mcp_"):
            return await self._execute_mcp_tool_step(
                step_id, current_step_details, context, console
            )
        elif tool_to_use in [tool["name"] for tool in context.file_tools] or (
            cloud_provider is None or str(cloud_provider).lower() == "none"
        ):
            return await self._execute_file_tool_step(
                step_id, current_step_details, context, console
            )
        else:
            return await self._execute_dag_step(
                step_id, current_step_details, context, contextual_outputs, console
            )

    async def _process_execution_results(
        self, context, console, all_steps_succeeded, accumulated_errors
    ):
        """Process the final results of execution."""
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
                
                # Show summary of failed steps
                if accumulated_errors:
                    console.print("\n[bold red]Failed Steps Summary:[/bold red]")
                    for error in accumulated_errors:
                        if "step_id" in error:
                            console.print(f"  • {error['step_id']}: {error.get('error', 'Unknown error')}")
                        else:
                            console.print(f"  • {error.get('error', 'Unknown error')}")
                            
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
        max_attempts: int = 3,
    ) -> Tuple[bool, Any]:
        """Execute a file build tool step with error feedback and retry."""
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

        attempt = 0
        last_error = None
        while attempt < max_attempts:
            attempt += 1
            if console:
                console.print(
                    f"Attempt {attempt}/{max_attempts} for file tool step [cyan]{step_id}[/cyan]"
                )
            try:
                result = await context.file_build_executor.execute(
                    tool_to_use, tool_args, console, f"exec_{tool_to_use}"
                )
                success = (
                    result[0]
                    if isinstance(result, tuple)
                    else result.get("success", False)
                )
                actual_result = result[1] if isinstance(result, tuple) else result

                context.state_recorder.record_node_result(
                    step_id,
                    success,
                    actual_result,
                    "COMPLETED_FILE_TOOL" if success else "FAILED_FILE_TOOL",
                )

                if success:
                    if console:
                        console.print(
                            f"[green]File tool step {step_id} completed successfully.[/green]"
                        )
                    
                    # Store the successful file tool call in step details for .sat file generation
                    if step_id in context.step_details_map:
                        file_command = f"file_tool: {tool_to_use} with args: {tool_args}"
                        context.step_details_map[step_id]["executed_command"] = file_command
                        context.step_details_map[step_id]["execution_successful"] = True
                        context.step_details_map[step_id]["file_tool_name"] = tool_to_use
                        context.step_details_map[step_id]["file_tool_args"] = tool_args
                    
                    return True, actual_result
                else:
                    error_msg = (
                        actual_result.get("error", "Unknown error")
                        if isinstance(actual_result, dict)
                        else str(actual_result)
                    )
                    last_error = error_msg
                    if console:
                        console.print(
                            f"[bold red]File tool step {step_id} failed (Attempt {attempt}): {error_msg}[/bold red]"
                        )

            except Exception as file_exc:
                last_error = f"Exception during file tool step {step_id}: {file_exc}"
                if console:
                    console.print(f"[bold red]{last_error}[/bold red]")
                context.state_recorder.record_node_result(
                    step_id, False, {"error": last_error}, "FAILED_FILE_TOOL_EXCEPTION"
                )

        if console:
            console.print(
                f"[bold red]File tool step {step_id} failed after {max_attempts} attempts.[/bold red]"
            )
        return False, {"error": last_error or "Unknown error", "step_id": step_id}

    async def _execute_mcp_tool_step(
        self,
        step_id: str,
        step_details: Dict[str, Any],
        context: StateMachineContext,
        console,
        max_attempts: int = 3,
    ) -> Tuple[bool, Any]:
        """Execute an MCP tool step with error feedback and retry."""
        tool_to_use = step_details.get("tool_to_use")
        tool_args = step_details.get("tool_args", {})

        if console:
            console.print(
                Panel(
                    f"[MCP Tool] Executing MCP tool: [cyan]{tool_to_use}[/cyan] with args: {tool_args}",
                    title=f"Step: {step_id}",
                    border_style="purple",
                )
            )

        # Check if MCP integrator is available
        if not hasattr(context, "mcp_integrator") or not context.mcp_integrator:
            error_msg = "MCP integrator not available"
            if console:
                console.print(
                    f"[bold red]MCP tool step {step_id} failed: {error_msg}[/bold red]"
                )
            context.state_recorder.record_node_result(
                step_id, False, {"error": error_msg}, "FAILED_MCP_TOOL"
            )
            return False, {"error": error_msg}

        attempt = 0
        last_error = None
        while attempt < max_attempts:
            attempt += 1
            if console:
                console.print(
                    f"Attempt {attempt}/{max_attempts} for MCP tool step [cyan]{step_id}[/cyan]"
                )
            try:
                result = await context.mcp_integrator.call_tool(tool_to_use, tool_args)
                success = result.get("success", False)

                context.state_recorder.record_node_result(
                    step_id,
                    success,
                    result,
                    "COMPLETED_MCP_TOOL" if success else "FAILED_MCP_TOOL",
                )

                if success:
                    if console:
                        console.print(
                            f"[green]MCP tool step {step_id} completed successfully.[/green]"
                        )

                        # Display the actual MCP tool result
                        if result and "result" in result:
                            mcp_result = result["result"]
                            if "content" in mcp_result and mcp_result["content"]:
                                result_text = ""
                                for content_item in mcp_result["content"]:
                                    if content_item.get("type") == "text":
                                        result_text += content_item.get("text", "")

                                if result_text:
                                    console.print(
                                        Panel(
                                            result_text,
                                            title=f"MCP Tool Result: {step_id}",
                                            title_align="left",
                                            border_style="green",
                                        )
                                    )
                                else:
                                    console.print(
                                        f"[dim]No text content in MCP result for {step_id}[/dim]"
                                    )
                            else:
                                console.print(
                                    f"[dim]No content in MCP result for {step_id}[/dim]"
                                )
                        else:
                            console.print(
                                f"[dim]No result data from MCP tool {step_id}[/dim]"
                            )
                    
                    # Store the successful MCP tool call in step details for .sat file generation
                    if step_id in context.step_details_map:
                        mcp_command = f"mcp_tool: {tool_to_use} with args: {tool_args}"
                        context.step_details_map[step_id]["executed_command"] = mcp_command
                        context.step_details_map[step_id]["execution_successful"] = True
                        context.step_details_map[step_id]["mcp_tool_name"] = tool_to_use
                        context.step_details_map[step_id]["mcp_tool_args"] = tool_args
                    
                    return True, result
                else:
                    error_msg = result.get("error", "Unknown MCP error")
                    last_error = error_msg
                    if console:
                        console.print(
                            f"[bold red]MCP tool step {step_id} failed (Attempt {attempt}): {error_msg}[/bold red]"
                        )

                        # Also show the actual error content if available
                        if result and "result" in result:
                            mcp_result = result["result"]
                            if "content" in mcp_result and mcp_result["content"]:
                                error_text = ""
                                for content_item in mcp_result["content"]:
                                    if content_item.get("type") == "text":
                                        error_text += content_item.get("text", "")

                                if error_text:
                                    console.print(
                                        Panel(
                                            error_text,
                                            title=f"MCP Error Details: {step_id}",
                                            title_align="left",
                                            border_style="red",
                                        )
                                    )

            except Exception as mcp_exc:
                last_error = f"Exception during MCP tool step {step_id}: {mcp_exc}"
                if console:
                    console.print(f"[bold red]{last_error}[/bold red]")
                context.state_recorder.record_node_result(
                    step_id, False, {"error": last_error}, "FAILED_MCP_TOOL_EXCEPTION"
                )

        if console:
            console.print(
                f"[bold red]MCP tool step {step_id} failed after {max_attempts} attempts.[/bold red]"
            )
        return False, {"error": last_error}

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
        For loaded workflows (.sat files), uses stored commands directly.
        Otherwise, generates a cloud command using LLM, executes it, and handles retries.
        """
        
        # Check if this is a loaded workflow with stored commands
        if getattr(context, 'is_loaded_workflow', False) and step_details.get('executed_command'):
            return await self._execute_stored_command(
                step_id, step_details, context, console
            )
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
                    
                    # Store the successful command in step details for .sat file generation
                    if step_id in context.step_details_map:
                        context.step_details_map[step_id]["executed_command"] = command_to_execute
                        context.step_details_map[step_id]["execution_successful"] = True
                    
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

    async def _execute_stored_command(
        self,
        step_id: str,
        step_details: Dict[str, Any],
        context: StateMachineContext,
        console,
    ) -> Tuple[bool, Any]:
        """
        Execute a stored command from a loaded .sat workflow file.
        This bypasses LLM generation and uses the exact command that was successful before.
        """
        if console:
            console.print(
                Panel(
                    f"Executing Stored Command for Step: [cyan]{step_id}[/cyan]\n"
                    f"Description: {step_details.get('description', 'N/A')}\n"
                    f"[dim]Using stored command from .sat file[/dim]",
                    title="[bold green]Stored Command Execution[/bold green]",
                    border_style="green",
                )
            )

        context.state_recorder.record_event(
            "stored_command_execution_start",
            {"step_id": step_id, "description": step_details.get("description")},
        )
        context.state_recorder.record_node_status_change(step_id, "RUNNING")

        stored_command = step_details.get("executed_command")
        cloud_provider = step_details.get("cloud_provider")

        try:
            # Handle different types of stored commands
            if step_details.get("mcp_tool_name"):
                # This is an MCP tool execution
                tool_name = step_details.get("mcp_tool_name")
                tool_args = step_details.get("mcp_tool_args", {})
                
                if console:
                    console.print(f"[cyan]Executing stored MCP tool: {tool_name}[/cyan]")
                    console.print(f"[dim]Arguments: {tool_args}[/dim]")
                
                if not hasattr(context, "mcp_integrator") or not context.mcp_integrator:
                    error_msg = "MCP integrator not available for stored MCP command"
                    if console:
                        console.print(f"[bold red]Error: {error_msg}[/bold red]")
                    context.state_recorder.record_node_result(
                        step_id, False, {"error": error_msg}, "FAILED_STORED_MCP"
                    )
                    return False, {"error": error_msg}
                
                result = await context.mcp_integrator.call_tool(tool_name, tool_args)
                success = result.get("success", False)
                
                context.state_recorder.record_node_result(
                    step_id, success, result, "COMPLETED_STORED_MCP" if success else "FAILED_STORED_MCP"
                )
                
                if success:
                    if console:
                        console.print(f"[green]✓ Stored MCP command executed successfully[/green]")
                    return True, result
                else:
                    error_msg = result.get("error", "Unknown MCP error")
                    if console:
                        console.print(f"[bold red]✗ Stored MCP command failed: {error_msg}[/bold red]")
                    return False, {"error": error_msg}
                    
            elif step_details.get("file_tool_name"):
                # This is a file tool execution
                tool_name = step_details.get("file_tool_name")
                tool_args = step_details.get("file_tool_args", {})
                
                if console:
                    console.print(f"[cyan]Executing stored file tool: {tool_name}[/cyan]")
                    console.print(f"[dim]Arguments: {tool_args}[/dim]")
                
                result = await context.file_build_executor.execute(
                    tool_name, tool_args, console, f"stored_{tool_name}"
                )
                success = (
                    result[0] if isinstance(result, tuple) else result.get("success", False)
                )
                actual_result = result[1] if isinstance(result, tuple) else result
                
                context.state_recorder.record_node_result(
                    step_id, success, actual_result, "COMPLETED_STORED_FILE" if success else "FAILED_STORED_FILE"
                )
                
                if success:
                    if console:
                        console.print(f"[green]✓ Stored file tool executed successfully[/green]")
                    return True, actual_result
                else:
                    error_msg = (
                        actual_result.get("error", "Unknown error")
                        if isinstance(actual_result, dict)
                        else str(actual_result)
                    )
                    if console:
                        console.print(f"[bold red]✗ Stored file tool failed: {error_msg}[/bold red]")
                    return False, {"error": error_msg}
                    
            elif cloud_provider in ["gcp", "aws"]:
                # This is a cloud CLI command
                if console:
                    console.print(f"[cyan]Executing stored {cloud_provider.upper()} command:[/cyan]")
                    console.print(f"[bold]{stored_command}[/bold]")
                
                # Validate cloud provider executor availability
                if cloud_provider == "gcp" and not context.gcp_executor:
                    error_msg = f"GCP Executor not available for stored command: {step_id}"
                    if console:
                        console.print(f"[bold red]Error: {error_msg}[/bold red]")
                    context.state_recorder.record_node_result(
                        step_id, False, {"error": error_msg}, "FAILED_STORED_EXECUTOR_MISSING"
                    )
                    return False, {"error": error_msg}
                elif cloud_provider == "aws" and not context.aws_executor:
                    error_msg = f"AWS Executor not available for stored command: {step_id}"
                    if console:
                        console.print(f"[bold red]Error: {error_msg}[/bold red]")
                    context.state_recorder.record_node_result(
                        step_id, False, {"error": error_msg}, "FAILED_STORED_EXECUTOR_MISSING"
                    )
                    return False, {"error": error_msg}
                
                # Execute the stored command
                if cloud_provider == "gcp":
                    success, result_or_error = await context.gcp_executor.execute(
                        stored_command, console, f"stored_{step_id}"
                    )
                elif cloud_provider == "aws":
                    success, result_or_error = await context.aws_executor.execute(
                        stored_command, console, f"stored_{step_id}"
                    )
                
                if success:
                    if console:
                        console.print(f"[green]✓ Stored {cloud_provider.upper()} command executed successfully[/green]")
                        
                        if isinstance(result_or_error, str) and result_or_error.strip():
                            console.print(
                                Panel(
                                    result_or_error,
                                    title=f"Result for Step: {step_id}",
                                    title_align="left",
                                    border_style="green",
                                )
                            )
                    
                    context.state_recorder.record_node_result(
                        step_id, True, {"result": result_or_error, "executed_command_str": stored_command}, "COMPLETED_STORED_SUCCESS"
                    )
                    return True, result_or_error
                else:
                    error_msg = str(result_or_error)
                    if console:
                        console.print(f"[bold red]✗ Stored {cloud_provider.upper()} command failed: {error_msg}[/bold red]")
                    
                    context.state_recorder.record_node_result(
                        step_id, False, {"error": error_msg, "executed_command_str": stored_command}, "FAILED_STORED_COMMAND"
                    )
                    return False, {"error": error_msg}
            else:
                error_msg = f"Unknown stored command type for step {step_id}: {stored_command}"
                if console:
                    console.print(f"[bold red]Error: {error_msg}[/bold red]")
                context.state_recorder.record_node_result(
                    step_id, False, {"error": error_msg}, "FAILED_STORED_UNKNOWN_TYPE"
                )
                return False, {"error": error_msg}
                
        except Exception as e:
            error_msg = f"Exception during stored command execution for {step_id}: {str(e)}"
            if console:
                console.print(f"[bold red]{error_msg}[/bold red]")
            context.state_recorder.record_node_result(
                step_id, False, {"error": error_msg}, "FAILED_STORED_EXCEPTION"
            )
            return False, {"error": error_msg}

    def _build_dependency_map(self, dag):
        dep_map = {}
        for edge in dag.edges:
            if edge.target not in dep_map:
                dep_map[edge.target] = []
            dep_map[edge.target].append(edge.source)
        return dep_map
