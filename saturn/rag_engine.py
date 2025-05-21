import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.llms import LLM # For type hinting, can also be used to set Settings.llm = None
from llama_index.core.embeddings import BaseEmbedding # For type hinting and explicit None
# For local embeddings, if you don't want to rely on OpenAI for embeddings:
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# For local LLM for LlamaIndex synthesis (optional, if not just using it for retrieval)
# from llama_index.llms.ollama import Ollama 

# Using rich console for logging within the RAG engine itself
from rich.console import Console
from rich.panel import Panel # For example usage
from typing import Dict, Any, Optional, List
console = Console()

# Updated default embedding model name to a standard, correctly formatted Gemini model
DEFAULT_EMBED_MODEL_NAME = "models/text-embedding-004" 

# Chroma Defaults
DEFAULT_CHROMA_PATH = "./db/chroma_db"
DEFAULT_CHROMA_COLLECTION = "gclouddocs"
# DuckDB Defaults
DEFAULT_DUCKDB_PATH = "./db/duckdb_store"
DEFAULT_DUCKDB_DB_FILE_NAME = "vector_store.duckdb" # DuckDB file name
DEFAULT_DUCKDB_TABLE_NAME = "gclouddocs_embeddings"

# Default LlamaIndex settings to be applied early
DEFAULT_CONTEXT_WINDOW = 65536 # Increased default
DEFAULT_CHUNK_SIZE = 2048     # Reduced chunk size for potentially better granularity
DEFAULT_CHUNK_OVERLAP_RATIO = 0.25 # 10% overlap

class RAGEngine:
    """Handles loading documentation, building/loading an index, and querying it using LlamaIndex."""

    def __init__(self, 
                 vector_store_choice: str = "default", 
                 db_config: Optional[Dict[str, Any]] = None,
                 embed_model_name: str = DEFAULT_EMBED_MODEL_NAME,
                 google_api_key: Optional[str] = None, # Added for Gemini API key
                 documents_path_for_init: Optional[str] = None, # If in-memory, docs are needed at init
                 build_index_on_init: bool = False, # Controls if index is built from docs_path_for_init
                 # Pass llm=None from LlamaIndex if you want to avoid OpenAI default
                 # Or pass your app's LLM instance if RAG needs to synthesize
                 llm_for_settings: Optional[LLM] = None 
                 ):
        """
        Initializes the RAGEngine, sets up embedding model and vector store client.
        Optionally loads documents and builds an index if specified (mainly for in-memory or initial setup).

        Args:
            vector_store_choice (str): "default" (in-memory), "chroma", "duckdb".
            db_config (Optional[Dict[str, Any]]): Configuration for the chosen database.
            embed_model_name (str): Name of the embedding model to use.
            google_api_key (Optional[str]): API key for Gemini embeddings.
            documents_path_for_init (Optional[str]): Path to documents for initial in-memory index or if build_index_on_init is True.
            build_index_on_init (bool): If True, attempts to build index from documents_path_for_init.
            llm_for_settings (Optional[LLM]): An LLM instance for LlamaIndex Settings, or None to disable its LLM.
        """
        self.index: Optional[VectorStoreIndex] = None
        self.query_engine = None
        self.db_config = db_config if db_config else {}
        self.vector_store_choice = vector_store_choice.lower()
        self.storage_context: Optional[StorageContext] = None
        self.vector_store: Optional[Any] = None # Will hold ChromaVectorStore or DuckDBVectorStore instance
        self._is_initialized_properly = False # Flag to check successful init

        console.print(f"[RAG Engine] Initializing RAGEngine.")
        console.print(f"[RAG Engine] Vector store choice: {self.vector_store_choice}")
        console.print(f"[RAG Engine] Attempting to use embedding model identifier: {embed_model_name}")

        try:
            # 0. Configure LlamaIndex Global Settings
            if llm_for_settings is None:
                # console.print("[RAG Engine] Setting LlamaIndex Settings.llm to None. Observability may be affected.")
                Settings.llm = None # Primary way to avoid default OpenAI LLM for synthesis
                # Settings.global_handler = None # This line caused "Eval mode None not supported"
            elif llm_for_settings: 
                Settings.llm = llm_for_settings
                console.print(f"[RAG Engine] LlamaIndex Settings.llm configured with provided LLM: {type(llm_for_settings).__name__}")

            # Set context window and chunk size globally for LlamaIndex
            # These are applied before embedding model, as some tokenizers might be influenced
            Settings.context_window = DEFAULT_CONTEXT_WINDOW
            Settings.chunk_size = 2048
            Settings.chunk_overlap = 204  # 10% of 2048
            console.print(f"[RAG Engine] Set LlamaIndex Settings: context_window={Settings.context_window}, chunk_size={Settings.chunk_size}, chunk_overlap={Settings.chunk_overlap}")

            # 1. Configure Embeddings - CRUCIAL for RAG
            embedding_model_configured = False
            effective_google_api_key = google_api_key or os.getenv("GOOGLE_API_KEY")
            
            # Debug printing with safe handling of None values
            print(f"\n[RAG Engine Debug] API Key Sources:")
            if google_api_key:
                print(f"  - Direct google_api_key param: {google_api_key[:5]}...{google_api_key[-4:]}")
            else:
                print("  - Direct google_api_key param: None")
                
            env_key = os.getenv("GOOGLE_API_KEY")
            if env_key:
                print(f"  - From os.environ: {env_key[:5]}...{env_key[-4:]}")
            else:
                print("  - From os.environ: None")
                
            if effective_google_api_key:
                print(f"  - Effective key chosen: {effective_google_api_key[:5]}...{effective_google_api_key[-4:]}")
            else:
                print("  - Effective key chosen: None")

            # Standardize model name format for Google models
            final_google_model_name = embed_model_name
            
            if "gemini" in embed_model_name.lower() or "embedding-" in embed_model_name.lower() or embed_model_name.startswith("models/") or embed_model_name.startswith("text-"):
                if not (embed_model_name.startswith("models/") or embed_model_name.startswith("tunedModels/")):
                    if "embedding-001" in embed_model_name or \
                       "text-embedding-" in embed_model_name or \
                       "gemini-embedding-exp-03-07" in embed_model_name: 
                        final_google_model_name = f"models/{embed_model_name}" 
                        console.print(f"[RAG Engine] [yellow]Info:[/] Auto-prefixed Google model name to: {final_google_model_name}")
            print(f"embed_model_name: {embed_model_name}")
            is_google_model_candidate =  final_google_model_name.startswith("models/")
            print(f"is_google_model_candidate: {is_google_model_candidate}")
            print(f"final_google_model_name: {final_google_model_name}")
            print(f"starts with local:: {final_google_model_name.startswith('local:')}")
            
            if is_google_model_candidate and not final_google_model_name.startswith("local:"):
                console.print(f"[RAG Engine] Configuring Google (PaLM/Vertex/Gemini) embedding model: {final_google_model_name}")
                if not effective_google_api_key:
                    console.print("[RAG Engine] [bold red]Error:[/] GOOGLE_API_KEY not provided for Google embeddings.")
                    console.print("[RAG Engine] Please set the GOOGLE_API_KEY environment variable or provide it in config.yaml")
                    return
                console.print(f"[RAG Engine Debug] Effective GOOGLE_API_KEY being used: {effective_google_api_key[:5]}...{effective_google_api_key[-4:] if effective_google_api_key and len(effective_google_api_key) > 9 else 'KEY_TOO_SHORT_OR_NONE'}")
                try:
                    from llama_index.embeddings.google_genai import GoogleGenAIEmbedding 
                    print(f"[RAG Engine Debug] Creating GoogleGenAIEmbedding with:")
                    print(f"  - model_name: {final_google_model_name}")
                    print(f"  - api_key: {effective_google_api_key[:5]}...{effective_google_api_key[-4:]}")
                    print(f"  - embed_batch_size: 4")

                    Settings.embed_model = GoogleGenAIEmbedding(
                        model_name=final_google_model_name,
                        api_key=effective_google_api_key,
                        embed_batch_size=64  # Try 4, or 1 if needed
                    )
                    console.print(f"[RAG Engine] Configured GoogleGenAIEmbedding model: {final_google_model_name} with batch size 4")
                    embedding_model_configured = True
                except ImportError:
                    console.print("[RAG Engine] [bold red]Error:[/] `llama-index-embeddings-google-genai` or its dependencies not installed. Please install it.")
                except Exception as e_google_embed:
                    console.print(f"[RAG Engine] [bold red]Error initializing GoogleGenAIEmbedding model '{final_google_model_name}':[/] {e_google_embed}")
                    print(f"[RAG Engine Debug] Full error details: {str(e_google_embed)}")
                    if hasattr(e_google_embed, '__cause__'):
                        print(f"[RAG Engine Debug] Caused by: {str(e_google_embed.__cause__)}")
            elif embed_model_name.startswith("local:"):
                hf_model_name = embed_model_name.split("local:", 1)[1]
                try:
                    from llama_index.embeddings.huggingface import HuggingFaceEmbedding 
                    Settings.embed_model = HuggingFaceEmbedding(model_name=hf_model_name)
                    console.print(f"[RAG Engine] Configured local HuggingFace embedding model: {hf_model_name}")
                    embedding_model_configured = True
                except ImportError:
                    console.print(f"[RAG Engine] [bold red]Error:[/] `llama-index-embeddings-huggingface` not installed.")
                except Exception as e_hf_embed:
                    console.print(f"[RAG Engine] [bold red]Error initializing local HuggingFace model '{hf_model_name}':[/] {e_hf_embed}")
            elif embed_model_name and embed_model_name != "default": 
                try:
                    Settings.embed_model = embed_model_name 
                    console.print(f"[RAG Engine] Attempting to use explicitly named embedding model: {embed_model_name}")
                    embedding_model_configured = True 
                except Exception as e_named_embed:
                    console.print(f"[RAG Engine] [bold red]Error setting named embedding model '{embed_model_name}':[/] {e_named_embed}")
            else: 
                 console.print(f"[RAG Engine] [bold yellow]Warning:[/] Using LlamaIndex default embedding model resolution. If OPENAI_API_KEY is not set, this may fail.")
                 Settings.embed_model = "default" 
                 embedding_model_configured = True 

            if not embedding_model_configured:
                console.print("[RAG Engine] [bold red]CRITICAL:[/] Embedding model could not be configured. RAG engine will not be functional.")
                return # Stop initialization if no embedding model is set up

            # 2. Setup Vector Store Client/Connection
            if self.vector_store_choice == "chroma":
                console.print("[RAG Engine] Setting up ChromaDB vector store client...")
                try:
                    import chromadb
                    from llama_index.vector_stores.chroma import ChromaVectorStore
                    chroma_path = self.db_config.get("chroma_path", DEFAULT_CHROMA_PATH)
                    collection_name = self.db_config.get("chroma_collection_name", DEFAULT_CHROMA_COLLECTION)
                    console.print(f"[RAG Engine] ChromaDB path: {chroma_path}, Collection: {collection_name}")
                    os.makedirs(chroma_path, exist_ok=True)
                    
                    db = chromadb.PersistentClient(path=chroma_path)
                    chroma_collection = db.get_or_create_collection(collection_name)
                    self.vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
                    self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
                    console.print(f"[RAG Engine] ChromaDB client setup. Collection '{collection_name}' ready.")
                    # Try to load existing index metadata from this store
                    if chroma_collection.count() > 0 and not build_index_on_init:
                        console.print(f"[RAG Engine] Attempting to load index from existing Chroma collection.")
                        self.index = VectorStoreIndex.from_vector_store(self.vector_store, storage_context=self.storage_context)
                        console.print(f"[RAG Engine] Index loaded from ChromaDB.")
                except ImportError:
                    console.print("[RAG Engine] [bold red]Error:[/] ChromaDB deps not found. Fallback to default in-memory.")
                    self.vector_store_choice = "default"
                except Exception as e_chroma:
                    console.print(f"[RAG Engine] [bold red]Error setting up ChromaDB:[/] {e_chroma}. Fallback to default.")
                    self.vector_store_choice = "default"
            
            elif self.vector_store_choice == "duckdb":
                console.print("[RAG Engine] Setting up DuckDB vector store client...")
                try:
                    import duckdb 
                    from llama_index.vector_stores.duckdb import DuckDBVectorStore
                    duckdb_dir = self.db_config.get("duckdb_path", DEFAULT_DUCKDB_PATH)
                    db_file = self.db_config.get("duckdb_file_name", DEFAULT_DUCKDB_DB_FILE_NAME)
                    table_name = self.db_config.get("duckdb_table_name", DEFAULT_DUCKDB_TABLE_NAME)
                    os.makedirs(duckdb_dir, exist_ok=True)
                    full_duckdb_path = os.path.join(duckdb_dir, db_file)
                    console.print(f"[RAG Engine] DuckDB file: {full_duckdb_path}, Table: {table_name}")
                    
                    self.vector_store = DuckDBVectorStore(database_path=full_duckdb_path, table_name=table_name)
                    self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
                    console.print(f"[RAG Engine] DuckDB client setup. Table '{table_name}' will be used/created.")
                    # Try to load existing index metadata from this store
                    # DuckDBVectorStore handles table creation; from_vector_store checks if it can load.
                    if not build_index_on_init:
                        try:
                            console.print(f"[RAG Engine] Attempting to load index from existing DuckDB table.")
                            self.index = VectorStoreIndex.from_vector_store(self.vector_store, storage_context=self.storage_context)
                            console.print(f"[RAG Engine] Index loaded from DuckDB.")
                        except Exception as e_duck_load_idx:
                            console.print(f"[RAG Engine] Index not found or error loading from DuckDB table '{table_name}' ({e_duck_load_idx}). Will build if documents provided.")
                except ImportError:
                    console.print("[RAG Engine] [bold red]Error:[/] DuckDB deps not found. Fallback to default in-memory.")
                    self.vector_store_choice = "default"
                except Exception as e_duck:
                    console.print(f"[RAG Engine] [bold red]Error setting up DuckDB:[/] {e_duck}. Fallback to default.")
                    self.vector_store_choice = "default"

            # If build_index_on_init is True, or if it's an in-memory store (which always needs docs at init)
            if build_index_on_init and documents_path_for_init:
                self.ingest_and_build_index(documents_path_for_init, force_rebuild=False) # Pass force_rebuild=False here
            elif self.vector_store_choice == "default" and documents_path_for_init:
                 console.print("[RAG Engine] Building in-memory index from provided documents_path_for_init.")
                 self.ingest_and_build_index(documents_path_for_init, force_rebuild=False) # In-memory always rebuilds
            
            if self.index:
                # Pass llm=None explicitly to as_query_engine if Settings.llm is None
                current_llm_setting = Settings.llm
                self.query_engine = self.index.as_query_engine(similarity_top_k=6, llm=current_llm_setting)
                console.print(f"[RAG Engine] Query engine initialized (using LLM: {type(current_llm_setting).__name__ if current_llm_setting else 'None'}).")
                self._is_initialized_properly = True
            else:
                console.print("[RAG Engine] Index not yet available. Query engine not initialized. Use ingest_and_build_index() or check init flags.")

        except Exception as e:
            console.print(f"[RAG Engine] [bold red]Critical error during RAGEngine __init__:[/] {e}")
            console.print_exception(show_locals=False)

    def ingest_and_build_index(self, documents_path: str, force_rebuild: bool = False) -> bool:
        """
        Loads documents from the given path and builds/updates the vector store index.

        Args:
            documents_path (str): Path to the directory containing Markdown documents.
            force_rebuild (bool): If True, attempts to clear existing persistent store before building.
                                  For in-memory, it always rebuilds.
        Returns:
            bool: True if index building was successful, False otherwise.
        """
        console.print(f"[RAG Engine] Starting ingestion from: {documents_path}")
        if not os.path.exists(documents_path):
            console.print(f"[RAG Engine] [bold red]Error:[/] Documents path for ingestion does not exist: {documents_path}")
            return False

        try:
            console.print(f"[RAG Engine] Loading documents for ingestion from {documents_path}...")
            reader = SimpleDirectoryReader(documents_path, required_exts=[".md"], recursive=True)
            documents = reader.load_data()
            if not documents:
                console.print(f"[RAG Engine] [bold yellow]Warning:[/] No documents found at {documents_path} for ingestion.")
                return False
            console.print(f"[RAG Engine] Loaded {len(documents)} documents for ingestion.")

            if self.vector_store_choice == "chroma" and force_rebuild:
                if self.vector_store and hasattr(self.vector_store, 'client') and hasattr(self.vector_store.client, 'delete_collection'):
                    collection_name = self.db_config.get("chroma_collection_name", DEFAULT_CHROMA_COLLECTION)
                    console.print(f"[RAG Engine] ChromaDB force_rebuild: Deleting collection '{collection_name}'...")
                    try:
                        self.vector_store.client.delete_collection(name=collection_name)
                        db = self.vector_store.client # Assuming PersistentClient
                        chroma_collection = db.get_or_create_collection(collection_name)
                        self.vector_store = type(self.vector_store)(chroma_collection=chroma_collection) # Re-init VectorStore adapter
                        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
                        console.print(f"[RAG Engine] ChromaDB collection '{collection_name}' re-created.")
                        self.index = None # Ensure index is rebuilt
                    except Exception as e_delete_chroma:
                        console.print(f"[RAG Engine] [bold red]Error deleting/re-creating Chroma collection '{collection_name}':[/] {e_delete_chroma}")
                        # Proceeding might lead to duplicate data if not handled carefully
            elif self.vector_store_choice == "duckdb" and force_rebuild:
                if self.vector_store and hasattr(self.vector_store, '_conn'):
                    table_name = self.db_config.get("duckdb_table_name", DEFAULT_DUCKDB_TABLE_NAME)
                    console.print(f"[RAG Engine] DuckDB force_rebuild: Dropping table '{table_name}'...")
                    try:
                        self.vector_store._conn.execute(f"DROP TABLE IF EXISTS \"{table_name}\"")
                        console.print(f"[RAG Engine] DuckDB table '{table_name}' dropped.")
                        self.index = None # Ensure index is rebuilt
                         # Re-initialize vector_store for a fresh start if needed, though from_documents should handle table creation
                        # full_duckdb_path = os.path.join(self.db_config.get("duckdb_path", DEFAULT_DUCKDB_PATH), self.db_config.get("duckdb_file_name", DEFAULT_DUCKDB_DB_FILE_NAME))
                        # self.vector_store = type(self.vector_store)(database_path=full_duckdb_path, table_name=table_name)
                        # self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
                    except Exception as e_drop_duckdb:
                        console.print(f"[RAG Engine] [bold red]Error dropping DuckDB table '{table_name}':[/] {e_drop_duckdb}")
            
            # For in-memory ("default"), it always rebuilds from documents implicitly.
            # For persistent stores, if not force_rebuild, from_documents should add new/changed docs.
            
            console.print(f"[RAG Engine] Building/updating index with {len(documents)} documents for '{self.vector_store_choice}' store...")
            if self.vector_store_choice == "default" or not self.storage_context:
                # In-memory or if storage_context wasn't set up (e.g. error in persistent store setup)
                self.index = VectorStoreIndex.from_documents(documents, show_progress=True)
                console.print("[RAG Engine] Built new in-memory index.")
            else:
                # Persistent store (Chroma or DuckDB with existing storage_context)
                self.index = VectorStoreIndex.from_documents(
                    documents, 
                    storage_context=self.storage_context, 
                    show_progress=True
                )
                console.print(f"[RAG Engine] Index built/updated for {self.vector_store_choice}.")

            if self.index:
                # Pass llm=None explicitly to as_query_engine if Settings.llm is None
                current_llm_setting = Settings.llm
                self.query_engine = self.index.as_query_engine(similarity_top_k=6, llm=current_llm_setting)
                console.print(f"[RAG Engine] Query engine (re)initialized (using LLM: {type(current_llm_setting).__name__ if current_llm_setting else 'None'}).")
                self._is_initialized_properly = True # Mark as successfully initialized
                return True
            else:
                console.print("[RAG Engine] [bold red]Error:[/] Index build/update failed.")
                return False
        except Exception as e:
            console.print(f"[RAG Engine] [bold red]Error during document ingestion and index building:[/] {e}")
            console.print_exception(show_locals=False)
            return False

    def query_docs(self, query_text: str, min_similarity_score: float = 0.55) -> str:
        """
        Queries the indexed documents and returns a concatenated string of relevant text chunks.
        Filters results by a minimum similarity score if the retriever supports it.
        """
        if not self._is_initialized_properly or not self.query_engine:
            console.print("[RAG Engine] Query engine not properly initialized or index not built. Cannot query.")
            return "RAG Engine not available or failed to initialize. Please check logs or run ingestion."

        console.print(f"[RAG Engine] Querying with: '{query_text[:300]}...'")
        try:
            response = self.query_engine.query(query_text)
        except Exception as e:
            console.print(f"[RAG Engine] [bold red]Error during query:[/] {e}")
            return "Error occurred during RAG query."

        relevant_docs_parts = []
        if hasattr(response, 'source_nodes') and response.source_nodes:
            console.print(f"[RAG Engine] Retrieved {len(response.source_nodes)} source nodes.")
            for i, source_node in enumerate(response.source_nodes):
                score = source_node.get_score()
                text_content = source_node.get_text()
                metadata = source_node.node.metadata or {}
                file_name = metadata.get('file_name', 'N/A')
                
                display_score = f"{score:.2f}" if score is not None else "N/A"
                console.print(f"  [RAG Engine] Node {i+1}: Score={display_score}, File='{file_name}'")
                
                if score is None or score >= min_similarity_score:
                    relevant_docs_parts.append(f"---\nSource Document: {file_name} (Score: {display_score})\n---\n{text_content}\n\n")
                else:
                    console.print(f"  [RAG Engine] Node {i+1} from '{file_name}' skipped due to low score ({display_score} < {min_similarity_score}).")
            
            if not relevant_docs_parts:
                console.print("[RAG Engine] No documents met the minimum similarity score or no scores available.")
                if response.source_nodes:
                     top_node_text = response.source_nodes[0].get_text()
                     console.print("[RAG Engine] Returning text of the most relevant document as fallback.")
                     return f"Potentially relevant content (similarity score may be low or unavailable):\n{top_node_text}"
                return "No sufficiently relevant documents found."
        else:
            console.print("[RAG Engine] No source nodes retrieved from query response.")
            if response.response:
                console.print("[RAG Engine] Returning direct response from query engine.")
                return response.response
            return "No relevant documents found by RAG engine."

        return "".join(relevant_docs_parts)

# Example Usage (for testing this module directly):
if __name__ == '__main__':
    docs_dir = os.path.join(os.path.dirname(__file__), '..' , 'internal', 'tools', 'gcloud_online_docs_markdown')
    gemini_key_for_test = os.getenv("GOOGLE_API_KEY") # For Gemini embedding test

    if not os.path.isdir(docs_dir):
        console.print(f"[bold red]Error for example usage:[/] Documentation directory not found at expected path: {docs_dir}")
    else:
        console.print(f"[Example Usage] RAG Engine Test Script")
        console.print(f"Using document source: {docs_dir}")

        # --- Test In-Memory with default local HuggingFace embedding ---
        console.print("\n[bold]--- Testing In-Memory (HuggingFace Embeddings) ---[/bold]")
        rag_memory_hf = RAGEngine(
            vector_store_choice="default", 
            documents_path_for_init=docs_dir, 
            build_index_on_init=True, 
            llm_for_settings=None,
            embed_model_name="local:BAAI/bge-small-en-v1.5" # Explicitly test this
        )
        if rag_memory_hf.query_engine:
            console.print("[In-Memory HF] Querying for 'create instance'...")
            context_mem_hf = rag_memory_hf.query_docs("How to create a gcloud compute instance?")
            console.print(Panel(context_mem_hf, title="In-Memory HF: 'create instance'", border_style="blue", expand=False))
        else: console.print("[In-Memory HF] Failed to initialize.")

        # --- Test In-Memory with Gemini Embedding (if API key is available) ---
        console.print("\n[bold]--- Testing In-Memory (Gemini Embeddings) ---[/bold]")
        if gemini_key_for_test:
            rag_memory_gemini = RAGEngine(
                vector_store_choice="default", 
                documents_path_for_init=docs_dir, 
                build_index_on_init=True, 
                llm_for_settings=None,
                embed_model_name=DEFAULT_EMBED_MODEL_NAME, # This should be your Gemini model
                google_api_key=gemini_key_for_test
            )
            if rag_memory_gemini.query_engine:
                console.print("[In-Memory Gemini] Querying for 'create instance'...")
                context_mem_gemini = rag_memory_gemini.query_docs("How to create a gcloud compute instance?")
                console.print(Panel(context_mem_gemini, title="In-Memory Gemini: 'create instance'", border_style="magenta", expand=False))
            else: console.print("[In-Memory Gemini] Failed to initialize.")
        else:
            console.print("[Example Usage] GOOGLE_API_KEY not found in env. Skipping Gemini embedding test.")

        # --- Test ChromaDB --- 
        console.print("\n[bold]--- Testing ChromaDB Vector Store (using Gemini Embeddings if key provided) ---[/bold]")
        chroma_test_config = {"chroma_path": "./db/test_chroma_example", "chroma_collection_name": "example_collection_gemini_test"}
        console.print("(ChromaDB first run - building index...)")
        rag_chroma = RAGEngine(vector_store_choice="chroma", db_config=chroma_test_config, llm_for_settings=None, embed_model_name=DEFAULT_EMBED_MODEL_NAME, google_api_key=gemini_key_for_test)
        ingest_success_chroma = rag_chroma.ingest_and_build_index(documents_path=docs_dir, force_rebuild=True)
        if ingest_success_chroma and rag_chroma.query_engine:
            console.print("[ChromaDB] Querying for 'list machine types'...")
            context_chroma = rag_chroma.query_docs("list available machine types in a zone")
            console.print(Panel(context_chroma, title="Chroma: 'list machine types'", border_style="green", expand=False))
        else: console.print("[ChromaDB] Failed to initialize or ingest.")

        # --- Test DuckDB --- 
        console.print("\n[bold]--- Testing DuckDB Vector Store (using Gemini Embeddings if key provided) ---[/bold]")
        duckdb_test_config = {"duckdb_path": "./db/test_duckdb_example", "duckdb_file_name": "example_store_gemini.duckdb", "duckdb_table_name": "example_embeddings_gemini"}
        console.print("(DuckDB first run - building index...)")
        rag_duckdb = RAGEngine(vector_store_choice="duckdb", db_config=duckdb_test_config, llm_for_settings=None, embed_model_name=DEFAULT_EMBED_MODEL_NAME, google_api_key=gemini_key_for_test)
        ingest_success_duckdb = rag_duckdb.ingest_and_build_index(documents_path=docs_dir, force_rebuild=True)
        if ingest_success_duckdb and rag_duckdb.query_engine:
            console.print("[DuckDB] Querying for 'gcloud addresses create'...")
            context_duckdb = rag_duckdb.query_docs("gcloud addresses create")
            console.print(Panel(context_duckdb, title="DuckDB: 'gcloud addresses create'", border_style="purple", expand=False))
        else: console.print("[DuckDB] Failed to initialize or ingest.") 