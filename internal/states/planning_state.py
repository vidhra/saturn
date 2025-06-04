import json
import traceback
from typing import Any, Dict, Tuple, Type

import json_repair
from rich.table import Table

from internal.dag.dag import ORDER_UP, AcyclicGraph, Edge
# Import prompts from orchestrator
from saturn.prompts import PLANNING_SYSTEM_PROMPT_TEMPLATE

from .base_state import BaseState, StateMachineContext
from .executing_state import ExecutingState
from .failed_state import FailedState


class PlanningState(BaseState):
    """State responsible for generating a DAG-based execution plan using LLM."""

    async def run(
        self, context: StateMachineContext
    ) -> Tuple[Type[BaseState], StateMachineContext]:
        print("--- State: PLANNING ---")

        max_attempts = 5
        attempt = 1

        while attempt <= max_attempts:
            print(f"Planning attempt {attempt}/{max_attempts}")

            # Get file build tool names for DAG planning
            from saturn.file_build_tools import FileBuildToolCaller

            file_tool_caller = FileBuildToolCaller(
                context.file_build_executor.config.get("working_directory", ".")
            )
            file_tool_schemas = file_tool_caller.get_tools_schema()
            context.file_tool_names = set(
                [tool["function"]["name"] for tool in file_tool_schemas]
            )

            print(f"Available file tool names: {context.file_tool_names}")
            print(
                f"execute_command in file_tool_names: {'execute_command' in context.file_tool_names}"
            )

            # Generate DAG plan using orchestrator logic
            dag, step_details_map = await self._generate_plan_dag(
                context.original_query,
                context.llm_interface,
                context.state_recorder,
                context.file_tool_names,
                context.console,
                attempt_number=attempt,
            )

            if not dag or not step_details_map:
                print("Failed to generate a valid execution plan.")
                context.current_errors.append(
                    {
                        "method": "PLANNING",
                        "error": "Failed to generate DAG plan",
                        "arguments": {"query": context.original_query},
                    }
                )
                return FailedState, context

            # Store DAG information in context
            context.dag = dag
            context.step_details_map = step_details_map

            try:
                context.execution_order = dag.topo_order(ORDER_UP)
                print(f"DAG Execution Order: {' -> '.join(context.execution_order)}")
            except Exception as e:
                error_msg = f"Failed to get execution order from DAG: {e}"
                print(f"Error: {error_msg}")
                context.current_errors.append(
                    {"method": "PLANNING", "error": error_msg, "arguments": {}}
                )
                return FailedState, context

            context.state_recorder.record_event(
                "plan_generation_success",
                {
                    "dag_nodes": len(dag.vertices),
                    "dag_edges": len(dag.edges),
                    "execution_order": context.execution_order,
                },
            )

            print("Planning completed successfully. Transitioning to EXECUTING.")
            return ExecutingState, context

    async def _generate_plan_dag(
        self,
        user_query: str,
        llm_interface,
        state_logger,
        file_tool_names: set,
        console,
        attempt_number: int,
    ) -> Tuple[Any, Dict[str, Any]]:
        """
        Calls the LLM to generate a multi-step plan and constructs a DAG.
        Returns a tuple of (AcyclicGraph, Dict_of_step_details) or (None, None) on failure.
        """
        if console:
            console.print(
                f"Generating execution plan for query: [cyan]{user_query}[/cyan]"
            )

        state_logger.record_event("plan_generation_start", {"query": user_query})

        # Create tools list for the prompt
        available_file_tools = ", ".join(sorted(file_tool_names))
        available_cloud_tools = (
            "cli_command_generation (for gcp and aws cloud operations)"
        )

        planning_prompt = PLANNING_SYSTEM_PROMPT_TEMPLATE.format(
            user_query=user_query,
            available_file_tools=available_file_tools,
            available_cloud_tools=available_cloud_tools,
        )

        try:
            response = await llm_interface.agenerate(
                [
                    {"role": "system", "content": "You are a planning assistant."},
                    {"role": "user", "content": planning_prompt},
                ]
            )
            try:
                choice = response.choices[0]
                message = getattr(choice, "message", None)
                if message is None:
                    raise ValueError(
                        "No 'message' attribute in response. Full response: {}".format(
                            response
                        )
                    )
                content = getattr(message, "content", None)
                if not isinstance(content, str):
                    raise ValueError(
                        f"Expected string content, got {type(content)}. Content: {content}"
                    )
                raw_plan_str = content.strip()
                if console:
                    console.print(f"Raw plan: {raw_plan_str}")
            except Exception as e:
                if console:
                    console.print(
                        f"[bold red]Error extracting plan from LLM response:[/bold red] {e}"
                    )
                    console.print(f"[dim]Full response object: {response}[/dim]")
                raw_plan_str = None

            if raw_plan_str is None:
                error_msg = "LLM returned an empty plan."
                if console:
                    console.print(f"[bold red]Error:[/] {error_msg}")
                state_logger.record_event(
                    "plan_generation_failed",
                    {"error": error_msg, "raw_response": raw_plan_str},
                )
                return None, None

            try:
                plan_steps = json.loads(raw_plan_str)
            except json.JSONDecodeError:
                if console:
                    console.print(
                        "[yellow]Initial JSON parsing failed, trying json_repair...[/yellow]"
                    )
                try:
                    plan_steps = json_repair.loads(raw_plan_str)
                except Exception as repair_err:
                    error_msg = (
                        f"Failed to parse plan JSON even with json_repair: {repair_err}"
                    )
                    if console:
                        console.print(f"[bold red]Error:[/] {error_msg}")
                    state_logger.record_event(
                        "plan_generation_failed",
                        {"error": error_msg, "raw_response": raw_plan_str},
                    )
                    return None, None

            if not isinstance(plan_steps, list):
                error_msg = "LLM plan is not a list of steps."
                if console:
                    console.print(f"[bold red]Error:[/] {error_msg}")
                state_logger.record_event(
                    "plan_generation_failed",
                    {"error": error_msg, "parsed_plan": plan_steps},
                )
                return None, None

            # Display plan in rich table
            if console:
                plan_display_table = Table(
                    title="LLM Generated Plan",
                    show_header=True,
                    header_style="bold blue",
                )
                plan_display_table.add_column("Step ID", style="cyan", no_wrap=True)
                plan_display_table.add_column("Provider", style="green")
                plan_display_table.add_column("Description", style="white")
                plan_display_table.add_column("Dependencies", style="yellow")
                plan_display_table.add_column("Pass Output", style="magenta")

                if not plan_steps:
                    console.print("[yellow]LLM returned an empty plan.[/yellow]")
                else:
                    for i, step_data in enumerate(plan_steps):
                        if isinstance(step_data, dict):
                            step_id_disp = step_data.get(
                                "id", f"Step {i+1} (ID missing)"
                            )
                            tool_to_use = step_data.get("tool_to_use", "")
                            cloud_provider_val = step_data.get("cloud_provider")
                            if (
                                not cloud_provider_val
                                and tool_to_use in file_tool_names
                            ):
                                provider_disp = "FILE"
                            elif (
                                isinstance(cloud_provider_val, str)
                                and cloud_provider_val
                            ):
                                provider_disp = cloud_provider_val.upper()
                            else:
                                provider_disp = "N/A"
                                console.print(
                                    f"[yellow]Warning: Step {step_id_disp} is missing a valid cloud_provider and is not a file/build step. Step: {step_data}[/yellow]"
                                )
                            description_disp = step_data.get("description", "N/A")
                            dependencies_disp = (
                                ", ".join(step_data.get("dependencies", [])) or "-"
                            )
                            pass_output_disp = str(
                                step_data.get("pass_output_to_next", "True")
                            )
                            plan_display_table.add_row(
                                step_id_disp,
                                provider_disp,
                                description_disp,
                                dependencies_disp,
                                pass_output_disp,
                            )
                        else:
                            plan_display_table.add_row(
                                f"Step {i+1}",
                                "N/A",
                                "Invalid step data format",
                                "-",
                                "-",
                            )
                    console.print(plan_display_table)

            dag = AcyclicGraph()
            step_details_map = {}
            step_ids = set()

            for step in plan_steps:
                tool_to_use = step.get("tool_to_use", "")
                cloud_provider = step.get("cloud_provider")
                if console:
                    console.print(
                        f"[dim]DEBUG: Validating step {step.get('id')} with tool '{tool_to_use}', cloud_provider: {cloud_provider}[/dim]"
                    )
                    console.print(
                        f"[dim]DEBUG: file_tool_names = {file_tool_names}[/dim]"
                    )
                if not cloud_provider and tool_to_use in file_tool_names:
                    # File/build step, allow
                    pass
                elif not cloud_provider and tool_to_use == "cli_command_generation":
                    # cli_command_generation without cloud provider is invalid, should use execute_command instead
                    error_msg = f"Step {step.get('id')} uses 'cli_command_generation' without a cloud_provider. For command execution, use 'execute_command' instead."
                    if console:
                        console.print(f"[bold red]Error:[/] {error_msg}")
                    state_logger.record_event(
                        "plan_generation_failed",
                        {"error": error_msg, "plan_steps": plan_steps},
                    )
                    return None, None
                elif not cloud_provider and tool_to_use not in file_tool_names:
                    # Invalid file tool name - suggest corrections
                    suggestions = []
                    if "analyze" in tool_to_use or "project" in tool_to_use:
                        suggestions.append("detect_project_type")
                    if "dockerfile" in tool_to_use or "docker" in tool_to_use:
                        suggestions.append("generate_dockerfile")
                    if "write" in tool_to_use or "file" in tool_to_use:
                        suggestions.append("write_file")

                    suggestion_text = (
                        f" Did you mean: {', '.join(suggestions)}?"
                        if suggestions
                        else ""
                    )
                    error_msg = f"Step {step.get('id')} uses invalid tool '{tool_to_use}'. Available file tools: {', '.join(sorted(file_tool_names))}.{suggestion_text}"
                    if console:
                        console.print(f"[bold red]Error:[/] {error_msg}")
                    state_logger.record_event(
                        "plan_generation_failed",
                        {
                            "error": error_msg,
                            "plan_steps": plan_steps,
                            "available_tools": list(file_tool_names),
                        },
                    )
                    return None, None
                elif not isinstance(cloud_provider, str) or not cloud_provider:
                    error_msg = f"Step {step.get('id')} is missing a valid cloud_provider and is not a file/build step."
                    if console:
                        console.print(f"[bold red]Error:[/] {error_msg}")
                    state_logger.record_event(
                        "plan_generation_failed",
                        {"error": error_msg, "plan_steps": plan_steps},
                    )
                    return None, None
                if step.get("cloud_provider") and step["cloud_provider"] not in [
                    "gcp",
                    "aws",
                ]:
                    error_msg = f"Invalid cloud_provider '{step['cloud_provider']}' in step {step['id']}. Must be 'gcp' or 'aws'."
                    if console:
                        console.print(f"[bold red]Error:[/] {error_msg}")
                    state_logger.record_event(
                        "plan_generation_failed",
                        {"error": error_msg, "plan_steps": plan_steps},
                    )
                    return None, None
                step_id = step["id"]
                if step_id in step_ids:
                    error_msg = f"Duplicate step ID found in plan: {step_id}"
                    if console:
                        console.print(f"[bold red]Error:[/] {error_msg}")
                    state_logger.record_event(
                        "plan_generation_failed",
                        {"error": error_msg, "plan_steps": plan_steps},
                    )
                    return None, None
                step_ids.add(step_id)
                dag.add(step_id)
                step_details_map[step_id] = {
                    "id": step_id,
                    "description": step.get("description", ""),
                    "cloud_provider": step.get("cloud_provider"),
                    "dependencies": step.get("dependencies", []),
                    "tool_to_use": step.get("tool_to_use", "cli_command_generation"),
                    "tool_args": step.get("tool_args", {}),
                    "pass_output_to_next": step.get("pass_output_to_next", True),
                }

            for step_id_key, details in step_details_map.items():
                for dep_id in details.get("dependencies", []):
                    if dep_id not in step_details_map:
                        error_msg = f"Dependency '{dep_id}' for step '{step_id_key}' not found in plan."
                        if console:
                            console.print(f"[bold red]Error:[/] {error_msg}")
                        state_logger.record_event(
                            "plan_generation_failed",
                            {"error": error_msg, "plan_steps": plan_steps},
                        )
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
                        "pass_output_to_next": s_details.get("pass_output_to_next"),
                    }

                state_logger.record_dag_structure(
                    {
                        "nodes": dag_nodes_for_log,
                        "edges": [str(e) for e in dag.edges],
                        "execution_order": execution_order,
                    }
                )
                # Initialize all planned nodes in the logger
                for step_id_to_init, details_to_init in step_details_map.items():
                    state_logger.record_node_initialization(
                        node_id=step_id_to_init,
                        tool_name=details_to_init.get(
                            "tool_to_use", "cli_command_generation"
                        ),
                        attempt=0,
                        args={"cloud_provider": details_to_init.get("cloud_provider")},
                        initial_status="PLANNED",
                    )

                if console:
                    console.print(
                        f"Plan generated successfully. DAG has {len(dag.vertices)} nodes and {len(dag.edges)} edges."
                    )
                    console.print(f"Execution order: {' -> '.join(execution_order)}")
                return dag, step_details_map
            except Exception as dag_err:
                error_msg = f"DAG validation failed: {dag_err}"
                if console:
                    console.print(f"[bold red]Error:[/] {error_msg}")
                state_logger.record_event(
                    "plan_generation_failed",
                    {"error": error_msg, "plan_steps": plan_steps},
                )
                return None, None

        except Exception as e:
            error_msg = f"Error during plan generation: {str(e)}"
            if console:
                console.print(f"[bold red]Error:[/] {error_msg}")
            if hasattr(e, "response") and hasattr(e.response, "text"):
                error_msg += f" LLM Response: {e.response.text}"
            state_logger.record_event(
                "plan_generation_failed",
                {"error": error_msg, "traceback": traceback.format_exc()},
            )
            return None, None
