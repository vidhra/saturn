#!/usr/bin/env python3
"""
Multi-Provider Documentation Ingestion Script

This script demonstrates how to ingest both GCP and AWS CLI documentation
into separate ChromaDB collections using provider-specific configurations.

Usage:
    python internal/tools/ingest_multi_provider_docs.py
"""

import os
import sys
from pathlib import Path

# Add saturn directory to path for imports
saturn_dir = Path(__file__).parent.parent.parent / "saturn"
sys.path.insert(0, str(saturn_dir))

from rag_engine import RAGEngine, build_provider_db_config, get_provider_docs_path
from config import load_config
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def ingest_provider_docs(provider: str, config: dict, vector_store_choice: str = "chroma"):
    """
    Ingest documentation for a specific cloud provider.
    
    Args:
        provider: "gcp" or "aws" 
        config: Configuration dictionary
        vector_store_choice: "chroma" or "duckdb"
    """
    console.print(f"\n[bold blue]Ingesting {provider.upper()} CLI Documentation[/bold blue]")
    
    # Get provider-specific paths and database config
    docs_path = get_provider_docs_path(config, provider)
    db_config = build_provider_db_config(config, provider, vector_store_choice)
    
    # Display configuration
    config_table = Table(title=f"{provider.upper()} Configuration", show_header=True, header_style="bold magenta")
    config_table.add_column("Setting", style="cyan")
    config_table.add_column("Value", style="white")
    
    config_table.add_row("Documentation Path", docs_path)
    config_table.add_row("Vector Store", vector_store_choice)
    for key, value in db_config.items():
        config_table.add_row(key, str(value))
    
    console.print(config_table)
    
    # Check if docs directory exists
    if not os.path.isdir(docs_path):
        console.print(f"[bold red]Error:[/] Documentation directory not found: {docs_path}")
        console.print(f"Please run the {provider} documentation scraper first.")
        return False
    
    try:
        # Initialize RAG Engine with provider-specific config
        rag_engine = RAGEngine(
            vector_store_choice=vector_store_choice,
            db_config=db_config,
            embed_model_name=config.get("rag_embedding_model", "models/text-embedding-004"),
            google_api_key=config.get("google_api_key"),
            llm_for_settings=None,
            # Context-aware parsing settings from config
            use_context_aware_parsing=config.get("use_context_aware_parsing", True),
            max_chunk_size=config.get("max_chunk_size", 2048),
            chunk_overlap=config.get("chunk_overlap", 200),
            preserve_code_blocks=config.get("preserve_code_blocks", True),
            preserve_command_context=config.get("preserve_command_context", True)
        )
        
        # Ingest documents
        console.print(f"[yellow]Ingesting {provider.upper()} documentation...[/yellow]")
        success = rag_engine.ingest_and_build_index(docs_path, force_rebuild=True)
        
        if success:
            console.print(f"[bold green]✅ {provider.upper()} documentation ingested successfully![/bold green]")
            
            # Test query to verify ingestion
            if provider == "gcp":
                test_query = "How to create a gcloud compute instance?"
            else:  # aws
                test_query = "How to list S3 buckets using AWS CLI?"
                
            console.print(f"[yellow]Testing with query: '{test_query}'[/yellow]")
            result = rag_engine.query_docs(test_query)
            
            if result and "No relevant documents found" not in result:
                console.print(f"[bold green]✅ Query test successful for {provider.upper()}![/bold green]")
                # Show first 200 chars of result
                preview = result[:200] + "..." if len(result) > 200 else result
                console.print(Panel(preview, title=f"Query Result Preview ({provider.upper()})", border_style="green"))
            else:
                console.print(f"[bold yellow]⚠️  Query test returned no results for {provider.upper()}[/bold yellow]")
                
        else:
            console.print(f"[bold red]❌ Failed to ingest {provider.upper()} documentation[/bold red]")
            
        return success
        
    except Exception as e:
        console.print(f"[bold red]Error ingesting {provider.upper()} docs:[/] {e}")
        return False

def main():
    """Main function to ingest both GCP and AWS documentation."""
    console.print(Panel("Multi-Provider CLI Documentation Ingestion", style="bold blue"))
    
    # Load configuration
    try:
        config = load_config()
        console.print("[green]Configuration loaded successfully[/green]")
    except Exception as e:
        console.print(f"[bold red]Error loading configuration:[/] {e}")
        return 1
    
    # Check required configuration
    vector_store = config.get("vector_store", "chroma")
    embedding_model = config.get("rag_embedding_model", "models/text-embedding-004")
    
    console.print(f"Using vector store: [cyan]{vector_store}[/cyan]")
    console.print(f"Using embedding model: [cyan]{embedding_model}[/cyan]")
    
    if embedding_model.startswith("models/") and not config.get("google_api_key"):
        console.print("[bold red]Error:[/] Google API key required for Google embedding models")
        console.print("Set GOOGLE_API_KEY environment variable or add google_api_key to config.yaml")
        return 1
    
    # Ingest documentation for both providers
    providers = ["gcp", "aws"]
    results = {}
    
    for provider in providers:
        results[provider] = ingest_provider_docs(provider, config, vector_store)
    
    # Summary
    console.print("\n[bold blue]Ingestion Summary[/bold blue]")
    summary_table = Table(show_header=True, header_style="bold magenta")
    summary_table.add_column("Provider", style="cyan")
    summary_table.add_column("Status", style="white")
    summary_table.add_column("Collection/Table", style="yellow")
    
    for provider in providers:
        status = "✅ Success" if results[provider] else "❌ Failed"
        db_config = build_provider_db_config(config, provider, vector_store)
        
        if vector_store == "chroma":
            collection_name = db_config.get("chroma_collection_name", "N/A")
        else:  # duckdb
            collection_name = db_config.get("duckdb_table_name", "N/A")
            
        summary_table.add_row(provider.upper(), status, collection_name)
    
    console.print(summary_table)
    
    success_count = sum(results.values())
    if success_count == len(providers):
        console.print("\n[bold green]🎉 All documentation ingested successfully![/bold green]")
        console.print("You can now use Saturn with both GCP and AWS CLI documentation.")
        return 0
    else:
        console.print(f"\n[bold yellow]⚠️  {success_count}/{len(providers)} providers ingested successfully[/bold yellow]")
        return 1

if __name__ == "__main__":
    exit(main()) 