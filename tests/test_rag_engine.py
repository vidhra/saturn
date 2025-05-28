#!/usr/bin/env python3
"""
Comprehensive test script for RAG Engine functionality.
Tests different vector stores, embedding models, and context-aware parsing.
"""

import os
import asyncio
import tempfile
import shutil
from pathlib import Path
from typing import Dict, Any, List
import json

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    
    # Look for .env file in current directory and parent directories
    env_file_paths = [
        Path(".env"),
        Path("../.env"),
        Path("../../.env"),
        Path.cwd() / ".env",
        Path.cwd().parent / ".env",
        Path.cwd().parent.parent / ".env"
    ]
    
    env_loaded = False
    for env_path in env_file_paths:
        if env_path.exists():
            load_dotenv(env_path)
            print(f"📄 [RAG Test] Loaded environment variables from: {env_path.absolute()}")
            env_loaded = True
            break
    
    if not env_loaded:
        print("⚠️  [RAG Test] No .env file found. Using system environment variables only.")
        
except ImportError:
    print("⚠️  [RAG Test] python-dotenv not installed. Using system environment variables only.")

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Import RAG Engine components
from saturn.rag_engine import (
    RAGEngine, 
    CLIContextAwareParser,
    build_provider_db_config,
    get_provider_docs_path,
    DEFAULT_EMBED_MODEL_NAME,
    DEFAULT_CHROMA_PATH,
    DEFAULT_CHROMA_COLLECTION,
    DEFAULT_DUCKDB_PATH,
    DEFAULT_DUCKDB_DB_FILE_NAME,
    DEFAULT_DUCKDB_TABLE_NAME
)

console = Console()

class RAGEngineTestSuite:
    """Comprehensive test suite for RAG Engine functionality."""
    
    def __init__(self):
        self.test_results = {}
        self.temp_dirs = []
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        
        # Create test configuration
        self.test_config = {
            "gcp_rag_docs_path": self._get_test_docs_path("gcp"),
            "aws_rag_docs_path": self._get_test_docs_path("aws"),
            "vector_store": "chroma",
            "chroma_db_path": "./test_db/chroma_db",
            "gcp_chroma_collection_name": "test_gcp_docs",
            "aws_chroma_collection_name": "test_aws_docs",
            "duckdb_path": "./test_db/duckdb_store",
            "duckdb_file_name": "test_vectors.duckdb",
            "gcp_duckdb_table_name": "test_gcp_embeddings",
            "aws_duckdb_table_name": "test_aws_embeddings"
        }
        
        # Create sample test documents
        self._create_test_documents()
    
    def _get_test_docs_path(self, provider: str) -> str:
        """Get the path to test documentation."""
        if provider == "gcp":
            return os.path.join(os.path.dirname(__file__), '..', 'internal', 'tools', 'gcloud_online_docs_markdown')
        elif provider == "aws":
            return os.path.join(os.path.dirname(__file__), '..', 'internal', 'tools', 'aws_cli_docs_markdown')
        else:
            return ""
    
    def _create_test_documents(self):
        """Create sample test documents for testing."""
        # Create temporary directory for test documents
        self.test_docs_dir = tempfile.mkdtemp(prefix="rag_test_docs_")
        self.temp_dirs.append(self.test_docs_dir)
        
        # Sample GCP documentation
        gcp_docs = {
            "compute_instances.md": """
# gcloud compute instances

## NAME
gcloud compute instances - read and manipulate Compute Engine virtual machine instances

## SYNOPSIS
gcloud compute instances create INSTANCE_NAMES [--zone=ZONE] [--machine-type=MACHINE_TYPE]

## DESCRIPTION
Read and manipulate Compute Engine virtual machine instances.

## COMMANDS
### create
Create new virtual machine instances.

#### SYNOPSIS
```
gcloud compute instances create INSTANCE_NAMES [--zone=ZONE] [--machine-type=MACHINE_TYPE] [--image=IMAGE]
```

#### DESCRIPTION
Creates one or more Compute Engine virtual machine instances with the specified names.

#### EXAMPLES
Create a simple instance:
```bash
gcloud compute instances create my-instance --zone=us-central1-a
```

Create an instance with specific machine type:
```bash
gcloud compute instances create my-instance --zone=us-central1-a --machine-type=n1-standard-4
```

### list
List virtual machine instances.

#### SYNOPSIS
```
gcloud compute instances list [--zones=ZONES] [--filter=FILTER]
```

#### EXAMPLES
List all instances:
```bash
gcloud compute instances list
```

List instances in specific zone:
```bash
gcloud compute instances list --zones=us-central1-a
```
""",
            
            "storage_buckets.md": """
# gcloud storage buckets

## NAME
gcloud storage buckets - manage Cloud Storage buckets

## SYNOPSIS
gcloud storage buckets create gs://BUCKET_NAME [--location=LOCATION]

## DESCRIPTION
Create and manage Cloud Storage buckets.

## COMMANDS
### create
Create a new Cloud Storage bucket.

#### SYNOPSIS
```
gcloud storage buckets create gs://BUCKET_NAME [--location=LOCATION] [--storage-class=STORAGE_CLASS]
```

#### EXAMPLES
Create a bucket:
```bash
gcloud storage buckets create gs://my-bucket
```

Create a bucket in specific location:
```bash
gcloud storage buckets create gs://my-bucket --location=us-central1
```

### list
List Cloud Storage buckets.

#### EXAMPLES
```bash
gcloud storage buckets list
```
"""
        }
        
        # Write test documents
        for filename, content in gcp_docs.items():
            file_path = os.path.join(self.test_docs_dir, filename)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
        
        console.print(f"[RAG Test] Created test documents in: {self.test_docs_dir}")
    
    def print_env_status(self):
        """Print environment variable status for debugging."""
        console.print("\n🔧 [RAG Test] Environment Variable Status:")
        console.print("-" * 50)
        
        env_vars = {
            "GOOGLE_API_KEY": "Google Embeddings",
            "OPENAI_API_KEY": "OpenAI Embeddings",
            "RAG_EMBED_MODEL": "RAG Embedding Model"
        }
        
        for env_var, description in env_vars.items():
            value = os.getenv(env_var)
            if value:
                if "key" in env_var.lower() or "api" in env_var.lower():
                    masked_value = f"{value[:8]}...{value[-4:]}" if len(value) > 12 else f"{value[:4]}..."
                else:
                    masked_value = value
                console.print(f"✅ {description:20} ({env_var}): {masked_value}")
            else:
                console.print(f"❌ {description:20} ({env_var}): Not set")
        console.print("-" * 50)
    
    async def test_context_aware_parser(self) -> bool:
        """Test the CLI context-aware parser."""
        console.print("\n=== Testing CLI Context-Aware Parser ===")
        
        try:
            from llama_index.core.schema import Document
            
            # Create test document
            test_content = """
# gcloud compute instances create

## SYNOPSIS
gcloud compute instances create INSTANCE_NAMES [--zone=ZONE]

## DESCRIPTION
Creates virtual machine instances.

## OPTIONS
--zone=ZONE
    Zone for the instance

--machine-type=MACHINE_TYPE
    Machine type for the instance

## EXAMPLES
Create an instance:
```bash
gcloud compute instances create my-vm --zone=us-central1-a
```
"""
            
            doc = Document(text=test_content, metadata={"file_name": "test_compute.md"})
            
            # Test parser
            parser = CLIContextAwareParser(
                max_chunk_size=500,
                chunk_overlap=50,
                preserve_code_blocks=True,
                preserve_command_context=True
            )
            
            nodes = parser.get_nodes_from_documents([doc], show_progress=True)
            
            console.print(f"✅ Parser created {len(nodes)} nodes from test document")
            
            # Verify node content
            for i, node in enumerate(nodes):
                metadata = node.metadata or {}
                console.print(f"  Node {i+1}: '{metadata.get('section_title', 'Unknown')}' "
                           f"({len(node.text)} chars)")
            
            self.test_results["context_aware_parser"] = True
            return True
            
        except Exception as e:
            console.print(f"❌ Context-aware parser test failed: {e}")
            self.test_results["context_aware_parser"] = False
            return False
    
    async def test_in_memory_rag(self, embed_model: str = "local:BAAI/bge-small-en-v1.5") -> bool:
        """Test in-memory RAG with HuggingFace embeddings."""
        console.print(f"\n=== Testing In-Memory RAG ({embed_model}) ===")
        
        try:
            rag_engine = RAGEngine(
                vector_store_choice="default",
                documents_path_for_init=self.test_docs_dir,
                build_index_on_init=True,
                embed_model_name=embed_model,
                google_api_key=self.google_api_key,
                llm_for_settings=None,
                use_context_aware_parsing=True
            )
            
            if not rag_engine.query_engine:
                console.print("❌ In-memory RAG engine failed to initialize")
                self.test_results["in_memory_rag"] = False
                return False
            
            # Test query
            result = rag_engine.query_docs("How do I create a compute instance?")
            
            if result and "gcloud compute instances create" in result:
                console.print("✅ In-memory RAG query successful")
                console.print(Panel(result[:300] + "...", title="Query Result Preview", border_style="green"))
                self.test_results["in_memory_rag"] = True
                return True
            else:
                console.print("❌ In-memory RAG query returned unexpected result")
                self.test_results["in_memory_rag"] = False
                return False
                
        except Exception as e:
            console.print(f"❌ In-memory RAG test failed: {e}")
            self.test_results["in_memory_rag"] = False
            return False
    
    async def test_gemini_embeddings(self) -> bool:
        """Test RAG with Gemini embeddings."""
        console.print(f"\n=== Testing Gemini Embeddings ===")
        
        if not self.google_api_key:
            console.print("⚠️  Skipping Gemini embeddings test - GOOGLE_API_KEY not found")
            self.test_results["gemini_embeddings"] = "skipped"
            return True
        
        try:
            rag_engine = RAGEngine(
                vector_store_choice="default",
                documents_path_for_init=self.test_docs_dir,
                build_index_on_init=True,
                embed_model_name=DEFAULT_EMBED_MODEL_NAME,
                google_api_key=self.google_api_key,
                llm_for_settings=None,
                use_context_aware_parsing=True
            )
            
            if not rag_engine.query_engine:
                console.print("❌ Gemini embeddings RAG engine failed to initialize")
                self.test_results["gemini_embeddings"] = False
                return False
            
            # Test query
            result = rag_engine.query_docs("How do I list storage buckets?")
            
            if result and ("storage" in result.lower() or "bucket" in result.lower()):
                console.print("✅ Gemini embeddings RAG query successful")
                console.print(Panel(result[:300] + "...", title="Gemini Query Result Preview", border_style="magenta"))
                self.test_results["gemini_embeddings"] = True
                return True
            else:
                console.print("❌ Gemini embeddings RAG query returned unexpected result")
                self.test_results["gemini_embeddings"] = False
                return False
                
        except Exception as e:
            console.print(f"❌ Gemini embeddings test failed: {e}")
            self.test_results["gemini_embeddings"] = False
            return False
    
    async def test_chroma_vector_store(self) -> bool:
        """Test ChromaDB vector store."""
        console.print(f"\n=== Testing ChromaDB Vector Store ===")
        
        try:
            # Create test-specific database configuration
            chroma_config = {
                "chroma_path": "./test_db/chroma_test",
                "chroma_collection_name": "test_collection"
            }
            
            rag_engine = RAGEngine(
                vector_store_choice="chroma",
                db_config=chroma_config,
                embed_model_name="local:BAAI/bge-small-en-v1.5",
                llm_for_settings=None,
                use_context_aware_parsing=True
            )
            
            # Ingest documents
            success = rag_engine.ingest_and_build_index(
                documents_path=self.test_docs_dir,
                force_rebuild=True
            )
            
            if not success or not rag_engine.query_engine:
                console.print("❌ ChromaDB RAG engine failed to build index")
                self.test_results["chroma_vector_store"] = False
                return False
            
            # Test query
            result = rag_engine.query_docs("How to create compute instances with machine type?")
            
            if result and "machine-type" in result:
                console.print("✅ ChromaDB vector store test successful")
                console.print(Panel(result[:300] + "...", title="ChromaDB Query Result Preview", border_style="blue"))
                self.test_results["chroma_vector_store"] = True
                return True
            else:
                console.print("❌ ChromaDB vector store query returned unexpected result")
                self.test_results["chroma_vector_store"] = False
                return False
                
        except Exception as e:
            console.print(f"❌ ChromaDB vector store test failed: {e}")
            self.test_results["chroma_vector_store"] = False
            return False
    
    async def test_duckdb_vector_store(self) -> bool:
        """Test DuckDB vector store."""
        console.print(f"\n=== Testing DuckDB Vector Store ===")
        
        try:
            # Create test-specific database configuration
            duckdb_config = {
                "duckdb_path": "./test_db/duckdb_test",
                "duckdb_file_name": "test_vectors.duckdb",
                "duckdb_table_name": "test_embeddings"
            }
            
            rag_engine = RAGEngine(
                vector_store_choice="duckdb",
                db_config=duckdb_config,
                embed_model_name="local:BAAI/bge-small-en-v1.5",
                llm_for_settings=None,
                use_context_aware_parsing=True
            )
            
            # Ingest documents
            success = rag_engine.ingest_and_build_index(
                documents_path=self.test_docs_dir,
                force_rebuild=True
            )
            
            if not success or not rag_engine.query_engine:
                console.print("❌ DuckDB RAG engine failed to build index")
                self.test_results["duckdb_vector_store"] = False
                return False
            
            # Test query
            result = rag_engine.query_docs("List all instances in a zone")
            
            if result and ("list" in result.lower() or "zone" in result.lower()):
                console.print("✅ DuckDB vector store test successful")
                console.print(Panel(result[:300] + "...", title="DuckDB Query Result Preview", border_style="cyan"))
                self.test_results["duckdb_vector_store"] = True
                return True
            else:
                console.print("❌ DuckDB vector store query returned unexpected result")
                self.test_results["duckdb_vector_store"] = False
                return False
                
        except Exception as e:
            console.print(f"❌ DuckDB vector store test failed: {e}")
            self.test_results["duckdb_vector_store"] = False
            return False
    
    async def test_provider_specific_configs(self) -> bool:
        """Test provider-specific database configurations."""
        console.print(f"\n=== Testing Provider-Specific Configurations ===")
        
        try:
            # Test GCP configuration
            gcp_chroma_config = build_provider_db_config(self.test_config, "gcp", "chroma")
            aws_chroma_config = build_provider_db_config(self.test_config, "aws", "chroma")
            
            gcp_duckdb_config = build_provider_db_config(self.test_config, "gcp", "duckdb")
            aws_duckdb_config = build_provider_db_config(self.test_config, "aws", "duckdb")
            
            # Verify configurations are different
            assert gcp_chroma_config["chroma_collection_name"] != aws_chroma_config["chroma_collection_name"]
            assert gcp_duckdb_config["duckdb_table_name"] != aws_duckdb_config["duckdb_table_name"]
            
            console.print("✅ Provider-specific configurations test passed")
            console.print(f"  GCP Chroma: {gcp_chroma_config['chroma_collection_name']}")
            console.print(f"  AWS Chroma: {aws_chroma_config['chroma_collection_name']}")
            console.print(f"  GCP DuckDB: {gcp_duckdb_config['duckdb_table_name']}")
            console.print(f"  AWS DuckDB: {aws_duckdb_config['duckdb_table_name']}")
            
            self.test_results["provider_configs"] = True
            return True
            
        except Exception as e:
            console.print(f"❌ Provider-specific configurations test failed: {e}")
            self.test_results["provider_configs"] = False
            return False
    
    async def test_query_similarity_filtering(self) -> bool:
        """Test query result similarity filtering."""
        console.print(f"\n=== Testing Query Similarity Filtering ===")
        
        try:
            rag_engine = RAGEngine(
                vector_store_choice="default",
                documents_path_for_init=self.test_docs_dir,
                build_index_on_init=True,
                embed_model_name="local:BAAI/bge-small-en-v1.5",
                llm_for_settings=None,
                use_context_aware_parsing=True
            )
            
            if not rag_engine.query_engine:
                console.print("❌ RAG engine failed to initialize for similarity test")
                self.test_results["similarity_filtering"] = False
                return False
            
            # Test with high similarity threshold (should return relevant results)
            result_high = rag_engine.query_docs("create compute instance", min_similarity_score=0.1)
            
            # Test with very high similarity threshold (should return fewer/no results)
            result_low = rag_engine.query_docs("create compute instance", min_similarity_score=0.95)
            
            # High threshold should return content, very high threshold might not
            has_results_high = result_high and len(result_high) > 100
            has_results_low = result_low and len(result_low) > 100
            
            if has_results_high:
                console.print("✅ Query similarity filtering test passed")
                console.print(f"  Low threshold (0.1): {len(result_high)} chars")
                console.print(f"  High threshold (0.95): {len(result_low)} chars")
                self.test_results["similarity_filtering"] = True
                return True
            else:
                console.print("❌ Query similarity filtering test failed - no results with low threshold")
                self.test_results["similarity_filtering"] = False
                return False
                
        except Exception as e:
            console.print(f"❌ Query similarity filtering test failed: {e}")
            self.test_results["similarity_filtering"] = False
            return False
    
    def cleanup(self):
        """Clean up temporary directories and test databases."""
        console.print("\n🧹 Cleaning up test resources...")
        
        # Clean up temporary directories
        for temp_dir in self.temp_dirs:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
                console.print(f"  Removed: {temp_dir}")
        
        # Clean up test databases
        test_db_paths = ["./test_db"]
        for db_path in test_db_paths:
            if os.path.exists(db_path):
                shutil.rmtree(db_path)
                console.print(f"  Removed: {db_path}")
    
    def print_summary(self):
        """Print test results summary."""
        console.print("\n📊 Test Results Summary")
        console.print("=" * 60)
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Test", style="cyan", no_wrap=True)
        table.add_column("Status", style="bold")
        table.add_column("Details")
        
        for test_name, result in self.test_results.items():
            if result is True:
                status = "[green]✅ PASSED[/green]"
                details = "Test completed successfully"
            elif result is False:
                status = "[red]❌ FAILED[/red]"
                details = "Test failed - check logs above"
            elif result == "skipped":
                status = "[yellow]⏭️ SKIPPED[/yellow]"
                details = "Test skipped (missing requirements)"
            else:
                status = "[dim]❓ UNKNOWN[/dim]"
                details = str(result)
            
            table.add_row(test_name.replace("_", " ").title(), status, details)
        
        console.print(table)
        
        # Calculate pass rate
        passed = sum(1 for r in self.test_results.values() if r is True)
        total = len([r for r in self.test_results.values() if r != "skipped"])
        skipped = sum(1 for r in self.test_results.values() if r == "skipped")
        
        console.print(f"\n📈 Results: {passed}/{total} tests passed")
        if skipped > 0:
            console.print(f"   {skipped} tests skipped")
        
        if passed == total:
            console.print("[bold green]🎉 All tests passed![/bold green]")
        elif passed > total * 0.7:
            console.print("[yellow]⚠️  Most tests passed, some issues found[/yellow]")
        else:
            console.print("[bold red]❌ Multiple test failures detected[/bold red]")

async def main():
    """Main test function."""
    console.print("🧪 RAG Engine Test Suite")
    console.print("=" * 60)
    
    test_suite = RAGEngineTestSuite()
    
    try:
        # Show environment status
        test_suite.print_env_status()
        
        # Run all tests
        console.print("\n🚀 Starting RAG Engine Tests...")
        
        await test_suite.test_context_aware_parser()
        await test_suite.test_in_memory_rag()
        await test_suite.test_gemini_embeddings()
        await test_suite.test_chroma_vector_store()
        await test_suite.test_duckdb_vector_store()
        await test_suite.test_provider_specific_configs()
        await test_suite.test_query_similarity_filtering()
        
        # Print summary
        test_suite.print_summary()
        
    except KeyboardInterrupt:
        console.print("\n⚠️  Tests interrupted by user")
    except Exception as e:
        console.print(f"\n💥 Unexpected error during testing: {e}")
        console.print_exception(show_locals=False)
    finally:
        # Always clean up
        test_suite.cleanup()
        console.print("\n✅ Test suite completed")

if __name__ == "__main__":
    asyncio.run(main()) 