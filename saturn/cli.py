import asyncio
import os
import time
from pathlib import Path
from typing import Optional

import typer

try:
    from dotenv import load_dotenv

    env_file_paths = [
        Path(".env"),
        Path(".env-temp"),
        Path("../.env"),
    ]

    env_loaded = False
    for env_path in env_file_paths:
        if env_path.exists():
            load_dotenv(env_path)
            env_loaded = True
            break

    if not env_loaded:
        print("⚠️  [CLI] No .env file found. Using system environment variables only.")

except ImportError:
    print(
        "⚠️  [CLI] python-dotenv not installed. Using system environment variables only."
    )
    print("   [CLI] Install with: pip install python-dotenv")

from rich.console import Console
from rich.panel import Panel

from .config import load_config
from .orchestrator import run_query_with_state_machine
from .rag_engine import (DEFAULT_CHROMA_COLLECTION, DEFAULT_CHROMA_PATH,
                         DEFAULT_DUCKDB_DB_FILE_NAME, DEFAULT_DUCKDB_PATH,
                         DEFAULT_DUCKDB_TABLE_NAME, DEFAULT_EMBED_MODEL_NAME,
                         RAGEngine)

APP_CONFIG = load_config()

app = typer.Typer(
    help="Saturn AI Assistant - Cloud Infrastructure Automation",
    add_completion=False,
    no_args_is_help=False,  # Allow running without arguments
)
console = Console()


def print_env_status_cli():
    """Print the status of key environment variables for CLI debugging."""

    env_vars = {
        "OPENAI_API_KEY": "OpenAI",
        "ANTHROPIC_API_KEY": "Claude",
        "GEMINI_API_KEY": "Gemini",
        "MISTRAL_API_KEY": "Mistral",
        "GOOGLE_API_KEY": "Google (Embeddings)",
        "GCP_PROJECT_ID": "GCP Project",
        "AWS_REGION": "AWS Region",
        "VECTOR_STORE": "Vector Store",
    }

    for env_var, description in env_vars.items():
        value = os.getenv(env_var)
        if value:
            if "key" in env_var.lower() or "api" in env_var.lower():
                masked_value = (
                    f"{value[:8]}...{value[-4:]}"
                    if len(value) > 12
                    else f"{value[:4]}..."
                )
            else:
                masked_value = value
            console.print(f"✅ {description:15} ({env_var}): {masked_value}")
        else:
            console.print(f"❌ {description:15} ({env_var}): Not set")
    console.print("-" * 50)


@app.callback(invoke_without_command=True)
def main(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", "-v", help="Show version and exit"),
    help_commands: bool = typer.Option(False, "--help-commands", help="Show available commands"),
):
    """
    Saturn AI Assistant - Cloud Infrastructure Automation
    
    Run 'saturn' to launch the interactive UI.
    Use 'saturn --help-commands' to see all available commands.
    """
    
    if version:
        console.print("[bold blue]Saturn AI Assistant[/bold blue] version 1.0.0")
        console.print("Cloud Infrastructure Automation Tool")
        raise typer.Exit()
    
    if help_commands:
        console.print("[bold blue]Saturn Commands:[/bold blue]")
        console.print("  [cyan]saturn[/cyan]              Launch interactive UI (default)")
        console.print("  [cyan]saturn run[/cyan]          Execute a query or .sat workflow file")
        console.print("  [cyan]saturn workflow[/cyan]     Manage .sat workflow files (list/validate/info)")
        console.print("  [cyan]saturn ingest-docs[/cyan]  Build RAG documentation index") 
        console.print("  [cyan]saturn terraform-run[/cyan] Terraform-focused execution")
        console.print("  [cyan]saturn hybrid-run[/cyan]   Hybrid gcloud/terraform execution")
        console.print("  [cyan]saturn convert-history[/cyan] Convert execution logs to Terraform")
        console.print("  [cyan]saturn install-cli[/cyan]  Install cloud CLI tools")
        console.print("  [cyan]saturn cache[/cyan]        Manage performance caches")
        console.print("\nUse 'saturn <command> --help' for detailed command help.")
        console.print("\n[bold blue]Saturn Workflow (.sat) Files:[/bold blue]")
        console.print("  • Workflows are automatically saved after successful planning")
        console.print("  • Run workflows: [cyan]saturn run example.sat[/cyan]")
        console.print("  • List workflows: [cyan]saturn workflow list[/cyan]")
        console.print("  • View workflow: [cyan]saturn workflow info --path example.sat[/cyan]")
        raise typer.Exit()
    
    # If no subcommand provided, launch UI by default
    if ctx.invoked_subcommand is None:
        try:
            from saturn.ui.saturn_app import run
            console.print("[bold blue]🚀 Launching Saturn AI Assistant...[/bold blue]")
            run()
        except KeyboardInterrupt:
            console.print("\n[cyan]Saturn terminated by user.[/cyan]")
        except Exception as e:
            console.print(f"[bold red]Error launching Saturn: {e}[/bold red]")
            console.print("Use 'saturn --help-commands' to see other available commands.")
            raise typer.Exit(code=1)


@app.command("run")
def run_command(
    query: str = typer.Argument(
        ..., help="The natural language query for the GCP agent, or path to a .sat workflow file."
    ),
    provider: Optional[str] = typer.Option(
        os.getenv("LLM_PROVIDER") or APP_CONFIG.get("llm_provider", "openai"),
        help="LLM provider (e.g., openai, gemini, claude, mistral",
    ),
    model: Optional[str] = typer.Option(
        None, help="Specific LLM model name (e.g., gpt-4o). Overrides config."
    ),
    project_id: Optional[str] = typer.Option(
        os.getenv("GCP_PROJECT_ID") or APP_CONFIG.get("gcp_project_id"),
        "--project-id",
        help="Google Cloud Project ID. Overrides config/env.",
    ),
    creds_path: Optional[str] = typer.Option(
        os.getenv("GCP_CREDENTIALS_PATH") or APP_CONFIG.get("gcp_credentials_path"),
        "--creds-path",
        help="Path to GCP service account key file (uses ADC if not provided). Overrides config/env.",
    ),
    max_retries: Optional[int] = typer.Option(
        int(os.getenv("MAX_RETRIES") or APP_CONFIG.get("max_retries", 5)),
        "--max-retries",
        help="Max retry attempts for the orchestrator loop.",
    ),
    execution_mode: Optional[str] = typer.Option(
        "manual",
        "--execution-mode",
        help="Execution mode: auto (default), yolo (auto-execute without prompts), manual (ask for confirmation on create/update/delete only)",
    ),
    cloud_provider: Optional[str] = typer.Option(
        "gcp",
        "--cloud-provider",
        help="Cloud provider for RAG database collection: gcp or aws. Defaults to gcp.",
    ),
    rag_docs_path: Optional[str] = typer.Option(
        os.getenv("GCLOUD_DOCS_PATH")
        or APP_CONFIG.get(
            "rag_docs_path",
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "internal",
                "tools",
                "gcloud_online_docs_markdown",
            ),
        ),
        "--rag-docs-path",
        help="Path to Markdown documents for RAG.",
    ),
    vector_store_cli: Optional[str] = typer.Option(
        None,
        "--vector-store",
        help="Vector store type: default (in-memory), chroma, duckdb. Overrides env and config.yaml.",
    ),
    db_path: Optional[str] = typer.Option(
        None,
        "--db-path",
        help="Path for persistent DB (e.g., ./db/chroma_store or ./db/duckdb_store/vector_store.duckdb).",
    ),
    db_collection_or_table: Optional[str] = typer.Option(
        None,
        "--db-collection-table",
        help="Collection name (Chroma) or Table name (DuckDB).",
    ),
    rag_embed_model: Optional[str] = typer.Option(
        os.getenv("RAG_EMBED_MODEL")
        or APP_CONFIG.get("rag_embedding_model", DEFAULT_EMBED_MODEL_NAME),
        "--rag-embed-model",
        help="RAG embedding model name.",
    ),
    google_api_key_cli: Optional[str] = typer.Option(
        None,
        "--google-api-key",
        help="Google API Key for Gemini Embeddings. Overrides GOOGLE_API_KEY env var.",
    ),
    show_env: bool = typer.Option(
        False, "--show-env", help="Show environment variable status for debugging."
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output, including full exception tracebacks.",
    ),
):
    """Runs the Saturn orchestrator with the specified query and configuration."""

    if show_env:
        print_env_status_cli()

    if execution_mode not in ["auto", "yolo", "manual"]:
        console.print(
            f"[bold red]Error:[/] Invalid execution mode '{execution_mode}'. Use: auto, yolo, or manual"
        )
        raise typer.Exit(code=1)

    # Check if query is a .sat file
    is_sat_file = query.endswith('.sat') and os.path.exists(query)
    
    if is_sat_file:
        console.print(
            Panel(
                f"Loading Saturn workflow: '[bold cyan]{query}[/bold cyan]'",
                title="Saturn Workflow Execution",
            )
        )
        # For .sat files, we don't need most of the configuration validation
        # as the workflow contains all necessary step information
    else:
        console.print(
            Panel(
                f"Processing query: '[bold cyan]{query}[/bold cyan]'",
                title="Saturn Command",
            )
        )

    config = APP_CONFIG.copy()
    config["llm_provider"] = provider
    if model:
        config[f"{provider}_model"] = model
    if project_id:
        config["gcp_project_id"] = project_id
    if creds_path:
        config["gcp_credentials_path"] = creds_path
    config["max_retries"] = max_retries
    config["execution_mode"] = execution_mode
    config["rag_docs_path_for_init"] = rag_docs_path
    config["rag_embedding_model"] = rag_embed_model
    config["google_api_key"] = (
        google_api_key_cli
        or os.getenv("GOOGLE_API_KEY")
        or config.get("google_api_key")
    )

    vs_choice_source = "hardcoded default in CLI"
    resolved_vector_store = "default"

    if vector_store_cli:
        resolved_vector_store = vector_store_cli
        vs_choice_source = "CLI option (--vector-store)"
    elif os.getenv("VECTOR_STORE"):
        resolved_vector_store = os.getenv("VECTOR_STORE")
        vs_choice_source = "environment variable (VECTOR_STORE)"
    elif APP_CONFIG.get("vector_store"):
        resolved_vector_store = APP_CONFIG.get("vector_store")
        vs_choice_source = "config.yaml (vector_store key)"

    config["vector_store_choice"] = resolved_vector_store.lower()
    console.print(
        f"[Config] Vector store choice '{config['vector_store_choice']}' determined from: {vs_choice_source}"
    )

    # Use provider-specific database configuration to ensure consistency with ingest-docs
    from .rag_engine import build_provider_db_config

    db_configuration = {}
    if config["vector_store_choice"] == "chroma":
        if db_path or db_collection_or_table:
            db_configuration["chroma_path"] = db_path or DEFAULT_CHROMA_PATH
            db_configuration["chroma_collection_name"] = (
                db_collection_or_table or DEFAULT_CHROMA_COLLECTION
            )
        else:
            db_configuration = build_provider_db_config(
                APP_CONFIG, cloud_provider.lower(), "chroma"
            )
    elif config["vector_store_choice"] == "duckdb":
        if db_path or db_collection_or_table:
            db_dir = (
                os.path.dirname(db_path)
                if db_path and ".duckdb" in db_path
                else (db_path or DEFAULT_DUCKDB_PATH)
            )
            db_file = (
                os.path.basename(db_path)
                if db_path and ".duckdb" in db_path
                else DEFAULT_DUCKDB_DB_FILE_NAME
            )
            db_configuration["duckdb_path"] = db_dir
            db_configuration["duckdb_file_name"] = db_file
            db_configuration["duckdb_table_name"] = (
                db_collection_or_table or DEFAULT_DUCKDB_TABLE_NAME
            )
        else:
            db_configuration = build_provider_db_config(
                APP_CONFIG, cloud_provider.lower(), "duckdb"
            )
    config["db_config"] = db_configuration if db_configuration else None

    config["rag_build_on_init"] = (
        True if config["vector_store_choice"] == "default" else False
    )

    if not config.get("gcp_project_id"):
        console.print("[bold red]Error:[/] GCP Project ID not found.")
        raise typer.Exit(code=1)
    
    # Map LLM providers to their corresponding API key names
    provider_api_key_map = {
        "openai": "openai_api_key",
        "claude": "anthropic_api_key",
        "gemini": "gemini_api_key", 
        "mistral": "mistral_api_key"
    }
    
    provider = config["llm_provider"]
    required_api_key_name = provider_api_key_map.get(provider, f'{provider}_api_key')
    if not config.get(required_api_key_name) and provider != "mock":
        console.print(
            f"[bold red]Error:[/] {required_api_key_name.upper()} not found for provider '{provider}'."
        )
        raise typer.Exit(code=1)

    console.print("--- Initializing Saturn Agent ---")
    console.print(f"Using LLM Provider: {config['llm_provider']}")
    if config.get(f"{provider}_model"):
        console.print(f"Using Model: {config.get(f'{provider}_model')}")
    console.print(f"Target GCP Project: {config['gcp_project_id']}")
    console.print(f"Execution Mode: {execution_mode}")

    if execution_mode == "yolo":
        console.print(
            "[bold green]🚀 YOLO MODE: Commands will auto-execute without confirmation[/bold green]"
        )
    elif execution_mode == "manual":
        console.print(
            "[bold yellow]✋ MANUAL MODE: You will be asked to confirm each command[/bold yellow]"
        )
    else:
        console.print(
            "[blue]🔄 AUTO MODE: Standard execution with progress display[/blue]"
        )

    console.print(f"RAG Vector Store: {config['vector_store_choice']}")
    if config["db_config"]:
        console.print(f"RAG DB Config: {config['db_config']}")
        console.print(
            f"[Info] Using {cloud_provider.upper()} provider-specific database configuration for consistency with 'saturn ingest-docs --provider {cloud_provider}'"
        )
    if config["google_api_key"] and "gemini" in config["rag_embedding_model"]:
        console.print("[Config] GOOGLE_API_KEY will be used for Gemini embeddings.")

    try:
        from model.llm.base_interface import get_llm_interface

        rag_engine_instance = RAGEngine(
            config=APP_CONFIG,
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

        if (
            not rag_engine_instance.query_engine
            and config["vector_store_choice"] != "default"
        ):
            console.print(
                f"[bold yellow]Warning:[/] RAG query engine for '{config['vector_store_choice']}' not ready. Index may need to be ingested first using 'saturn ingest-docs'."
            )
            console.print(
                f"[Info] You can run: saturn ingest-docs --provider {cloud_provider} --vector-store {config['vector_store_choice']}"
            )
        elif (
            not rag_engine_instance.query_engine
            and config["vector_store_choice"] == "default"
        ):
            console.print(
                "[bold yellow]Warning:[/] RAG query engine not initialized. Documentation support will be limited."
            )
            console.print(
                f"[Info] Verify that the RAG docs path exists: {config.get('rag_docs_path_for_init', 'Not specified')}"
            )

        console.print("--- Starting Orchestrator ---")
        asyncio.run(
            run_query_with_state_machine(
                query, config, rag_engine_instance, verbose=verbose, question_handler=cli_question_handler
            )
        )

    except Exception:
        console.print(
            "[bold red]\n--- An unexpected error occurred in 'run' command --- [/bold red]"
        )
        console.print_exception(show_locals=verbose)
        raise typer.Exit(code=1)


@app.command("ingest-docs")
def ingest_docs_command(
    provider: str = typer.Option(
        "gcp", "--provider", help="Cloud provider: gcp or aws"
    ),
    docs_path: Optional[str] = typer.Option(
        None,
        "--docs-path",
        help="Path to Markdown documents to ingest. If not specified, uses provider-specific default path.",
    ),
    vector_store: str = typer.Option(
        os.getenv("VECTOR_STORE") or APP_CONFIG.get("vector_store", "chroma"),
        "--vector-store",
        help="Vector store type: default (in-memory, not persistent for ingest), chroma, duckdb.",
    ),
    rag_embed_model: Optional[str] = typer.Option(
        os.getenv("RAG_EMBED_MODEL")
        or APP_CONFIG.get("rag_embedding_model", DEFAULT_EMBED_MODEL_NAME),
        "--rag-embed-model",
        help="RAG embedding model name.",
    ),
    google_api_key_cli: Optional[str] = typer.Option(
        None,
        "--google-api-key",
        help="Google API Key for Gemini Embeddings. Overrides GOOGLE_API_KEY env var.",
    ),
    show_env: bool = typer.Option(
        False, "--show-env", help="Show environment variable status for debugging."
    ),
    force_rebuild: bool = typer.Option(
        False,
        "--force-rebuild",
        help="Force rebuild of the index, deleting existing data in persistent stores.",
    ),
):
    """Ingests documents into the specified vector store with provider-specific configurations."""

    if show_env:
        print_env_status_cli()

    from .rag_engine import build_provider_db_config, get_provider_docs_path

    provider = provider.lower()
    if provider not in ["gcp", "aws"]:
        console.print(
            f"[bold red]Error:[/] Unsupported provider '{provider}'. Use 'gcp' or 'aws'."
        )
        raise typer.Exit(code=1)

    if not docs_path:
        docs_path = get_provider_docs_path(APP_CONFIG, provider)

    console.print(
        Panel(
            f"Starting {provider.upper()} Document Ingestion for Vector Store: [bold cyan]{vector_store}[/bold cyan]",
            title="Saturn Ingestion",
        )
    )
    console.print(f"Provider: [bold]{provider.upper()}[/bold]")
    console.print(f"Documents path: {docs_path}")

    vs_choice = vector_store.lower()
    if vs_choice == "default":
        console.print(
            "[bold yellow]Warning:[/] 'default' (in-memory) vector store selected. Ingestion will not be persistent. Use 'chroma' or 'duckdb' for persistence."
        )

    db_configuration = build_provider_db_config(APP_CONFIG, provider, vs_choice)

    if vs_choice == "chroma":
        console.print(
            f"[Info] Using ChromaDB with path: '{db_configuration['chroma_path']}' and collection: '{db_configuration['chroma_collection_name']}'"
        )
    elif vs_choice == "duckdb":
        console.print(
            f"[Info] Using DuckDB with path: '{db_configuration['duckdb_path']}/{db_configuration['duckdb_file_name']}' and table: '{db_configuration['duckdb_table_name']}'"
        )

    console.print(f"Database configuration: {db_configuration}")

    effective_google_api_key = (
        google_api_key_cli
        or os.getenv("GOOGLE_API_KEY")
        or APP_CONFIG.get("google_api_key")
    )

    console.print(f"Using Embedding Model: {rag_embed_model}")
    if effective_google_api_key and "gemini" in rag_embed_model.lower():
        console.print("[Config] GOOGLE_API_KEY will be used for Gemini embeddings.")
    elif not effective_google_api_key and "gemini" in rag_embed_model.lower():
        console.print(
            "[bold yellow]Warning:[/] GOOGLE_API_KEY not found but Gemini embedding model specified. This may cause issues."
        )

    try:
        rag_engine_instance = RAGEngine(
            config=APP_CONFIG,
            vector_store_choice=vs_choice,
            db_config=(
                db_configuration if db_configuration else None
            ),  # Pass None if not chroma/duckdb
            embed_model_name=rag_embed_model,
            google_api_key=effective_google_api_key,
            llm_for_settings=None,
            device="auto",
            parallel_process=True,
            use_context_aware_parsing=True,
            embed_batch_size=32,
            preserve_code_blocks=True,
            preserve_command_context=True,
        )

        console.print("Attempting to ingest and build index...")
        success = rag_engine_instance.ingest_and_build_index(
            documents_path=docs_path, force_rebuild=force_rebuild
        )

        if success:
            console.print(
                f"[bold green]Document ingestion and index building completed successfully for '{vs_choice}'![/bold green]"
            )
        else:
            console.print(
                f"[bold red]Document ingestion and index building failed for '{vs_choice}'. Check logs above.[/bold red]"
            )
            raise typer.Exit(code=1)

    except Exception:
        console.print(
            "[bold red]\n--- An unexpected error occurred during 'ingest-docs' command --- [/bold red]"
        )
        console.print_exception(show_locals=False)
        raise typer.Exit(code=1)


@app.command("terraform-run")
def terraform_run_command(
    query: str = typer.Argument(
        ..., help="The natural language query for the Terraform agent."
    ),
    provider: Optional[str] = typer.Option(
        os.getenv("LLM_PROVIDER") or APP_CONFIG.get("llm_provider", "openai"),
        help="LLM provider (e.g., openai, gemini, claude, mistral",
    ),
    model: Optional[str] = typer.Option(
        None, help="Specific LLM model name (e.g., gpt-4o). Overrides config."
    ),
    cloud_provider: Optional[str] = typer.Option(
        "gcp",
        "--cloud-provider",
        help="Cloud provider: gcp, aws, or multi (for multi-cloud).",
    ),
    execution_mode: Optional[str] = typer.Option(
        "auto",
        "--execution-mode",
        help="Execution mode: auto (default), yolo (auto-execute without prompts), manual (ask for confirmation on create/update/delete only)",
    ),
    gcp_project_id: Optional[str] = typer.Option(
        os.getenv("GCP_PROJECT_ID") or APP_CONFIG.get("gcp_project_id"),
        "--gcp-project-id",
        help="Google Cloud Project ID. Overrides config/env.",
    ),
    gcp_creds_path: Optional[str] = typer.Option(
        os.getenv("GCP_CREDENTIALS_PATH") or APP_CONFIG.get("gcp_credentials_path"),
        "--gcp-creds-path",
        help="Path to GCP service account key file. Overrides config/env.",
    ),
    gcp_region: Optional[str] = typer.Option(
        "us-central1", "--gcp-region", help="GCP default region."
    ),
    aws_region: Optional[str] = typer.Option(
        os.getenv("AWS_DEFAULT_REGION") or "us-west-2",
        "--aws-region",
        help="AWS default region.",
    ),
    aws_profile: Optional[str] = typer.Option(
        os.getenv("AWS_PROFILE"), "--aws-profile", help="AWS profile to use."
    ),
    aws_access_key: Optional[str] = typer.Option(
        os.getenv("AWS_ACCESS_KEY_ID"), "--aws-access-key", help="AWS access key ID."
    ),
    aws_secret_key: Optional[str] = typer.Option(
        os.getenv("AWS_SECRET_ACCESS_KEY"),
        "--aws-secret-key",
        help="AWS secret access key.",
    ),
    terraform_working_dir: Optional[str] = typer.Option(
        "terraform_workspace", "--terraform-dir", help="Terraform working directory."
    ),
    terraform_dry_run: bool = typer.Option(
        False, "--dry-run", help="Plan only, don't apply Terraform changes."
    ),
    terraform_keep_files: bool = typer.Option(
        False, "--keep-files", help="Keep Terraform files after execution."
    ),
    terraform_state_backend: Optional[str] = typer.Option(
        "local",
        "--state-backend",
        help="Terraform state backend (local, gcs, s3, etc.).",
    ),
    rag_docs_path: Optional[str] = typer.Option(
        os.getenv("GCLOUD_DOCS_PATH")
        or APP_CONFIG.get(
            "rag_docs_path",
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "internal",
                "tools",
                "gcloud_online_docs_markdown",
            ),
        ),
        "--rag-docs-path",
        help="Path to Markdown documents for RAG.",
    ),
    vector_store_cli: Optional[str] = typer.Option(
        None,
        "--vector-store",
        help="Vector store type: default (in-memory), chroma, duckdb. Overrides env and config.yaml.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output, including full exception tracebacks.",
    ),
):
    """Runs the Saturn orchestrator using Terraform for multi-cloud infrastructure provisioning."""

    console.print(
        Panel(
            f"Processing query with multi-cloud Terraform: '[bold cyan]{query}[/bold cyan]'\nTarget providers: [yellow]{cloud_provider}[/yellow]",
            title="Saturn Multi-Cloud Terraform",
        )
    )

    if execution_mode not in ["auto", "yolo", "manual"]:
        console.print(
            f"[bold red]Error:[/] Invalid execution mode '{execution_mode}'. Use: auto, yolo, or manual"
        )
        raise typer.Exit(code=1)

    config = APP_CONFIG.copy()
    config["llm_provider"] = provider
    if model:
        config[f"{provider}_model"] = model

    config["cloud_provider"] = cloud_provider
    config["execution_mode"] = execution_mode

    # GCP configuration
    if gcp_project_id:
        config["gcp_project_id"] = gcp_project_id
    if gcp_creds_path:
        config["gcp_credentials_path"] = gcp_creds_path
    config["gcp_default_region"] = gcp_region

    # AWS configuration
    config["aws_default_region"] = aws_region
    if aws_profile:
        config["aws_profile"] = aws_profile
    if aws_access_key:
        config["aws_access_key_id"] = aws_access_key
    if aws_secret_key:
        config["aws_secret_access_key"] = aws_secret_key

    # Terraform-specific configuration
    config["terraform_working_dir"] = terraform_working_dir
    config["terraform_dry_run"] = terraform_dry_run
    config["terraform_keep_files"] = terraform_keep_files
    config["terraform_state_backend"] = terraform_state_backend
    config["default_executor"] = "terraform"

    # RAG configuration (reuse from existing command)
    config["rag_docs_path_for_init"] = rag_docs_path
    config["vector_store_choice"] = (
        vector_store_cli
        or os.getenv("VECTOR_STORE")
        or APP_CONFIG.get("vector_store", "default")
    ).lower()

    # Validate that at least one cloud provider is configured
    gcp_configured = bool(config.get("gcp_project_id"))
    aws_configured = bool(config.get("aws_default_region"))

    if cloud_provider == "gcp" and not gcp_configured:
        console.print("[bold red]Error:[/] GCP Project ID required for GCP operations.")
        raise typer.Exit(code=1)
    elif cloud_provider == "aws" and not aws_configured:
        console.print("[bold red]Error:[/] AWS region required for AWS operations.")
        raise typer.Exit(code=1)
    elif cloud_provider == "multi" and not (gcp_configured or aws_configured):
        console.print(
            "[bold red]Error:[/] At least one cloud provider (GCP or AWS) must be configured for multi-cloud operations."
        )
        raise typer.Exit(code=1)

    try:
        from .hybrid_orchestrator import run_query_hybrid
        from .rag_engine import RAGEngine

        # Initialize RAG engine with simple defaults
        rag_engine_instance = RAGEngine(
            vector_store_choice="default",
            embed_model_name="sentence-transformers/all-MiniLM-L6-v2",
            documents_path_for_init=config.get(
                "rag_docs_path_for_init", "internal/tools/gcloud_online_docs_markdown"
            ),
            build_index_on_init=True,
            device="auto",
            parallel_process=False,
            embed_batch_size=32,
            preserve_code_blocks=True,
            preserve_command_context=True,
        )

        console.print("--- Starting Terraform Orchestrator ---")
        console.print(f"Execution Mode: {execution_mode}")

        if execution_mode == "yolo":
            console.print(
                "[bold green]🚀 YOLO MODE: Commands will auto-execute without confirmation[/bold green]"
            )
        elif execution_mode == "manual":
            console.print(
                "[bold yellow]✋ MANUAL MODE: You will be asked to confirm each command[/bold yellow]"
            )
        else:
            console.print(
                "[blue]🔄 AUTO MODE: Standard execution with progress display[/blue]"
            )

        asyncio.run(
            run_query_hybrid(
                query,
                config,
                rag_engine_instance,
                execution_mode="terraform",
                verbose=verbose,
            )
        )

    except Exception:
        console.print(
            "[bold red]\n--- An unexpected error occurred in 'terraform-run' command --- [/bold red]"
        )
        console.print_exception(show_locals=verbose)
        raise typer.Exit(code=1)


@app.command("hybrid-run")
def hybrid_run_command(
    query: str = typer.Argument(
        ..., help="The natural language query for the hybrid agent."
    ),
    execution_mode_hybrid: str = typer.Option(
        "auto", "--mode", help="Execution mode: auto, terraform, gcloud, or dual"
    ),
    execution_mode: Optional[str] = typer.Option(
        "auto",
        "--execution-mode",
        help="Execution mode: auto (default), yolo (auto-execute without prompts), manual (ask for confirmation on create/update/delete only)",
    ),
    provider: Optional[str] = typer.Option(
        os.getenv("LLM_PROVIDER") or APP_CONFIG.get("llm_provider", "openai"),
        help="LLM provider (e.g., openai, gemini, claude, mistral",
    ),
    model: Optional[str] = typer.Option(
        None, help="Specific LLM model name (e.g., gpt-4o). Overrides config."
    ),
    project_id: Optional[str] = typer.Option(
        os.getenv("GCP_PROJECT_ID") or APP_CONFIG.get("gcp_project_id"),
        "--project-id",
        help="Google Cloud Project ID. Overrides config/env.",
    ),
    creds_path: Optional[str] = typer.Option(
        os.getenv("GCP_CREDENTIALS_PATH") or APP_CONFIG.get("gcp_credentials_path"),
        "--creds-path",
        help="Path to GCP service account key file (uses ADC if not provided). Overrides config/env.",
    ),
    default_executor: Optional[str] = typer.Option(
        "gcloud",
        "--default-executor",
        help="Default executor when mode is auto: gcloud or terraform",
    ),
    terraform_dry_run: bool = typer.Option(
        False, "--dry-run", help="Plan only, don't apply Terraform changes."
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output, including full exception tracebacks.",
    ),
):
    """Runs the Saturn orchestrator with hybrid Terraform/gcloud execution."""

    if execution_mode_hybrid not in ["auto", "terraform", "gcloud", "dual"]:
        console.print(
            f"[bold red]Error:[/] Invalid execution mode '{execution_mode_hybrid}'. Use: auto, terraform, gcloud, or dual"
        )
        raise typer.Exit(code=1)

    if execution_mode not in ["auto", "yolo", "manual"]:
        console.print(
            f"[bold red]Error:[/] Invalid execution mode '{execution_mode}'. Use: auto, yolo, or manual"
        )
        raise typer.Exit(code=1)

    console.print(
        Panel(
            f"Processing query with hybrid orchestrator\n"
            f"Query: '[bold cyan]{query}[/bold cyan]'\n"
            f"Mode: [yellow]{execution_mode_hybrid}[/yellow]",
            title="Saturn Hybrid Command",
        )
    )

    config = APP_CONFIG.copy()
    config["llm_provider"] = provider
    if model:
        config[f"{provider}_model"] = model
    if project_id:
        config["gcp_project_id"] = project_id
    if creds_path:
        config["gcp_credentials_path"] = creds_path
    config["default_executor"] = default_executor
    config["terraform_dry_run"] = terraform_dry_run
    config["execution_mode"] = execution_mode

    if not config.get("gcp_project_id"):
        console.print("[bold red]Error:[/] GCP Project ID not found.")
        raise typer.Exit(code=1)

    try:
        from .hybrid_orchestrator import run_query_hybrid
        from .rag_engine import RAGEngine

        rag_engine_instance = RAGEngine(
            config=APP_CONFIG,
            vector_store_choice="default",
            embed_model_name="sentence-transformers/all-MiniLM-L6-v2",
            documents_path_for_init=config.get(
                "rag_docs_path_for_init", "internal/tools/gcloud_online_docs_markdown"
            ),
            build_index_on_init=True,
            device="auto",
            parallel_process=False,
            embed_batch_size=32,
            preserve_code_blocks=True,
            preserve_command_context=True,
        )

        console.print("--- Starting Hybrid Orchestrator ---")
        console.print(f"Execution Mode: {execution_mode}")

        if execution_mode == "yolo":
            console.print(
                "[bold green]🚀 YOLO MODE: Commands will auto-execute without confirmation[/bold green]"
            )
        elif execution_mode == "manual":
            console.print(
                "[bold yellow]✋ MANUAL MODE: You will be asked to confirm each command[/bold yellow]"
            )
        else:
            console.print(
                "[blue]🔄 AUTO MODE: Standard execution with progress display[/blue]"
            )

        asyncio.run(
            run_query_hybrid(
                query,
                config,
                rag_engine_instance,
                execution_mode=execution_mode_hybrid,
                verbose=verbose,
            )
        )

    except Exception:
        console.print(
            "[bold red]\n--- An unexpected error occurred in 'hybrid-run' command --- [/bold red]"
        )
        console.print_exception(show_locals=verbose)
        raise typer.Exit(code=1)


@app.command("convert-history")
def convert_history_command(
    log_file: str = typer.Argument(
        ..., help="Path to Saturn execution log file (JSON format)."
    ),
    output_file: Optional[str] = typer.Option(
        "converted_terraform.tf", "--output", "-o", help="Output Terraform file path."
    ),
    project_id: Optional[str] = typer.Option(
        os.getenv("GCP_PROJECT_ID") or APP_CONFIG.get("gcp_project_id"),
        "--project-id",
        help="Google Cloud Project ID.",
    ),
    creds_path: Optional[str] = typer.Option(
        os.getenv("GCP_CREDENTIALS_PATH") or APP_CONFIG.get("gcp_credentials_path"),
        "--creds-path",
        help="Path to GCP service account key file.",
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output."
    ),
):
    """Convert gcloud command history from Saturn logs to Terraform configuration."""

    if not os.path.exists(log_file):
        console.print(f"[bold red]Error:[/] Log file not found: {log_file}")
        raise typer.Exit(code=1)

    console.print(
        Panel(
            f"Converting Saturn history to Terraform\nInput: [cyan]{log_file}[/cyan]\nOutput: [green]{output_file}[/green]",
            title="History Conversion",
        )
    )

    config = APP_CONFIG.copy()
    if project_id:
        config["gcp_project_id"] = project_id
    if creds_path:
        config["gcp_credentials_path"] = creds_path

    try:
        from .hybrid_orchestrator import HybridOrchestrator
        from .rag_engine import RAGEngine

        rag_engine_instance = RAGEngine(
            vector_store_choice="default", build_index_on_init=False
        )

        orchestrator = HybridOrchestrator(config, rag_engine_instance)

        result = asyncio.run(
            orchestrator.generate_terraform_from_gcloud_history(log_file)
        )

        if result["status"] == "success":
            if output_file != result["combined_file"]:
                import shutil

                shutil.move(result["combined_file"], output_file)

            console.print(
                "[bold green]✓ Successfully converted history to Terraform![/bold green]"
            )
            console.print(f"Output file: {output_file}")
            console.print(f"Converted {len(result['configs'])} commands")

            if verbose:
                console.print("\n[bold]Generated Terraform Configuration:[/bold]")
                console.print(result["combined_config"])

        elif result["status"] == "no_conversions":
            console.print(f"[yellow]⚠ {result['message']}[/yellow]")
        else:
            console.print(
                f"[bold red]✗ Conversion failed: {result.get('error', 'Unknown error')}[/bold red]"
            )
            raise typer.Exit(code=1)

    except Exception as e:
        console.print(
            "[bold red]\n--- An unexpected error occurred in 'convert-history' command --- [/bold red]"
        )
        if verbose:
            console.print_exception(show_locals=True)
        else:
            console.print(f"Error: {e}")
        raise typer.Exit(code=1)


@app.command("install-cli")
def install_cli_command(
    gcp: bool = typer.Option(True, "--gcp/--no-gcp", help="Install Google Cloud CLI"),
    aws: bool = typer.Option(True, "--aws/--no-aws", help="Install AWS CLI"),
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output"
    ),
):
    """Install AWS and/or GCP CLI tools."""

    console.print(Panel("Installing Cloud CLI Tools", title="Saturn CLI Installation"))

    def get_os_type():
        """Get the operating system type."""
        system = os.uname().sysname if hasattr(os, "uname") else os.name
        if system == "Darwin":
            return "macos"
        elif system == "Linux":
            return "linux"
        elif system == "Windows" or os.name == "nt":
            return "windows"
        return "unknown"

    def install_gcp_cli():
        """Install Google Cloud CLI based on OS."""
        os_type = get_os_type()

        if os_type == "macos":
            console.print("Downloading Google Cloud SDK...")
            os.system("curl https://sdk.cloud.google.com > install.sh")
            os.system("bash install.sh --disable-prompts")
            os.system("rm install.sh")

            shell = os.environ.get("SHELL", "")
            if "zsh" in shell:
                with open(os.path.expanduser("~/.zshrc"), "a") as f:
                    f.write("\n# Google Cloud SDK\n")
                    f.write(
                        'source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.zsh.inc"\n'
                    )
                    f.write(
                        'source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.zsh.inc"\n'
                    )
            elif "bash" in shell:
                with open(os.path.expanduser("~/.bashrc"), "a") as f:
                    f.write("\n# Google Cloud SDK\n")
                    f.write(
                        'source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/path.bash.inc"\n'
                    )
                    f.write(
                        'source "$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/completion.bash.inc"\n'
                    )

        elif os_type == "linux":
            console.print("Installing Google Cloud SDK for Linux...")
            os.system(
                'echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list'
            )
            os.system(
                "curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -"
            )
            os.system("sudo apt-get update && sudo apt-get install google-cloud-sdk")

            with open(os.path.expanduser("~/.bashrc"), "a") as f:
                f.write("\n# Google Cloud SDK\n")
                f.write("source /usr/share/google-cloud-sdk/completion.bash.inc\n")
                f.write("source /usr/share/google-cloud-sdk/path.bash.inc\n")

            if os.path.exists("/usr/share/google-cloud-sdk/completion.zsh.inc"):
                with open(os.path.expanduser("~/.zshrc"), "a") as f:
                    f.write("\n# Google Cloud SDK\n")
                    f.write("source /usr/share/google-cloud-sdk/completion.zsh.inc\n")
                    f.write("source /usr/share/google-cloud-sdk/path.zsh.inc\n")

        elif os_type == "windows":
            console.print("Downloading Google Cloud SDK for Windows...")
            os.system(
                "curl -o GoogleCloudSDKInstaller.exe https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe"
            )
            console.print(
                "Please run GoogleCloudSDKInstaller.exe to complete the installation"
            )
            console.print(
                "After installation, restart your terminal and run 'gcloud init'"
            )
            return False

        else:
            console.print("[bold red]Error:[/] Unsupported operating system")
            console.print(
                "Please install manually from: https://cloud.google.com/sdk/docs/install"
            )
            return False

        console.print(
            "[bold green]✓ Google Cloud CLI installed successfully![/bold green]"
        )
        if os_type != "windows":
            console.print(
                "Please restart your terminal or run 'source ~/.bashrc' (or ~/.zshrc) to update your PATH"
            )
        return True

    def install_aws_cli():
        """Install AWS CLI based on OS."""
        os_type = get_os_type()

        if os_type == "macos":
            console.print("Installing AWS CLI using Homebrew...")
            os.system("brew install awscli")

        elif os_type == "linux":
            console.print("Installing AWS CLI for Linux...")
            os.system(
                'curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"'
            )
            os.system("unzip awscliv2.zip")
            os.system("sudo ./aws/install")
            os.system("rm -rf aws awscliv2.zip")

        elif os_type == "windows":
            console.print("Downloading AWS CLI for Windows...")
            os.system("curl -o AWSCLIV2.msi https://awscli.amazonaws.com/AWSCLIV2.msi")
            console.print("Please run AWSCLIV2.msi to complete the installation")
            console.print(
                "After installation, restart your terminal and run 'aws configure'"
            )
            return False

        else:
            console.print("[bold red]Error:[/] Unsupported operating system")
            console.print("Please install manually from: https://aws.amazon.com/cli/")
            return False

        console.print("[bold green]✓ AWS CLI installed successfully![/bold green]")
        return True

    if gcp:
        console.print("\n[bold cyan]Installing Google Cloud CLI...[/bold cyan]")
        try:
            gcp_success = install_gcp_cli()
        except Exception as e:
            console.print(f"[bold red]Error installing Google Cloud CLI:[/] {str(e)}")
            if verbose:
                console.print_exception(show_locals=True)
            raise typer.Exit(code=1)

    if aws:
        console.print("\n[bold cyan]Installing AWS CLI...[/bold cyan]")
        try:
            aws_success = install_aws_cli()
        except Exception as e:
            console.print(f"[bold red]Error installing AWS CLI:[/] {str(e)}")
            if verbose:
                console.print_exception(show_locals=True)
            raise typer.Exit(code=1)

    console.print("\n[bold green]Installation complete![/bold green]")
    console.print("\nNext steps:")
    if gcp and gcp_success:
        console.print("1. Run 'gcloud init' to initialize Google Cloud CLI")
    if aws and aws_success:
        console.print(
            "2. Run 'aws configure' to configure AWS CLI with your credentials"
        )


@app.command("cache")
def cache_command(
    action: str = typer.Argument(..., help="Action: 'status', 'clear', or 'stats'"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed cache information")
):
    """Manage Saturn's performance caches."""
    
    if action == "status":
        console.print("[bold blue]Cache Status[/bold blue]")
        
        # Check FileBuildToolCaller cache
        from saturn.file_build_tools import FileBuildToolCaller
        tools_cached = FileBuildToolCaller._is_tools_cache_valid()
        cache_age = time.time() - FileBuildToolCaller._tools_cache_timestamp if FileBuildToolCaller._tools_cache_timestamp > 0 else 0
        
        console.print(f"File Tools Cache: {'✓ Valid' if tools_cached else '✗ Invalid/Empty'}")
        if FileBuildToolCaller._tools_cache_timestamp > 0:
            console.print(f"  Age: {cache_age:.1f} seconds")
            console.print(f"  TTL: {FileBuildToolCaller._tools_cache_ttl} seconds")
            if verbose and FileBuildToolCaller._tools_schema_cache:
                console.print(f"  Cached Tools: {len(FileBuildToolCaller._tools_schema_cache)}")
        
        # Show performance configuration
        console.print(f"\nPerformance Settings:")
        console.print(f"  Tool Cache TTL: {APP_CONFIG.get('tool_cache_ttl', 300)} seconds")
        console.print(f"  Checkpoints Enabled: {APP_CONFIG.get('enable_checkpoints', False)}")
        console.print(f"  Parallel Execution: {APP_CONFIG.get('parallel_execution', True)}")
        console.print(f"  Max Parallel Tasks: {APP_CONFIG.get('max_parallel_tasks', 3)}")
        
    elif action == "clear":
        console.print("[yellow]Clearing all caches...[/yellow]")
        
        # Clear FileBuildToolCaller cache
        from saturn.file_build_tools import FileBuildToolCaller
        FileBuildToolCaller.clear_tools_cache()
        
        console.print("[green]✓ File tools cache cleared[/green]")
        console.print("[green]✓ All caches cleared successfully[/green]")
        
    elif action == "stats":
        console.print("[bold blue]Cache Performance Statistics[/bold blue]")
        
        # This would be more useful during actual execution
        # For now, show configuration that affects performance
        console.print("Configuration affecting performance:")
        performance_keys = [
            'tool_cache_ttl', 'enable_checkpoints', 'parallel_execution', 
            'max_parallel_tasks', 'fail_fast', 'max_retries'
        ]
        
        for key in performance_keys:
            value = APP_CONFIG.get(key, "Not set")
            console.print(f"  {key}: {value}")
            
        if verbose:
            console.print(f"\nAll configuration keys:")
            for key, value in sorted(APP_CONFIG.items()):
                console.print(f"  {key}: {value}")
                
    else:
        console.print(f"[bold red]Error:[/bold red] Unknown action '{action}'. Use 'status', 'clear', or 'stats'.")
        raise typer.Exit(code=1)


@app.command("workflow")
def workflow_command(
    action: str = typer.Argument(..., help="Action: 'list', 'validate', or 'info'"),
    workflow_path: Optional[str] = typer.Option(
        None, "--path", "-p", help="Path to specific .sat workflow file (for validate/info actions)"
    ),
    directory: Optional[str] = typer.Option(
        ".", "--dir", "-d", help="Directory to search for .sat files (for list action)"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Show detailed information")
):
    """Manage Saturn workflow (.sat) files."""
    
    if action == "list":
        console.print(f"[bold blue]Saturn Workflows in {directory}[/bold blue]")
        
        try:
            from internal.saturn_workflow import SaturnWorkflow
            workflow_handler = SaturnWorkflow()
            workflows = workflow_handler.list_workflows(directory)
            
            if not workflows:
                console.print(f"[yellow]No .sat workflow files found in {directory}[/yellow]")
                return
            
            from rich.table import Table
            table = Table(title=f"Found {len(workflows)} workflow(s)")
            table.add_column("Filename", style="cyan")
            table.add_column("Created", style="dim")
            table.add_column("Steps", justify="right", style="green")
            table.add_column("Dependencies", justify="right", style="blue")
            if verbose:
                table.add_column("Original Query", style="dim")
            
            for workflow in workflows:
                created = workflow["created_at"][:19].replace("T", " ") if workflow["created_at"] != "Unknown" else "Unknown"
                row = [
                    workflow["filename"],
                    created,
                    str(workflow["step_count"]),
                    str(workflow["edge_count"])
                ]
                if verbose:
                    query = workflow["original_query"][:50] + "..." if len(workflow["original_query"]) > 50 else workflow["original_query"]
                    row.append(query)
                table.add_row(*row)
            
            console.print(table)
            
        except Exception as e:
            console.print(f"[bold red]Error listing workflows: {e}[/bold red]")
            raise typer.Exit(code=1)
    
    elif action == "validate":
        if not workflow_path:
            console.print("[bold red]Error:[/bold red] --path is required for validate action")
            raise typer.Exit(code=1)
        
        try:
            from internal.saturn_workflow import SaturnWorkflow
            workflow_handler = SaturnWorkflow()
            
            console.print(f"[cyan]Validating workflow: {workflow_path}[/cyan]")
            is_valid = workflow_handler.validate_workflow(workflow_path)
            
            if is_valid:
                console.print("[green]✓ Workflow is valid and ready for execution[/green]")
            else:
                console.print("[red]✗ Workflow validation failed[/red]")
                raise typer.Exit(code=1)
                
        except FileNotFoundError:
            console.print(f"[bold red]Error:[/bold red] Workflow file not found: {workflow_path}")
            raise typer.Exit(code=1)
        except Exception as e:
            console.print(f"[bold red]Error validating workflow: {e}[/bold red]")
            raise typer.Exit(code=1)
    
    elif action == "info":
        if not workflow_path:
            console.print("[bold red]Error:[/bold red] --path is required for info action")
            raise typer.Exit(code=1)
        
        try:
            from internal.saturn_workflow import SaturnWorkflow
            workflow_handler = SaturnWorkflow()
            
            dag, step_details_map, execution_order, original_query = workflow_handler.load_workflow(workflow_path)
            
            from rich.panel import Panel
            from rich.table import Table
            
            # Workflow metadata
            console.print(Panel(
                f"[bold]Original Query:[/bold] {original_query}\n"
                f"[bold]Steps:[/bold] {len(step_details_map)}\n"
                f"[bold]Dependencies:[/bold] {len(dag.edges)}\n"
                f"[bold]Execution Order:[/bold] {' → '.join(execution_order)}",
                title=f"Workflow Info: {os.path.basename(workflow_path)}",
                border_style="blue"
            ))
            
            # Step details table
            steps_table = Table(title="Step Details")
            steps_table.add_column("Step ID", style="cyan")
            steps_table.add_column("Provider", style="dim")
            steps_table.add_column("Tool", style="green")
            steps_table.add_column("Description")
            
            for step_id in execution_order:
                details = step_details_map[step_id]
                provider = details.get("cloud_provider", "")
                if not provider:
                    tool_name = details.get("tool_to_use", "")
                    if tool_name.startswith("mcp_"):
                        provider = "MCP"
                    else:
                        provider = "FILE"
                else:
                    provider = provider.upper()
                
                steps_table.add_row(
                    step_id,
                    provider,
                    details.get("tool_to_use", ""),
                    details.get("description", "")
                )
            
            console.print(steps_table)
            
            if verbose:
                # Dependencies table
                deps_table = Table(title="Dependencies")
                deps_table.add_column("Step", style="cyan")
                deps_table.add_column("Depends On", style="yellow")
                
                for step_id, details in step_details_map.items():
                    deps = details.get("dependencies", [])
                    if deps:
                        deps_table.add_row(step_id, ", ".join(deps))
                
                if deps_table.rows:
                    console.print(deps_table)
                else:
                    console.print("[dim]No dependencies found[/dim]")
                
        except Exception as e:
            console.print(f"[bold red]Error reading workflow info: {e}[/bold red]")
            raise typer.Exit(code=1)
    
    else:
        console.print(f"[bold red]Error:[/bold red] Unknown action '{action}'. Use 'list', 'validate', or 'info'.")
        raise typer.Exit(code=1)


# Add CLI question handler
async def cli_question_handler(formatted_question: str, suggested_answers: list = None) -> str:
    """Handle questions in CLI mode by prompting user for input."""
    from rich.console import Console
    from rich.prompt import Prompt
    
    console = Console()
    console.print(formatted_question)
    
    if suggested_answers:
        console.print("\n[dim]You can type the number (1, 2, etc.) or the full answer.[/dim]")
    
    while True:
        try:
            answer = Prompt.ask("\n[bold yellow]Your answer[/bold yellow]")
            
            # If suggested answers exist, check if user provided a number
            if suggested_answers and answer.strip().isdigit():
                index = int(answer.strip()) - 1
                if 0 <= index < len(suggested_answers):
                    return suggested_answers[index]
                else:
                    console.print(f"[red]Please enter a number between 1 and {len(suggested_answers)} or type your answer.[/red]")
                    continue
            
            # Return the answer as-is
            if answer.strip():
                return answer.strip()
            else:
                console.print("[red]Please provide an answer.[/red]")
                continue
                
        except KeyboardInterrupt:
            console.print("\n[yellow]Skipping question...[/yellow]")
            return "SKIPPED_BY_USER"
        except Exception as e:
            console.print(f"[red]Error getting input: {e}[/red]")
            return "ERROR_GETTING_INPUT"


if __name__ == "__main__":
    app()
