import typer
import os
import asyncio
from typing import Optional, List
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

# Import from within the saturn package
from .config import load_config
from .orchestrator import run_query_with_feedback # Use the loop version
from .knowledge_base import KnowledgeBase # Still used for something else potentially, or can be removed if not
from .gcp_executor import GcloudExecutor
from .rag_engine import (
    RAGEngine, 
    DEFAULT_EMBED_MODEL_NAME, 
    DEFAULT_CHROMA_PATH, 
    DEFAULT_CHROMA_COLLECTION, 
    DEFAULT_DUCKDB_PATH, 
    DEFAULT_DUCKDB_DB_FILE_NAME, 
    DEFAULT_DUCKDB_TABLE_NAME
)

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
    # kb_path is for the old KnowledgeBase, RAG uses rag_docs_path
    # kb_path: Optional[str] = typer.Option(os.getenv("KB_PATH") or APP_CONFIG.get('kb_path', "api_defs"), "--kb-path", help="Path to the knowledge base API definitions."),
    rag_docs_path: Optional[str] = typer.Option(os.getenv("GCLOUD_DOCS_PATH") or APP_CONFIG.get('rag_docs_path', os.path.join(os.path.dirname(__file__), '..' , 'internal', 'tools', 'gcloud_online_docs_markdown')), "--rag-docs-path", help="Path to Markdown documents for RAG."),
    
    vector_store_cli: Optional[str] = typer.Option(None, "--vector-store", help="Vector store type: default (in-memory), chroma, duckdb. Overrides env and config.yaml."), # Changed name to avoid conflict
    
    db_path: Optional[str] = typer.Option(None, "--db-path", help="Path for persistent DB (e.g., ./db/chroma_store or ./db/duckdb_store/vector_store.duckdb)."),
    db_collection_or_table: Optional[str] = typer.Option(None, "--db-collection-table", help="Collection name (Chroma) or Table name (DuckDB)."),
    rag_embed_model: Optional[str] = typer.Option(
        os.getenv("RAG_EMBED_MODEL") or APP_CONFIG.get('rag_embedding_model', DEFAULT_EMBED_MODEL_NAME),
        "--rag-embed-model", 
        help="RAG embedding model name."
    ),
    google_api_key_cli: Optional[str] = typer.Option(None, "--google-api-key", help="Google API Key for Gemini Embeddings. Overrides GOOGLE_API_KEY env var."),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="Enable verbose output, including full exception tracebacks.")
):
    """Runs the Saturn orchestrator with the specified query and configuration."""
    
    console.print(Panel(f"Processing query: '[bold cyan]{query}[/bold cyan]'", title="Saturn Command"))

    config = APP_CONFIG.copy()
    config['llm_provider'] = provider
    if model: config[f'{provider}_model'] = model
    if project_id: config['gcp_project_id'] = project_id
    if creds_path: config['gcp_credentials_path'] = creds_path
    config['max_retries'] = max_retries 
    config['rag_docs_path_for_init'] = rag_docs_path 
    config['rag_embedding_model'] = rag_embed_model
    config['google_api_key'] = google_api_key_cli or os.getenv("GOOGLE_API_KEY") or config.get('google_api_key')

    # Determine vector_store_choice with clear precedence for diagnosis
    vs_choice_source = "hardcoded default in CLI"
    resolved_vector_store = "default" # Ultimate fallback

    if vector_store_cli:
        resolved_vector_store = vector_store_cli
        vs_choice_source = "CLI option (--vector-store)"
    elif os.getenv("VECTOR_STORE"):
        resolved_vector_store = os.getenv("VECTOR_STORE")
        vs_choice_source = "environment variable (VECTOR_STORE)"
    elif APP_CONFIG.get('vector_store'):
        resolved_vector_store = APP_CONFIG.get('vector_store')
        vs_choice_source = "config.yaml (vector_store key)"
    # If none of the above, resolved_vector_store remains "default" from its initialization
    
    config['vector_store_choice'] = resolved_vector_store.lower()
    console.print(f"[Config] Vector store choice '{config['vector_store_choice']}' determined from: {vs_choice_source}")


    db_configuration = {}
    if config['vector_store_choice'] == "chroma":
        db_configuration["chroma_path"] = db_path or DEFAULT_CHROMA_PATH
        db_configuration["chroma_collection_name"] = db_collection_or_table or DEFAULT_CHROMA_COLLECTION
    elif config['vector_store_choice'] == "duckdb":
        db_dir = os.path.dirname(db_path) if db_path and '.duckdb' in db_path else (db_path or DEFAULT_DUCKDB_PATH)
        db_file = os.path.basename(db_path) if db_path and '.duckdb' in db_path else DEFAULT_DUCKDB_DB_FILE_NAME
        db_configuration["duckdb_path"] = db_dir
        db_configuration["duckdb_file_name"] = db_file
        db_configuration["duckdb_table_name"] = db_collection_or_table or DEFAULT_DUCKDB_TABLE_NAME
    config['db_config'] = db_configuration if db_configuration else None
    
    config['rag_build_on_init'] = True if config['vector_store_choice'] == "default" else False

    if not config.get('gcp_project_id'):
        console.print("[bold red]Error:[/] GCP Project ID not found.")
        raise typer.Exit(code=1)
    required_api_key_name = f'{config["llm_provider"]}_api_key'
    if not config.get(required_api_key_name) and config["llm_provider"] != "mock": # Allow mock provider
        console.print(f"[bold red]Error:[/] {required_api_key_name.upper()} not found for provider '{config["llm_provider"]}'.")
        raise typer.Exit(code=1)
    
    console.print("--- Initializing Saturn Agent ---")
    console.print(f"Using LLM Provider: {config['llm_provider']}")
    if config.get(f'{provider}_model'):
        console.print(f"Using Model: {config.get(f'{provider}_model')}")
    console.print(f"Target GCP Project: {config['gcp_project_id']}")
    console.print(f"RAG Docs Path for Init/Ingest: {config['rag_docs_path_for_init']}")
    console.print(f"RAG Vector Store: {config['vector_store_choice']}")
    if config['db_config']:
        console.print(f"RAG DB Config: {config['db_config']}")
    if config['google_api_key'] and "gemini" in config['rag_embedding_model']:
        console.print("[Config] GOOGLE_API_KEY will be used for Gemini embeddings.")

    try:
        executor = GcloudExecutor(config)
        rag_engine_instance = RAGEngine(
            vector_store_choice=config['vector_store_choice'],
            db_config=config['db_config'],
            embed_model_name=config['rag_embedding_model'],
            google_api_key=config.get('google_api_key'),
            documents_path_for_init=config['rag_docs_path_for_init'] if config['vector_store_choice'] == 'default' else None,
            build_index_on_init=config['rag_build_on_init'],
            llm_for_settings=None
        )

        if not rag_engine_instance.query_engine and config['vector_store_choice'] != 'default':
            console.print(f"[bold yellow]Warning:[/] RAG query engine for '{config['vector_store_choice']}' not ready. Index may need to be ingested first using 'saturn ingest-docs'.")

        console.print("--- Starting Orchestrator ---")
        asyncio.run(run_query_with_feedback(query, config, rag_engine_instance, verbose=verbose))

    except Exception as e:
        console.print(f"[bold red]\n--- An unexpected error occurred in 'run' command --- [/bold red]")
        console.print_exception(show_locals=verbose)
        raise typer.Exit(code=1)

@app.command("ingest-docs")
def ingest_docs_command(
    docs_path: str = typer.Option(
        os.getenv("GCLOUD_DOCS_PATH") or APP_CONFIG.get('rag_docs_path', os.path.join(os.path.dirname(__file__), '..' , 'internal', 'tools', 'gcloud_online_docs_markdown')),
        "--docs-path", 
        help="Path to Markdown documents to ingest."
    ),
    vector_store: str = typer.Option(
        os.getenv("VECTOR_STORE", "chroma"), 
        "--vector-store", 
        help="Vector store type: default (in-memory, not persistent for ingest), chroma, duckdb."
    ),
    # db_path: Optional[str] = typer.Option(None, "--db-path", help="Base path for persistent DB (e.g., ./db/chroma_store or ./db/duckdb_store)."), # REMOVED
    # db_name: Optional[str] = typer.Option(None, "--db-name", help="Collection name (Chroma) or DB file name (DuckDB, e.g., vectors.duckdb)."), # REMOVED
    # table_name: Optional[str] = typer.Option(None, "--table-name", help="Table name (DuckDB only)."), # REMOVED
    rag_embed_model: Optional[str] = typer.Option(
        os.getenv("RAG_EMBED_MODEL") or APP_CONFIG.get('rag_embedding_model', DEFAULT_EMBED_MODEL_NAME),
        "--rag-embed-model", 
        help="RAG embedding model name."
    ),
    google_api_key_cli: Optional[str] = typer.Option(None, "--google-api-key", help="Google API Key for Gemini Embeddings. Overrides GOOGLE_API_KEY env var."),
    force_rebuild: bool = typer.Option(False, "--force-rebuild", help="Force rebuild of the index, deleting existing data in persistent stores.")
):
    """Ingests documents into the specified vector store using predefined paths/names.""" # Updated docstring
    console.print(Panel(f"Starting Document Ingestion for Vector Store: [bold cyan]{vector_store}[/bold cyan]", title="Saturn Ingestion"))
    console.print(f"Documents path: {docs_path}")

    vs_choice = vector_store.lower()
    if vs_choice == "default":
        console.print("[bold yellow]Warning:[/] 'default' (in-memory) vector store selected. Ingestion will not be persistent. Use 'chroma' or 'duckdb' for persistence.")

    db_configuration = {}
    if vs_choice == "chroma":
        db_configuration["chroma_path"] = DEFAULT_CHROMA_PATH # Use default constant
        db_configuration["chroma_collection_name"] = DEFAULT_CHROMA_COLLECTION # Use default constant
        console.print(f"[Info] Using ChromaDB with default path: '{DEFAULT_CHROMA_PATH}' and collection: '{DEFAULT_CHROMA_COLLECTION}'")
    elif vs_choice == "duckdb":
        db_configuration["duckdb_path"] = DEFAULT_DUCKDB_PATH # Use default constant
        db_configuration["duckdb_file_name"] = DEFAULT_DUCKDB_DB_FILE_NAME # Use default constant
        db_configuration["duckdb_table_name"] = DEFAULT_DUCKDB_TABLE_NAME # Use default constant
        console.print(f"[Info] Using DuckDB with default path: '{DEFAULT_DUCKDB_PATH}/{DEFAULT_DUCKDB_DB_FILE_NAME}' and table: '{DEFAULT_DUCKDB_TABLE_NAME}'")
    
    effective_google_api_key = google_api_key_cli or os.getenv("GOOGLE_API_KEY") or APP_CONFIG.get('google_api_key')

    console.print(f"Using Embedding Model: {rag_embed_model}")
    if effective_google_api_key and "gemini" in rag_embed_model.lower():
        console.print("[Config] GOOGLE_API_KEY will be used for Gemini embeddings.")
    
    try:
        rag_engine_instance = RAGEngine(
            vector_store_choice=vs_choice,
            db_config=db_configuration if db_configuration else None, # Pass None if not chroma/duckdb
            embed_model_name=rag_embed_model,
            google_api_key=effective_google_api_key,
            llm_for_settings=None # Explicitly set LlamaIndex LLM to None
        )
        
        console.print(f"Attempting to ingest and build index...")
        success = rag_engine_instance.ingest_and_build_index(documents_path=docs_path, force_rebuild=force_rebuild)
        
        if success:
            console.print(f"[bold green]Document ingestion and index building completed successfully for '{vs_choice}'![/bold green]")
        else:
            console.print(f"[bold red]Document ingestion and index building failed for '{vs_choice}'. Check logs above.[/bold red]")
            raise typer.Exit(code=1)

    except Exception as e:
        console.print(f"[bold red]\n--- An unexpected error occurred during 'ingest-docs' command --- [/bold red]")
        console.print_exception(show_locals=False)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app() 