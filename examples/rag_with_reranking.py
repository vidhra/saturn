#!/usr/bin/env python3
"""
Example: Using RAG Engine with LLM Reranking

This example demonstrates how to use the RAG engine with LLM reranking
to improve document retrieval quality for CLI documentation queries.
"""

import os
import sys
from typing import Optional

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from rich.console import Console
from rich.panel import Panel

from saturn.rag_engine import (RAGEngine, build_provider_db_config,
                               get_provider_docs_path)

console = Console()


def create_rag_engine_with_reranking(
    provider: str = "gcp",
    vector_store: str = "chroma",
    embed_model: str = "models/text-embedding-004",
    google_api_key: Optional[str] = None,
    use_reranking: bool = True,
    rerank_top_n: int = 15,
    llm_for_reranking: Optional[str] = None,
) -> RAGEngine:
    """
    Creates a RAG engine with LLM reranking enabled.

    Args:
        provider: Cloud provider ("gcp" or "aws")
        vector_store: Vector store choice ("chroma" or "duckdb")
        embed_model: Embedding model to use
        google_api_key: API key for Google embeddings/LLM
        use_reranking: Whether to enable LLM reranking
        rerank_top_n: Number of documents to retrieve before reranking
        llm_for_reranking: LLM to use for reranking (if different from default)

    Returns:
        Configured RAG engine instance
    """

    config = {
        "chroma_db_path": "./db/chroma_db",
        "chroma_collection_name": f"{provider}_cli_docs_rerank",
        "duckdb_path": "./db/duckdb_store",
        "duckdb_file_name": "vector_store_rerank.duckdb",
        "duckdb_table_name": f"{provider}_cli_embeddings_rerank",
    }

    db_config = build_provider_db_config(config, provider, vector_store)
    docs_path = get_provider_docs_path(config, provider)

    console.print(
        f"[green]Setting up RAG engine for {provider.upper()} with LLM reranking[/green]"
    )
    console.print(f"Vector store: {vector_store}")
    console.print(f"Embedding model: {embed_model}")
    console.print(f"Docs path: {docs_path}")
    console.print(f"LLM reranking: {'enabled' if use_reranking else 'disabled'}")

    llm_for_settings = None
    if use_reranking and llm_for_reranking:
        try:
            if llm_for_reranking.startswith("gpt-"):
                from llama_index.llms.openai import OpenAI

                llm_for_settings = OpenAI(model=llm_for_reranking)
                console.print(
                    f"Configured OpenAI LLM for reranking: {llm_for_reranking}"
                )
        except ImportError as e:
            console.print(
                f"[yellow]Warning: Could not configure LLM {llm_for_reranking}: {e}[/yellow]"
            )

    # Create RAG engine
    rag_engine = RAGEngine(
        vector_store_choice=vector_store,
        db_config=db_config,
        embed_model_name=embed_model,
        google_api_key=google_api_key,
        llm_for_settings=llm_for_settings,
        documents_path_for_init=docs_path,
        build_index_on_init=True,
        use_context_aware_parsing=True,
        use_llm_rerank=use_reranking,
        rerank_top_n=rerank_top_n,
        rerank_choice_batch_size=5,
        max_chunk_size=1024,
        chunk_overlap=100,
    )

    return rag_engine


def compare_with_without_reranking(query: str, rag_engine: RAGEngine):
    """
    Demonstrates the difference between queries with and without reranking.
    """
    console.print(
        Panel.fit(f"[bold blue]Query:[/bold blue] {query}", border_style="blue")
    )

    if rag_engine.use_llm_rerank:
        console.print("\n[green]🔄 Results WITH LLM Reranking:[/green]")
        results_with_rerank = rag_engine.query_docs(query, min_similarity_score=0.4)
        console.print(
            results_with_rerank[:1000] + "..."
            if len(results_with_rerank) > 1000
            else results_with_rerank
        )

        rag_engine.update_rerank_settings(use_llm_rerank=False)
        console.print("\n[yellow]📄 Results WITHOUT LLM Reranking:[/yellow]")
        results_without_rerank = rag_engine.query_docs(query, min_similarity_score=0.4)
        console.print(
            results_without_rerank[:1000] + "..."
            if len(results_without_rerank) > 1000
            else results_without_rerank
        )

        rag_engine.update_rerank_settings(use_llm_rerank=True)
    else:
        console.print("\n[yellow]📄 Results (Reranking Disabled):[/yellow]")
        results = rag_engine.query_docs(query, min_similarity_score=0.4)
        console.print(results[:1000] + "..." if len(results) > 1000 else results)


def main():
    """Main example function."""

    console.print(
        Panel.fit(
            "[bold green]RAG Engine with LLM Reranking Example[/bold green]\n\n"
            "This example shows how to use LLM reranking to improve\n"
            "document retrieval quality for CLI documentation queries.",
            border_style="green",
        )
    )

    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        console.print(
            "[red]Warning: GOOGLE_API_KEY not found. Make sure to set it for Google embeddings.[/red]"
        )

    test_queries = [
        "How do I create a storage bucket with specific permissions?",
        "What are the options for configuring compute instance machine types?",
        "How to list all available regions and zones?",
        "What are the best practices for IAM role management?",
        "How to enable billing alerts and monitoring?",
    ]

    try:
        rag_engine = create_rag_engine_with_reranking(
            provider="gcp",
            vector_store="chroma",
            embed_model="local:BAAI/bge-small-en-v1.5",
            google_api_key=google_api_key,
            use_reranking=True,
            rerank_top_n=12,
        )

        if not rag_engine._is_initialized_properly:
            console.print(
                "[red]Failed to initialize RAG engine. Check configuration and dependencies.[/red]"
            )
            return

        console.print("[green]✅ RAG Engine initialized successfully![/green]\n")

        for i, query in enumerate(test_queries):
            console.print(f"\n{'='*60}")
            console.print(
                f"[bold cyan]Test Query {i+1}/{len(test_queries)}[/bold cyan]"
            )
            compare_with_without_reranking(query, rag_engine)

            if i < len(test_queries) - 1:
                input("\nPress Enter to continue to next query...")

        console.print(f"\n{'='*60}")
        console.print("[bold green]Interactive Mode[/bold green]")
        console.print("Enter your own queries (type 'quit' to exit):")

        while True:
            try:
                user_query = input("\n🔍 Your query: ").strip()
                if user_query.lower() in ["quit", "exit", "q"]:
                    break
                if not user_query:
                    continue

                compare_with_without_reranking(user_query, rag_engine)

            except KeyboardInterrupt:
                console.print("\n[yellow]Interrupted by user.[/yellow]")
                break

        console.print(f"\n{'='*60}")
        console.print(
            "[bold blue]Demonstrating Dynamic Rerank Settings Update[/bold blue]"
        )

        test_query = "How to create a virtual machine instance?"

        settings_to_test = [
            {"rerank_top_n": 5, "rerank_choice_batch_size": 3},
            {"rerank_top_n": 20, "rerank_choice_batch_size": 10},
            {"use_llm_rerank": False},
        ]

        for settings in settings_to_test:
            console.print(f"\n[cyan]Testing with settings: {settings}[/cyan]")
            rag_engine.update_rerank_settings(**settings, similarity_top_k=5)
            result = rag_engine.query_docs(test_query, min_similarity_score=0.4)
            console.print(result[:500] + "..." if len(result) > 500 else result)

    except Exception as e:
        console.print(f"[red]Error in main execution: {e}[/red]")
        import traceback

        traceback.print_exc()

    console.print("\n[green]Example completed![/green]")


if __name__ == "__main__":
    main()
