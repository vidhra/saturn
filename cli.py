import typer
import os
import asyncio
from typing import Optional, Dict, Any
from rich.console import Console
from rich.panel import Panel

# Import actual components from the package (using the new name 'saturn')
from saturn.config import load_config
# Import the main feedback loop function from the new orchestrator module
from saturn.orchestrator import run_query_with_feedback
from saturn.knowledge_base import KnowledgeBase
from saturn.gcp_executor import GcpExecutor

# Remove Temporary stubs
# async def run_query_with_feedback(...): ...
# def load_config(...): ...

# --- Load Config Once at Module Level ---
# Configuration is loaded when the script starts, using env vars or default config.yaml
# The --config-file option per command is removed for this approach.
APP_CONFIG = load_config() 

# --- CLI Application ---
app = typer.Typer()
console = Console()

@app.command()
def main(
    query: str = typer.Argument(..., help="The natural language query for GCP."),
    # config_file: Optional[str] = typer.Option("config.yaml", "--config-file", help="Path to configuration file."), # Removed: Config loaded globally
    state_file: Optional[str] = typer.Option("gcp_state.json", "--state-file", help="Path to state file (currently unused)."),
    api_defs_dir: Optional[str] = typer.Option("api_defs", "--api-defs-dir", help="Directory containing GCP API definitions."),
    max_attempts: Optional[int] = typer.Option(5, "--max-attempts", help="Maximum retry attempts for API calls."),
    verbose: bool = typer.Option(False, "-v", "--verbose", help="Enable verbose output.")
):
    """Processes a natural language query to interact with GCP APIs."""

    console.print(Panel(f"Processing query: '[bold cyan]{query}[/bold cyan]'", title="GCP Natural Language CLI", expand=False))

    # Use the globally loaded configuration
    config = APP_CONFIG

    if verbose:
        # Avoid printing sensitive keys directly
        printable_config = {k: (v[:5] + '...' if k == 'openai_api_key' and v else v) for k, v in config.items()}
        console.print(f"Using globally loaded configuration: {printable_config}")
        console.print(f"Using state file: {state_file}")
        console.print(f"Using API definitions from: {api_defs_dir}")
        console.print(f"Max attempts: {max_attempts}")

    # Load configuration using the actual function --- This call is removed
    # config = load_config(config_file)
    
    # Check the globally loaded config
    if not config.get('openai_api_key'):
        console.print("[bold red]Error:[/bold red] OpenAI API key not found. Set OPENAI_API_KEY environment variable or add to config file.")
        raise typer.Exit(code=1)
    if not config.get('gcp_project_id'):
        console.print("[bold red]Error:[/bold red] GCP Project ID not found. Set GCP_PROJECT_ID environment variable or add to config file.")
        raise typer.Exit(code=1)

    # --- Initialize components ---
    console.print("Initializing components...")
    try:
        # Instantiate the actual components
        kb = KnowledgeBase(api_defs_dir) 
        executor = GcpExecutor(config) # Pass the globally loaded config
        console.print("Components initialized.")
    except Exception as init_err:
        console.print(f"[bold red]Error initializing components:[/bold red] {init_err}")
        raise typer.Exit(code=1)

    # --- Run the main logic --- 
    console.print("Starting query processing loop...")
    try:
        # Call the actual run_query_with_feedback from openai_interface
        # Pass the real instances and globally loaded config
        asyncio.run(run_query_with_feedback(query, config, kb, executor, max_attempts))
        console.print("[bold green]Processing finished.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]An error occurred during processing:[/bold red] {e}")
        import traceback
        if verbose:
            traceback.print_exc()
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app() 