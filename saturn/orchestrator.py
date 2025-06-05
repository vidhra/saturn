from typing import Any, Dict, Optional

from rich.console import Console
from rich.panel import Panel

from internal.state_machine_runner import StateMachineRunner
from model.llm.base_interface import get_llm_interface

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
