from rich.console import Console

from saturn.rag_engine import (RAGEngine, build_provider_db_config,
                               get_provider_docs_path)


# Mock LLM for HyDE (returns a canned hypothetical doc)
class MockLLM:
    def complete(self, prompt):
        return type(
            "Resp", (), {"text": f"[MOCK HYPOTHETICAL DOC]\n{prompt[:100]}..."}
        )()

    def __call__(self, prompt):
        return self.complete(prompt)


console = Console()


async def test_hyde_rag():
    provider = "gcp"
    config = {
        "chroma_db_path": "./db/chroma_db",
        "chroma_collection_name": "test_gcp_hyde",
        "duckdb_path": "./db/duckdb_store",
        "duckdb_file_name": "test_vectors_hyde.duckdb",
        "duckdb_table_name": "test_gcp_embeddings_hyde",
        "gcp_rag_docs_path": "./internal/tools/gcloud_online_docs_markdown",
        "aws_rag_docs_path": "./internal/tools/aws_cli_docs_markdown",
    }
    db_config = build_provider_db_config(config, provider, "chroma")
    docs_path = get_provider_docs_path(config, provider)

    # Use the mock LLM for HyDE
    hyde_llm = MockLLM()

    rag_engine_hyde = RAGEngine(
        vector_store_choice="chroma",
        db_config=db_config,
        embed_model_name="local:bge-small-en-v1.5",
        documents_path_for_init=docs_path,
        build_index_on_init=True,
        use_context_aware_parsing=True,
        use_hyde=True,
        hyde_llm=hyde_llm,
    )

    rag_engine_no_hyde = RAGEngine(
        vector_store_choice="chroma",
        db_config=db_config,
        embed_model_name="local:bge-small-en-v1.5",
        documents_path_for_init=docs_path,
        build_index_on_init=True,
        use_context_aware_parsing=True,
        use_hyde=False,
    )

    query = "How do I create a GCP VPC with custom subnets?"
    console.rule("[bold green]RAG with HyDE (GCP)")
    result_hyde = await rag_engine_hyde.query_docs(query, provider="gcp")
    console.print(result_hyde)

    console.rule("[bold blue]RAG without HyDE (GCP)")
    result_no_hyde = await rag_engine_no_hyde.query_docs(query, provider="gcp")
    console.print(result_no_hyde)

    # Repeat for AWS
    provider = "aws"
    db_config_aws = build_provider_db_config(config, provider, "chroma")
    docs_path_aws = get_provider_docs_path(config, provider)
    rag_engine_hyde_aws = RAGEngine(
        vector_store_choice="chroma",
        db_config=db_config_aws,
        embed_model_name="local:bge-small-en-v1.5",
        documents_path_for_init=docs_path_aws,
        build_index_on_init=True,
        use_context_aware_parsing=True,
        use_hyde=True,
        hyde_llm=hyde_llm,
    )
    rag_engine_no_hyde_aws = RAGEngine(
        vector_store_choice="chroma",
        db_config=db_config_aws,
        embed_model_name="local:bge-small-en-v1.5",
        documents_path_for_init=docs_path_aws,
        build_index_on_init=True,
        use_context_aware_parsing=True,
        use_hyde=False,
    )
    query_aws = "How do I create an S3 bucket with versioning enabled?"
    console.rule("[bold green]RAG with HyDE (AWS)")
    result_hyde_aws = await rag_engine_hyde_aws.query_docs(query_aws, provider="aws")
    console.print(result_hyde_aws)
    console.rule("[bold blue]RAG without HyDE (AWS)")
    result_no_hyde_aws = await rag_engine_no_hyde_aws.query_docs(
        query_aws, provider="aws"
    )
    console.print(result_no_hyde_aws)


if __name__ == "__main__":
    import asyncio

    asyncio.run(test_hyde_rag())
