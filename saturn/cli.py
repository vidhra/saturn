import typer
import os
import asyncio
from typing import Optional
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

# Import from within the saturn package
from .config import load_config
from .orchestrator import run_query_with_feedback # Use the loop version
from .knowledge_base import KnowledgeBase
from .gcp_executor import GcloudExecutor

# Load environment variables from .env file if present
load_dotenv()

# Load base configuration once
APP_CONFIG = load_config()

# Create Typer app
app = typer.Typer()
console = Console()

@app.command("run")
def run_command(
    query: str = typer.Argument(..., help="The natural language query for the GCP agent."),
    provider: Optional[str] = typer.Option(os.getenv("LLM_PROVIDER") or APP_CONFIG.get('llm_provider', "openai"), help="LLM provider (e.g., openai, gemini, claude, mistral"),
    model: Optional[str] = typer.Option(None, help="Specific LLM model name (e.g., gpt-4o). Overrides config."),
    project_id: Optional[str] = typer.Option(os.getenv("GCP_PROJECT_ID") or APP_CONFIG.get('gcp_project_id'), "--project-id", help="Google Cloud Project ID. Overrides config/env."),
    creds_path: Optional[str] = typer.Option(os.getenv("GCP_CREDENTIALS_PATH") or APP_CONFIG.get('gcp_credentials_path'), "--creds-path", help="Path to GCP service account key file (uses ADC if not provided). Overrides config/env."),
    max_retries: Optional[int] = typer.Option(int(os.getenv("MAX_RETRIES") or APP_CONFIG.get('max_retries', 5)), "--max-retries", help="Max retry attempts for the orchestrator loop."),
    kb_path: Optional[str] = typer.Option(os.getenv("KB_PATH") or APP_CONFIG.get('kb_path', "api_defs"), "--kb-path", help="Path to the knowledge base API definitions."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output, including full exception tracebacks.")
):
    """Runs the Saturn orchestrator with the specified query and configuration."""
    
    console.print(Panel(f"Processing query: '[bold cyan]{query}[/bold cyan]'", title="Saturn Command"))

    # --- Assemble final config, prioritizing CLI > Env > Loaded Config --- 
    config = APP_CONFIG.copy() # Start with base config

    # Apply overrides from CLI options / Env Vars handled by Typer defaults
    config['llm_provider'] = provider
    if model:
        config[f'{provider}_model'] = model
    if project_id:
        config['gcp_project_id'] = project_id
    if creds_path:
        config['gcp_credentials_path'] = creds_path
    config['max_retries'] = max_retries
    # kb_path is used directly below
    
    # --- Validation --- 
    if not config.get('gcp_project_id'):
        console.print("[bold red]Error:[/] GCP Project ID not found. Set GCP_PROJECT_ID environment variable, use --project-id argument, or add to config file.")
        raise typer.Exit(code=1)
        
    required_api_key_name = f'{config["llm_provider"]}_api_key'
    # Ensure API keys are present in the config (they should be loaded by load_config)
    if not config.get(required_api_key_name):
        console.print(f"[bold red]Error:[/] {required_api_key_name.upper()} not found in config or environment for provider '{config['llm_provider']}'.")
        raise typer.Exit(code=1)
    
    console.print("--- Initializing Saturn Agent ---")
    console.print(f"Using LLM Provider: {config['llm_provider']}")
    if config.get(f'{provider}_model'):
        console.print(f"Using Model: {config.get(f'{provider}_model')}")
    console.print(f"Target GCP Project: {config['gcp_project_id']}")
    console.print(f"Knowledge Base Path: {kb_path}")

    # --- Initialize Components & Run --- 
    try:
        # Initialize components (KnowledgeBase, GcloudExecutor, LLMInterface)
        console.print("Initializing components...")
        kb_path = config.get('knowledge_base_path', 'api_defs')
        kb = KnowledgeBase(kb_path) # KB is still initialized for other potential uses or if re-added
        executor = GcloudExecutor(config)
        # LLM Interface is now initialized directly within run_query_with_feedback
        console.print("Components initialized.")

        console.print("--- Starting Orchestrator ---")
        asyncio.run(run_query_with_feedback(query, config, executor, config.get('max_retries', 5), verbose))

    except FileNotFoundError:
        console.print(f"[bold red]ERROR:[/] Knowledge Base directory '{kb_path}' not found.")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[bold red]\n--- An unexpected error occurred --- [/bold red]")
        console.print_exception(show_locals=False)
        raise typer.Exit(code=1)

# Optional: Add other commands if needed
# @app.command("config")
# def show_config(): ...

if __name__ == "__main__":
    app() # Allow running this file directly for testing 