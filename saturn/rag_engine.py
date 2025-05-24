import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.llms import LLM # For type hinting, can also be used to set Settings.llm = None
from llama_index.core.embeddings import BaseEmbedding # For type hinting and explicit None
from llama_index.core.schema import Document, TextNode # Add TextNode for custom splitting
from llama_index.core.node_parser.interface import NodeParser # Add for custom parser
# For local embeddings, if you don't want to rely on OpenAI for embeddings:
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# For local LLM for LlamaIndex synthesis (optional, if not just using it for retrieval)
# from llama_index.llms.ollama import Ollama 

# Using rich console for logging within the RAG engine itself
from rich.console import Console
from rich.panel import Panel # For example usage
from typing import Dict, Any, Optional, List
import re

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

# Helper function to build provider-specific database config
def build_provider_db_config(config: Dict[str, Any], provider: str = "gcp", vector_store_choice: str = "chroma") -> Dict[str, Any]:
    """
    Builds database configuration for a specific cloud provider.
    
    Args:
        config: Main configuration dictionary (from config.yaml or environment)
        provider: "gcp" or "aws"
        vector_store_choice: "chroma" or "duckdb"
    
    Returns:
        Database configuration dictionary for the provider
    """
    db_config = {}
    
    if vector_store_choice == "chroma":
        # Use shared chroma_db_path but provider-specific collection
        db_config["chroma_path"] = config.get("chroma_db_path", DEFAULT_CHROMA_PATH)
        
        if provider == "gcp":
            db_config["chroma_collection_name"] = config.get("gcp_chroma_collection_name", 
                                                           config.get("chroma_collection_name", "gcp_cli_docs"))
        elif provider == "aws":
            db_config["chroma_collection_name"] = config.get("aws_chroma_collection_name", "aws_cli_docs")
        else:
            db_config["chroma_collection_name"] = config.get("chroma_collection_name", DEFAULT_CHROMA_COLLECTION)
            
    elif vector_store_choice == "duckdb":
        # Use shared duckdb path and file but provider-specific table
        db_config["duckdb_path"] = config.get("duckdb_path", DEFAULT_DUCKDB_PATH) 
        db_config["duckdb_file_name"] = config.get("duckdb_file_name", DEFAULT_DUCKDB_DB_FILE_NAME)
        
        if provider == "gcp":
            db_config["duckdb_table_name"] = config.get("gcp_duckdb_table_name",
                                                       config.get("duckdb_table_name", "gcp_cli_embeddings"))
        elif provider == "aws":
            db_config["duckdb_table_name"] = config.get("aws_duckdb_table_name", "aws_cli_embeddings")
        else:
            db_config["duckdb_table_name"] = config.get("duckdb_table_name", DEFAULT_DUCKDB_TABLE_NAME)
    
    return db_config

def get_provider_docs_path(config: Dict[str, Any], provider: str = "gcp") -> str:
    """
    Gets the documentation path for a specific cloud provider.
    
    Args:
        config: Main configuration dictionary
        provider: "gcp" or "aws"
        
    Returns:
        Path to the provider's documentation directory
    """
    if provider == "gcp":
        return config.get("gcp_rag_docs_path", 
                         config.get("rag_docs_path", 
                                   os.path.join(os.path.dirname(__file__), '..', 'internal', 'tools', 'gcloud_online_docs_markdown')))
    elif provider == "aws":
        return config.get("aws_rag_docs_path",
                         os.path.join(os.path.dirname(__file__), '..', 'internal', 'tools', 'aws_cli_docs_markdown'))
    else:
        raise ValueError(f"Unsupported provider: {provider}")

class CLIContextAwareParser(NodeParser):
    """
    Context-aware text splitter for CLI documentation.
    
    This parser understands CLI documentation structure and splits text
    while preserving semantic context and command relationships.
    """
    
    def __init__(
        self,
        max_chunk_size: int = 2048,
        chunk_overlap: int = 200,
        preserve_code_blocks: bool = True,
        preserve_command_context: bool = True
    ):
        # Initialize with required model config
        super().__init__()
        
        # Store configuration as private attributes
        self._max_chunk_size = max_chunk_size
        self._chunk_overlap = chunk_overlap
        self._preserve_code_blocks = preserve_code_blocks
        self._preserve_command_context = preserve_command_context
        
        # Patterns for CLI documentation structure
        self._command_patterns = {
            'command_header': re.compile(r'^#{1,4}\s+(?:aws|gcloud)\s+.*$', re.MULTILINE | re.IGNORECASE),
            'subcommand_header': re.compile(r'^#{2,6}\s+(?:available\s+)?(?:commands?|subcommands?).*$', re.MULTILINE | re.IGNORECASE),
            'synopsis_header': re.compile(r'^#{2,6}\s+(?:synopsis|usage|syntax).*$', re.MULTILINE | re.IGNORECASE),
            'description_header': re.compile(r'^#{2,6}\s+(?:description|summary).*$', re.MULTILINE | re.IGNORECASE),
            'options_header': re.compile(r'^#{2,6}\s+(?:options|flags|parameters).*$', re.MULTILINE | re.IGNORECASE),
            'examples_header': re.compile(r'^#{2,6}\s+(?:examples?|sample).*$', re.MULTILINE | re.IGNORECASE),
            'code_block': re.compile(r'```[\s\S]*?```', re.MULTILINE),
            'inline_code': re.compile(r'`[^`]+`'),
            'command_line': re.compile(r'^\s*(?:aws|gcloud)\s+.*$', re.MULTILINE),
        }
    
    @property
    def max_chunk_size(self):
        return self._max_chunk_size
    
    @property
    def chunk_size(self):
        """Alias for max_chunk_size for LlamaIndex compatibility."""
        return self._max_chunk_size
    
    @chunk_size.setter
    def chunk_size(self, value):
        """Setter for chunk_size for LlamaIndex compatibility."""
        self._max_chunk_size = value
    
    @property
    def chunk_overlap(self):
        return self._chunk_overlap
        
    @property
    def preserve_code_blocks(self):
        return self._preserve_code_blocks
        
    @property
    def preserve_command_context(self):
        return self._preserve_command_context
        
    @property
    def command_patterns(self):
        return self._command_patterns
    
    def _extract_metadata_from_text(self, text: str, file_path: str = "") -> Dict[str, Any]:
        """Extract metadata from CLI documentation text."""
        metadata = {"file_path": file_path}
        
        # Extract command name from first header or file path
        command_match = self.command_patterns['command_header'].search(text)
        if command_match:
            header_text = command_match.group().strip()
            # Extract command from header like "# aws s3 cp" or "## gcloud compute instances create"
            command_parts = re.findall(r'\b(?:aws|gcloud)\s+[\w-]+(?:\s+[\w-]+)*', header_text, re.IGNORECASE)
            if command_parts:
                metadata["command"] = command_parts[0].strip()
        
        # Extract cloud provider
        if "aws" in text.lower() or "aws" in file_path.lower():
            metadata["provider"] = "aws"
        elif "gcloud" in text.lower() or "gcp" in file_path.lower():
            metadata["provider"] = "gcp"
        
        # Identify content type based on headers
        content_types = []
        if self.command_patterns['synopsis_header'].search(text):
            content_types.append("synopsis")
        if self.command_patterns['description_header'].search(text):
            content_types.append("description")
        if self.command_patterns['options_header'].search(text):
            content_types.append("options")
        if self.command_patterns['examples_header'].search(text):
            content_types.append("examples")
        if self.command_patterns['subcommand_header'].search(text):
            content_types.append("subcommands")
        
        metadata["content_types"] = content_types
        return metadata
    
    def _split_by_sections(self, text: str) -> List[Dict[str, Any]]:
        """Split text by CLI documentation sections."""
        sections = []
        
        # Split by markdown headers
        header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        matches = list(header_pattern.finditer(text))
        
        if not matches:
            # No headers found, treat entire text as one section
            return [{"content": text.strip(), "header_level": 0, "title": "Content"}]
        
        # Process sections between headers
        for i, match in enumerate(matches):
            start_pos = match.start()
            end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            
            header_level = len(match.group(1))
            title = match.group(2).strip()
            content = text[start_pos:end_pos].strip()
            
            sections.append({
                "content": content,
                "header_level": header_level,
                "title": title
            })
        
        # Handle any content before the first header
        if matches[0].start() > 0:
            pre_content = text[:matches[0].start()].strip()
            if pre_content:
                sections.insert(0, {
                    "content": pre_content,
                    "header_level": 0,
                    "title": "Introduction"
                })
        
        return sections
    
    def _should_preserve_together(self, section: Dict[str, Any]) -> bool:
        """Determine if a section should be preserved as a single chunk."""
        title = section["title"].lower()
        content = section["content"]
        
        # Convert max_chunk_size to int if it's a string
        max_size = int(self.max_chunk_size) if isinstance(self.max_chunk_size, str) else self.max_chunk_size
        
        # Preserve code blocks
        if self.preserve_code_blocks and self.command_patterns['code_block'].search(content):
            return True
        
        # Preserve command examples with their descriptions
        if "example" in title and len(content) < max_size:
            return True
        
        # Preserve synopsis/usage sections
        if any(keyword in title for keyword in ["synopsis", "usage", "syntax"]) and len(content) < max_size:
            return True
        
        # Preserve short option lists
        if "option" in title and len(content) < max_size * 0.8:
            return True
        
        return False
    
    def _smart_chunk_content(self, content: str, base_metadata: Dict[str, Any]) -> List[str]:
        """Intelligently chunk content while preserving context."""
        # Convert max_chunk_size to int if it's a string
        max_size = int(self.max_chunk_size) if isinstance(self.max_chunk_size, str) else self.max_chunk_size
        
        if len(content) <= max_size:
            return [content]
        
        chunks = []
        
        # Try to split by paragraphs first
        paragraphs = content.split('\n\n')
        current_chunk = ""
        
        for paragraph in paragraphs:
            # If adding this paragraph would exceed chunk size
            if len(current_chunk) + len(paragraph) + 2 > max_size:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = ""
                
                # If single paragraph is too large, split by sentences
                if len(paragraph) > max_size:
                    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
                    for sentence in sentences:
                        if len(current_chunk) + len(sentence) + 1 > max_size:
                            if current_chunk:
                                chunks.append(current_chunk.strip())
                                current_chunk = sentence
                            else:
                                # Even single sentence is too large, force split
                                chunks.append(sentence[:max_size].strip())
                        else:
                            current_chunk += (" " + sentence if current_chunk else sentence)
                else:
                    current_chunk = paragraph
            else:
                current_chunk += ("\n\n" + paragraph if current_chunk else paragraph)
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def get_nodes_from_documents(self, documents: List[Document], show_progress: bool = False) -> List[TextNode]:
        """Parse documents into context-aware nodes."""
        nodes = []
        
        for doc in documents:
            if show_progress:
                console.print(f"[cyan]Processing document:[/cyan] {doc.metadata.get('file_name', 'Unknown')}")
            
            text = doc.text
            file_path = doc.metadata.get('file_path', doc.metadata.get('file_name', ''))
            
            # Extract base metadata
            base_metadata = self._extract_metadata_from_text(text, file_path)
            base_metadata.update(doc.metadata)  # Preserve original metadata
            
            # Split by sections
            sections = self._split_by_sections(text)
            
            for section in sections:
                section_metadata = base_metadata.copy()
                section_metadata.update({
                    "section_title": section["title"],
                    "header_level": section["header_level"],
                    "content_types": ", ".join(base_metadata.get("content_types", []))  # Convert list to string for ChromaDB
                })
                
                # Determine if section should be preserved as-is
                if self._should_preserve_together(section):
                    # Create single node for this section
                    node = TextNode(
                        text=section["content"],
                        metadata=section_metadata
                    )
                    nodes.append(node)
                else:
                    # Split section into smaller chunks
                    chunks = self._smart_chunk_content(section["content"], section_metadata)
                    
                    for i, chunk in enumerate(chunks):
                        chunk_metadata = section_metadata.copy()
                        chunk_metadata.update({
                            "chunk_index": i,
                            "total_chunks": len(chunks),
                            "is_partial_section": len(chunks) > 1
                        })
                        
                        node = TextNode(
                            text=chunk,
                            metadata=chunk_metadata
                        )
                        nodes.append(node)
        
        if show_progress:
            console.print(f"[green]Created {len(nodes)} context-aware text nodes[/green]")
        
        return nodes
    
    def _parse_nodes(self, nodes: List[TextNode], show_progress: bool = False) -> List[TextNode]:
        """Required method for NodeParser interface. For CLI parser, this is a pass-through."""
        # The CLI parser works primarily on documents, so this is just a pass-through
        return nodes

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
                 llm_for_settings: Optional[LLM] = None,
                 # Context-aware parsing options
                 use_context_aware_parsing: bool = True,
                 max_chunk_size: int = 2048,
                 chunk_overlap: int = 200,
                 preserve_code_blocks: bool = True,
                 preserve_command_context: bool = True
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
            use_context_aware_parsing (bool): Whether to use CLI-specific context-aware text parsing.
            max_chunk_size (int): Maximum size for text chunks.
            chunk_overlap (int): Overlap between chunks for context preservation.
            preserve_code_blocks (bool): Whether to keep code blocks intact.
            preserve_command_context (bool): Whether to preserve command-related context.
        """
        self.index: Optional[VectorStoreIndex] = None
        self.query_engine = None
        self.db_config = db_config if db_config else {}
        self.vector_store_choice = vector_store_choice.lower()
        self.storage_context: Optional[StorageContext] = None
        self.vector_store: Optional[Any] = None # Will hold ChromaVectorStore or DuckDBVectorStore instance
        self._is_initialized_properly = False # Flag to check successful init
        
        # Store parsing configuration
        self.use_context_aware_parsing = use_context_aware_parsing
        self.max_chunk_size = max_chunk_size
        self.chunk_overlap = chunk_overlap
        self.preserve_code_blocks = preserve_code_blocks
        self.preserve_command_context = preserve_command_context

        console.print(f"[RAG Engine] Initializing RAGEngine.")
        console.print(f"[RAG Engine] Vector store choice: {self.vector_store_choice}")
        console.print(f"[RAG Engine] Attempting to use embedding model identifier: {embed_model_name}")
        console.print(f"[RAG Engine] Context-aware parsing: {'enabled' if use_context_aware_parsing else 'disabled'}")

        try:
            # 0. Configure LlamaIndex Global Settings
            if llm_for_settings is None:
                # console.print("[RAG Engine] Setting LlamaIndex Settings.llm to None. Observability may be affected.")
                Settings.llm = None # Primary way to avoid default OpenAI LLM for synthesis
                # Settings.global_handler = None # This line caused "Eval mode None not supported"
            elif llm_for_settings: 
                Settings.llm = llm_for_settings
                console.print(f"[RAG Engine] LlamaIndex Settings.llm configured with provided LLM: {type(llm_for_settings).__name__}")

            # Set context window and configure node parser
            Settings.context_window = DEFAULT_CONTEXT_WINDOW
            
            # Configure text splitting/parsing based on settings
            if self.use_context_aware_parsing:
                # Use custom CLI-aware parser
                Settings.node_parser = CLIContextAwareParser(
                    max_chunk_size=self.max_chunk_size,
                    chunk_overlap=self.chunk_overlap,
                    preserve_code_blocks=self.preserve_code_blocks,
                    preserve_command_context=self.preserve_command_context
                )
                console.print(f"[RAG Engine] Configured CLI context-aware parser (max_chunk_size={self.max_chunk_size})")
            else:
                # Use default sentence splitter
                Settings.node_parser = SentenceSplitter(
                    chunk_size=self.max_chunk_size,
                    chunk_overlap=self.chunk_overlap
                )
                console.print(f"[RAG Engine] Configured standard sentence splitter (chunk_size={self.max_chunk_size})")
            
            # Set chunk settings for compatibility (only if using standard sentence splitter)
            if not self.use_context_aware_parsing:
                Settings.chunk_size = self.max_chunk_size
                Settings.chunk_overlap = self.chunk_overlap
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
        Enhanced with context-aware metadata information.
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
            
            # Group nodes by command/provider for better organization
            nodes_by_command = {}
            
            for i, source_node in enumerate(response.source_nodes):
                score = source_node.get_score()
                text_content = source_node.get_text()
                metadata = source_node.node.metadata or {}
                
                # Extract enhanced metadata from context-aware parsing
                file_name = metadata.get('file_name', 'N/A')
                command = metadata.get('command', 'Unknown')
                provider = metadata.get('provider', 'Unknown')
                section_title = metadata.get('section_title', 'Content')
                content_types = metadata.get('content_types', [])
                
                display_score = f"{score:.2f}" if score is not None else "N/A"
                
                # Skip if score is too low
                if score is not None and score < min_similarity_score:
                    console.print(f"  [RAG Engine] Node {i+1} from '{file_name}' (command: {command}, section: {section_title}) skipped due to low score ({display_score} < {min_similarity_score}).")
                    continue
                
                # Group by command for better organization
                command_key = f"{provider}:{command}" if command != 'Unknown' else f"{provider}:{file_name}"
                if command_key not in nodes_by_command:
                    nodes_by_command[command_key] = []
                
                nodes_by_command[command_key].append({
                    'text': text_content,
                    'metadata': metadata,
                    'score': display_score,
                    'section_title': section_title,
                    'content_types': content_types
                })
            
            # Format results by command/provider
            if nodes_by_command:
                for command_key, nodes in nodes_by_command.items():
                    provider, command_or_file = command_key.split(':', 1)
                    
                    # Add command header
                    relevant_docs_parts.append(f"## {provider.upper()}: {command_or_file}\n")
                    
                    for node_info in nodes:
                        metadata = node_info['metadata']
                        section_title = node_info['section_title']
                        content_types = node_info['content_types']
                        score = node_info['score']
                        text_content = node_info['text']
                        
                        # Create a more informative header
                        header_parts = [f"**Section:** {section_title}"]
                        if content_types:
                            header_parts.append(f"**Type:** {', '.join(content_types)}")
                        header_parts.append(f"**Relevance:** {score}")
                        
                        header = " | ".join(header_parts)
                        
                        relevant_docs_parts.append(f"### {header}\n\n{text_content}\n\n---\n")
            else:
                console.print("[RAG Engine] No documents met the minimum similarity score.")
                # Fallback to the most relevant node if available
                if response.source_nodes:
                    top_node = response.source_nodes[0]
                    top_node_text = top_node.get_text()
                    top_node_metadata = top_node.node.metadata or {}
                    command = top_node_metadata.get('command', 'Unknown')
                    provider = top_node_metadata.get('provider', 'Unknown')
                    
                    console.print(f"[RAG Engine] Returning most relevant document as fallback (command: {command}, provider: {provider}).")
                    return f"**Potentially relevant content** (similarity score may be low):\n\n**Command:** {command} ({provider})\n\n{top_node_text}"
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
    # Load configuration (in a real app, this would come from config.py)
    example_config = {
        "gcp_rag_docs_path": os.path.join(os.path.dirname(__file__), '..', 'internal', 'tools', 'gcloud_online_docs_markdown'),
        "aws_rag_docs_path": os.path.join(os.path.dirname(__file__), '..', 'internal', 'tools', 'aws_cli_docs_markdown'),
        "vector_store": "chroma",
        "chroma_db_path": "./db/chroma_db",
        "gcp_chroma_collection_name": "gcp_cli_docs_test",
        "aws_chroma_collection_name": "aws_cli_docs_test",
        "gcp_duckdb_table_name": "gcp_cli_embeddings_test",
        "aws_duckdb_table_name": "aws_cli_embeddings_test"
    }
    
    docs_dir_gcp = get_provider_docs_path(example_config, "gcp")
    docs_dir_aws = get_provider_docs_path(example_config, "aws")
    gemini_key_for_test = os.getenv("GOOGLE_API_KEY") # For Gemini embedding test

    console.print(f"[Example Usage] RAG Engine Test Script with Provider-Specific Configurations")

    if not os.path.isdir(docs_dir_gcp):
        console.print(f"[bold yellow]Warning for GCP example usage:[/] GCP documentation directory not found at: {docs_dir_gcp}")
    if not os.path.isdir(docs_dir_aws):
        console.print(f"[bold yellow]Warning for AWS example usage:[/] AWS documentation directory not found at: {docs_dir_aws}")
        

    # --- Test In-Memory with default local HuggingFace embedding (using GCP docs for this example) ---
    if os.path.isdir(docs_dir_gcp):
        console.print("\n[bold]--- Testing In-Memory (HuggingFace Embeddings - GCP Docs) ---[/bold]")
        rag_memory_hf = RAGEngine(
            vector_store_choice="default", 
            documents_path_for_init=docs_dir_gcp, 
            build_index_on_init=True, 
            llm_for_settings=None,
            embed_model_name="local:BAAI/bge-small-en-v1.5" # Explicitly test this
        )
        if rag_memory_hf.query_engine:
            console.print("[In-Memory HF] Querying for 'create instance'...")
            context_mem_hf = rag_memory_hf.query_docs("How to create a gcloud compute instance?")
            console.print(Panel(context_mem_hf, title="In-Memory HF (GCP): 'create instance'", border_style="blue", expand=False))
        else: console.print("[In-Memory HF] Failed to initialize.")
    else:
        console.print("\n[bold yellow]Skipping In-Memory HuggingFace (GCP Docs) test as docs_dir_gcp not found.[/bold]")

    # --- Test In-Memory with Gemini Embedding (using GCP docs for this example, if API key is available) ---
    if os.path.isdir(docs_dir_gcp):
        console.print("\n[bold]--- Testing In-Memory (Gemini Embeddings - GCP Docs) ---[/bold]")
        if gemini_key_for_test:
            rag_memory_gemini = RAGEngine(
                vector_store_choice="default", 
                documents_path_for_init=docs_dir_gcp, 
                build_index_on_init=True, 
                llm_for_settings=None,
                embed_model_name=DEFAULT_EMBED_MODEL_NAME, 
                google_api_key=gemini_key_for_test
            )
            if rag_memory_gemini.query_engine:
                console.print("[In-Memory Gemini] Querying for 'create instance'...")
                context_mem_gemini = rag_memory_gemini.query_docs("How to create a gcloud compute instance?")
                console.print(Panel(context_mem_gemini, title="In-Memory Gemini (GCP): 'create instance'", border_style="magenta", expand=False))
            else: console.print("[In-Memory Gemini] Failed to initialize.")
        else:
            console.print("[Example Usage] GOOGLE_API_KEY not found in env. Skipping Gemini In-Memory (GCP) embedding test.")
    else:
        console.print("\n[bold yellow]Skipping In-Memory Gemini (GCP Docs) test as docs_dir_gcp not found.[/bold]")


    # --- Test ChromaDB (GCP Docs - using provider-specific config) --- 
    if os.path.isdir(docs_dir_gcp):
        console.print("\n[bold]--- Testing ChromaDB Vector Store (GCP Docs - Provider-Specific Config) ---[/bold]")
        chroma_gcp_config = build_provider_db_config(example_config, provider="gcp", vector_store_choice="chroma")
        console.print(f"GCP ChromaDB Config: {chroma_gcp_config}")
        console.print("(ChromaDB GCP first run - building index...)")
        rag_chroma_gcp = RAGEngine(
            vector_store_choice="chroma", 
            db_config=chroma_gcp_config, 
            llm_for_settings=None, 
            embed_model_name=DEFAULT_EMBED_MODEL_NAME, 
            google_api_key=gemini_key_for_test
        )
        ingest_success_chroma_gcp = rag_chroma_gcp.ingest_and_build_index(documents_path=docs_dir_gcp, force_rebuild=True)
        if ingest_success_chroma_gcp and rag_chroma_gcp.query_engine:
            console.print("[ChromaDB GCP] Querying for 'list machine types'...")
            context_chroma_gcp = rag_chroma_gcp.query_docs("list available gcloud machine types in a zone")
            console.print(Panel(context_chroma_gcp, title="Chroma (GCP): 'list machine types'", border_style="green", expand=False))
        else: console.print("[ChromaDB GCP] Failed to initialize or ingest.")
    else:
        console.print("\n[bold yellow]Skipping ChromaDB (GCP Docs) test as docs_dir_gcp not found.[/bold]")

    # --- Test ChromaDB (AWS Docs - using provider-specific config) --- 
    if os.path.isdir(docs_dir_aws):
        console.print("\n[bold]--- Testing ChromaDB Vector Store (AWS Docs - Provider-Specific Config) ---[/bold]")
        chroma_aws_config = build_provider_db_config(example_config, provider="aws", vector_store_choice="chroma")
        console.print(f"AWS ChromaDB Config: {chroma_aws_config}")
        console.print("(ChromaDB AWS first run - building index...)")
        rag_chroma_aws = RAGEngine(
            vector_store_choice="chroma", 
            db_config=chroma_aws_config, 
            llm_for_settings=None, 
            embed_model_name=DEFAULT_EMBED_MODEL_NAME, 
            google_api_key=gemini_key_for_test
        )
        ingest_success_chroma_aws = rag_chroma_aws.ingest_and_build_index(documents_path=docs_dir_aws, force_rebuild=True)
        if ingest_success_chroma_aws and rag_chroma_aws.query_engine:
            console.print("[ChromaDB AWS] Querying for 's3 list buckets'...")
            context_chroma_aws = rag_chroma_aws.query_docs("how to list s3 buckets using aws cli")
            console.print(Panel(context_chroma_aws, title="Chroma (AWS): 's3 list buckets'", border_style="cyan", expand=False))
        else: console.print("[ChromaDB AWS] Failed to initialize or ingest.")
    else:
        console.print("\n[bold yellow]Skipping ChromaDB (AWS Docs) test as docs_dir_aws not found.[/bold]")


    # --- Test DuckDB (GCP Docs - using provider-specific config) --- 
    if os.path.isdir(docs_dir_gcp):
        console.print("\n[bold]--- Testing DuckDB Vector Store (GCP Docs - Provider-Specific Config) ---[/bold]")
        duckdb_gcp_config = build_provider_db_config(example_config, provider="gcp", vector_store_choice="duckdb")
        console.print(f"GCP DuckDB Config: {duckdb_gcp_config}")
        console.print("(DuckDB GCP first run - building index...)")
        rag_duckdb_gcp = RAGEngine(
            vector_store_choice="duckdb", 
            db_config=duckdb_gcp_config, 
            llm_for_settings=None, 
            embed_model_name=DEFAULT_EMBED_MODEL_NAME, 
            google_api_key=gemini_key_for_test
        )
        ingest_success_duckdb_gcp = rag_duckdb_gcp.ingest_and_build_index(documents_path=docs_dir_gcp, force_rebuild=True)
        if ingest_success_duckdb_gcp and rag_duckdb_gcp.query_engine:
            console.print("[DuckDB GCP] Querying for 'gcloud addresses create'...")
            context_duckdb_gcp = rag_duckdb_gcp.query_docs("gcloud addresses create")
            console.print(Panel(context_duckdb_gcp, title="DuckDB (GCP): 'gcloud addresses create'", border_style="purple", expand=False))
        else: console.print("[DuckDB GCP] Failed to initialize or ingest.")
    else:
        console.print("\n[bold yellow]Skipping DuckDB (GCP Docs) test as docs_dir_gcp not found.[/bold]")
        
    # --- Test DuckDB (AWS Docs - using provider-specific config) --- 
    if os.path.isdir(docs_dir_aws):
        console.print("\n[bold]--- Testing DuckDB Vector Store (AWS Docs - Provider-Specific Config) ---[/bold]")
        duckdb_aws_config = build_provider_db_config(example_config, provider="aws", vector_store_choice="duckdb")
        console.print(f"AWS DuckDB Config: {duckdb_aws_config}")
        console.print("(DuckDB AWS first run - building index...)")
        rag_duckdb_aws = RAGEngine(
            vector_store_choice="duckdb", 
            db_config=duckdb_aws_config, 
            llm_for_settings=None, 
            embed_model_name=DEFAULT_EMBED_MODEL_NAME, 
            google_api_key=gemini_key_for_test
        )
        ingest_success_duckdb_aws = rag_duckdb_aws.ingest_and_build_index(documents_path=docs_dir_aws, force_rebuild=True)
        if ingest_success_duckdb_aws and rag_duckdb_aws.query_engine:
            console.print("[DuckDB AWS] Querying for 'ec2 describe instances'...")
            context_duckdb_aws = rag_duckdb_aws.query_docs("how to describe ec2 instances using aws cli")
            console.print(Panel(context_duckdb_aws, title="DuckDB (AWS): 'ec2 describe instances'", border_style="yellow", expand=False))
        else: console.print("[DuckDB AWS] Failed to initialize or ingest.")
    else:
        console.print("\n[bold yellow]Skipping DuckDB (AWS Docs) test as docs_dir_aws not found.[/bold]") 