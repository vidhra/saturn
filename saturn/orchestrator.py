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
    async for user_input in user_input_stream:
        if user_input.strip().lower() in {"exit", "quit"}:
            yield ("assistant", "[cyan]Goodbye![/cyan]")
            break
        transcript.append(("user", user_input))
        yield ("user", user_input)
        context = await runner.process_query(user_input)
        if hasattr(context, "step_details_map") and context.step_details_map:
            plan = [
                f"{i+1}. {step['description']}"
                for i, step in enumerate(context.step_details_map.values())
            ]
            plan_text = "\n".join(plan)
            assistant_msg = PLAN_SUMMARY_PROMPT.format(plan_text=plan_text)
            transcript.append(("assistant", assistant_msg))
            yield ("assistant", assistant_msg)
            # In a real UI, prompt for feedback here
            # For now, just continue
        if context.current_errors:
            summary = ERROR_SUMMARY_PROMPT.format(errors=context.current_errors)
            transcript.append(("assistant", summary))
            yield ("assistant", summary)
        else:
            summary = OPERATION_COMPLETED_PROMPT
            transcript.append(("assistant", summary))
            yield ("assistant", summary)
