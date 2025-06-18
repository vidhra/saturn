import contextlib
import io
import json
from typing import Any, Dict, Optional

from rich.console import Console
from rich.panel import Panel

from internal.state_machine_runner import StateMachineRunner
from model.llm.base_interface import get_llm_interface
from saturn.prompts import (ERROR_SUMMARY_PROMPT, OPERATION_COMPLETED_PROMPT,
                            PLAN_SUMMARY_PROMPT, SYSTEM_CHAT_PROMPT)

from .aws_executor import AWSExecutor
from .gcp_executor import GcloudExecutor
from .knowledge_base import KnowledgeBase
from .rag_engine import RAGEngine

console = Console()


async def run_query_with_state_machine(
    query: str,
    config: Dict[str, Any],
    rag_engine: RAGEngine,
    max_total_attempts: int = 5,
    verbose: bool = False,
) -> None:
    console.print(
        Panel(
            f"Processing Query: [cyan]{query}[/cyan]",
            title="[bold blue]Saturn Orchestrator (State Machine)[/bold blue]",
            border_style="blue",
        )
    )

    gcp_executor_instance: Optional[GcloudExecutor] = None
    aws_executor_instance: Optional[AWSExecutor] = None

    if config.get("gcp_project_id"):
        gcp_executor_instance = GcloudExecutor(config)
        console.print("GCP Executor initialized.")
    if config.get("aws_region") or config.get("aws_profile"):
        aws_executor_instance = AWSExecutor(config)
        console.print("AWS Executor initialized.")
    if not gcp_executor_instance and not aws_executor_instance:
        console.print(
            "[bold red]Error:[/] No cloud executor could be initialized. Check GCP/AWS configurations."
        )
        return

    try:
        llm_interface = get_llm_interface(config)
        console.print("LLM interface initialized.")
    except (ValueError, RuntimeError) as e:
        console.print(f"[bold red]Error:[/] Failed initializing LLM interface: {e}")
        return

    knowledge_base = KnowledgeBase(
        api_defs_dir=config.get("api_defs_dir", "./internal/api_definitions"),
        working_directory=config.get("working_directory", "."),
    )
    console.print(
        f"Knowledge Base initialized with {knowledge_base.get_tool_counts()['total_tools']} total tools."
    )

    system_prompt = "You are a cloud infrastructure orchestrator. Generate step-by-step plans for cloud operations and file management tasks."

    runner = StateMachineRunner(
        llm_interface=llm_interface,
        gcp_executor=gcp_executor_instance,
        aws_executor=aws_executor_instance,
        knowledge_base=knowledge_base,
        system_prompt=system_prompt,
        config={
            "max_retries": max_total_attempts,
            "working_directory": config.get("working_directory", "."),
        },
        console=console,
        rag_engine=rag_engine,
    )

    final_context = await runner.process_query(query)

    if final_context.current_errors:
        console.print(
            f"[bold red]Orchestration completed with {len(final_context.current_errors)} errors.[/bold red]"
        )
        if verbose:
            for i, error in enumerate(final_context.current_errors):
                console.print(f"  Error {i+1}: {error}")
    else:
        console.print("[bold green]Orchestration completed successfully![/bold green]")

    console.print("Orchestrator finished using state machine approach.")


async def run_query_with_feedback(
    query: str,
    config: Dict[str, Any],
    rag_engine: RAGEngine,
    max_total_attempts: int = 5,
    verbose: bool = False,
) -> None:
    await run_query_with_state_machine(
        query, config, rag_engine, max_total_attempts, verbose
    )


async def summarize_history(llm_interface, history):
    summary_prompt = "Summarize the following conversation, focusing on user goals, assistant plans, results, and feedback:\n\n"
    for role, message in history:
        summary_prompt += f"{role}: {message}\n"
    summary_prompt += "\nSummary:"
    response = await llm_interface.agenerate(
        [{"role": "user", "content": summary_prompt}]
    )
    return response.choices[0].message.content.strip()


async def run_chat_conversational(config, user_input_stream):
    """
    Conversational agent backend for UI frontends (Textual, CLI, etc).
    Accepts an async generator of user inputs, and yields (role, message) tuples for each turn.
    """
    rag_engine_instance = RAGEngine(
        config=config,
        vector_store_choice=config["vector_store_choice"],
        db_config=config["db_config"],
        embed_model_name=config["rag_embedding_model"],
        google_api_key=config.get("google_api_key"),
        documents_path_for_init=(
            config["rag_docs_path_for_init"]
            if config["vector_store_choice"] == "default"
            else None
        ),
        build_index_on_init=config["rag_build_on_init"],
        llm_for_settings=None,
        hyde_llm=get_llm_interface(config),
        hyde_similarity_top_k=5,
        use_hyde=True,
        device="auto",
        parallel_process=True,
        embed_batch_size=32,
        preserve_code_blocks=True,
        preserve_command_context=True,
    )
    runner = StateMachineRunner(
        llm_interface=get_llm_interface(config),
        gcp_executor=GcloudExecutor(config),
        aws_executor=AWSExecutor(config),
        knowledge_base=None,
        system_prompt=SYSTEM_CHAT_PROMPT,
        config={
            "max_retries": config.get("max_retries", 5),
            "working_directory": config.get("working_directory", "."),
        },
        console=console,
        rag_engine=rag_engine_instance,
    )
    transcript = []
    compressed_context = None
    last_captured_output = None
    N = 4
    async for user_input in user_input_stream:
        if user_input.strip().lower() in {"exit", "quit"}:
            yield ("assistant", "[cyan]Goodbye![/cyan]")
            break
        if user_input.strip().lower() == "/trace":
            if last_captured_output:
                yield (
                    "assistant",
                    f"[bold]Execution Output:[/bold]\n\n{last_captured_output}",
                )
            else:
                yield (
                    "assistant",
                    "[yellow]No execution trace available. Run a command first.[/yellow]",
                )
            continue
        transcript.append(("user", user_input))
        prompt = []
        prompt.append({"role": "system", "content": SYSTEM_CHAT_PROMPT})
        if compressed_context:
            prompt.append(
                {
                    "role": "system",
                    "content": f"Summary of previous conversation: {compressed_context}",
                }
            )
        for role, message in transcript:
            prompt.append({"role": role, "content": message})
        prompt.append({"role": "user", "content": user_input})
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            context = await runner.process_query(user_input)
        last_captured_output = buf.getvalue()
        if hasattr(context, "step_details_map") and context.step_details_map:
            plan = [
                f"{i+1}. {step['description']}"
                for i, step in enumerate(context.step_details_map.values())
            ]
            plan_text = "\n".join(plan)
            assistant_msg = PLAN_SUMMARY_PROMPT.format(plan_text=plan_text)
            transcript.append(("assistant", assistant_msg))
            yield ("assistant", assistant_msg)
        if context.current_errors:
            summary = ERROR_SUMMARY_PROMPT.format(
                errors=json.dumps(context.current_errors, indent=2)
            )
            transcript.append(("assistant", summary))
            yield ("assistant", summary)
        else:
            summary_parts = []
            if context.step_outputs:
                summary_parts.append("Completed Steps:")
                for step_id, output in context.step_outputs.items():
                    step_desc = context.step_details_map.get(step_id, {}).get(
                        "description", "Unknown step"
                    )
                    summary_parts.append(f"• {step_desc}")
                    if isinstance(output, str) and output.strip():
                        summary_parts.append(f"  Result: {output.strip()}")
                    elif isinstance(output, dict):
                        if "result" in output:
                            summary_parts.append(f"  Result: {output['result']}")
                        elif "output" in output:
                            summary_parts.append(f"  Output: {output['output']}")
                        elif "error" in output:
                            summary_parts.append(
                                f"  [yellow]Warning: {output['error']}[/yellow]"
                            )
            if context.llm_text_response:
                summary_parts.append(f"\nAdditional Info:\n{context.llm_text_response}")
            summary = (
                "\n".join(summary_parts)
                if summary_parts
                else "Operation completed with no output."
            )
            summary += "\n\n[dim]Use /trace to view detailed execution logs[/dim]"
            assistant_msg = OPERATION_COMPLETED_PROMPT.format(summary=summary)
            transcript.append(("assistant", assistant_msg))
            yield ("assistant", assistant_msg)
        if len(transcript) > 2 * N:
            to_summarize = transcript[:-N]
            compressed_context = await summarize_history(
                runner.llm_interface, to_summarize
            )
            transcript = transcript[-N:]
