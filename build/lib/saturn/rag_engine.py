import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.llms import LLM 
from llama_index.core.embeddings import BaseEmbedding 
from llama_index.core.schema import Document, TextNode 
from llama_index.core.node_parser.interface import NodeParser 
from rich.console import Console
from rich.panel import Panel 
from typing import Dict, Any, Optional, List
import re

try:
    import torch
except ImportError:
    torch = None

console = Console()

DEFAULT_EMBED_MODEL_NAME = "models/text-embedding-004" 
DEFAULT_CHROMA_PATH = "./db/chroma_db"
DEFAULT_CHROMA_COLLECTION = "gclouddocs"
DEFAULT_DUCKDB_PATH = "./db/duckdb_store"
DEFAULT_DUCKDB_DB_FILE_NAME = "vector_store.duckdb"
DEFAULT_DUCKDB_TABLE_NAME = "gclouddocs_embeddings"
DEFAULT_CONTEXT_WINDOW = 65536 
DEFAULT_CHUNK_SIZE = 2048     

DEFAULT_CHUNK_OVERLAP_RATIO = 0.25 

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
        
        db_config["chroma_path"] = config.get("chroma_db_path", DEFAULT_CHROMA_PATH)
        
        if provider == "gcp":
            db_config["chroma_collection_name"] = config.get("gcp_chroma_collection_name", 
                                                           config.get("chroma_collection_name", "gcp_cli_docs"))
        elif provider == "aws":
            db_config["chroma_collection_name"] = config.get("aws_chroma_collection_name", "aws_cli_docs")
        else:
            db_config["chroma_collection_name"] = config.get("chroma_collection_name", DEFAULT_CHROMA_COLLECTION)
            
    elif vector_store_choice == "duckdb":
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
        
        super().__init__()
        
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
        

        command_match = self.command_patterns['command_header'].search(text)
        if command_match:
            header_text = command_match.group().strip()
            command_parts = re.findall(r'\b(?:aws|gcloud)\s+[\w-]+(?:\s+[\w-]+)*', header_text, re.IGNORECASE)
            if command_parts:
                metadata["command"] = command_parts[0].strip()
        
        if "aws" in text.lower() or "aws" in file_path.lower():
            metadata["provider"] = "aws"
        elif "gcloud" in text.lower() or "gcp" in file_path.lower():
            metadata["provider"] = "gcp"
        
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
        
        header_pattern = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
        matches = list(header_pattern.finditer(text))
        
        if not matches:
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
        
        max_size = int(self.max_chunk_size) if isinstance(self.max_chunk_size, str) else self.max_chunk_size
        
        
        if self.preserve_code_blocks and self.command_patterns['code_block'].search(content):
            return True
        
        if "example" in title and len(content) < max_size:
            return True
        
        
        if any(keyword in title for keyword in ["synopsis", "usage", "syntax"]) and len(content) < max_size:
            return True
        
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
                 google_api_key: Optional[str] = None, 
                 documents_path_for_init: Optional[str] = None, 
                 build_index_on_init: bool = False,
                 llm_for_settings: Optional[LLM] = None,
                 use_context_aware_parsing: bool = True,
                 max_chunk_size: int = 2048,
                 chunk_overlap: int = 200,
                 preserve_code_blocks: bool = True,
                 preserve_command_context: bool = True,
                 # GPU and parallel processing parameters
                 device: Optional[str] = None,
                 parallel_process: bool = False,
                 target_devices: Optional[List[str]] = None,
                 embed_batch_size: int = 64,
                 show_progress_bar: bool = False,
                 torch_dtype: Optional[str] = None
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
            device (Optional[str]): Device to run embeddings on ("cuda", "cuda:0", "cpu", "mps", "auto"). If None, auto-detects GPU.
            parallel_process (bool): Enable multi-process parallel embedding processing. Great for large datasets.
            target_devices (Optional[List[str]]): List of specific devices for parallel processing, e.g. ["cuda:0", "cuda:1"].
            embed_batch_size (int): Batch size for embedding processing. Larger values can be faster on GPU.
            show_progress_bar (bool): Show progress bar during embedding operations.
            torch_dtype (Optional[str]): PyTorch dtype for model weights ("float16", "bfloat16", "float32"). float16 recommended for GPU.
        """
        self.index: Optional[VectorStoreIndex] = None
        self.query_engine = None
        self.db_config = db_config if db_config else {}
        self.vector_store_choice = vector_store_choice.lower()
        self.storage_context: Optional[StorageContext] = None
        self.vector_store: Optional[Any] = None 
        self._is_initialized_properly = False 
        self.use_context_aware_parsing = use_context_aware_parsing
        self.max_chunk_size = max_chunk_size
        self.chunk_overlap = chunk_overlap
        self.preserve_code_blocks = preserve_code_blocks
        self.preserve_command_context = preserve_command_context
        
        # GPU and performance parameters
        self.device = device
        self.parallel_process = parallel_process
        self.target_devices = target_devices
        self.embed_batch_size = embed_batch_size
        self.show_progress_bar = show_progress_bar
        self.torch_dtype = torch_dtype

        console.print(f"[RAG Engine] Initializing RAGEngine.")
        console.print(f"[RAG Engine] Vector store choice: {self.vector_store_choice}")
        console.print(f"[RAG Engine] Attempting to use embedding model identifier: {embed_model_name}")
        console.print(f"[RAG Engine] Context-aware parsing: {'enabled' if use_context_aware_parsing else 'disabled'}")
        console.print(f"[RAG Engine] Device: {device if device else 'auto-detect'}")
        console.print(f"[RAG Engine] Parallel processing: {'enabled' if parallel_process else 'disabled'}")
        console.print(f"[RAG Engine] Batch size: {embed_batch_size}")

        try:
            
            if llm_for_settings is None:
               
                Settings.llm = None
               
            elif llm_for_settings: 
                Settings.llm = llm_for_settings
                console.print(f"[RAG Engine] LlamaIndex Settings.llm configured with provided LLM: {type(llm_for_settings).__name__}")
            Settings.context_window = DEFAULT_CONTEXT_WINDOW
            
            if self.use_context_aware_parsing:
                Settings.node_parser = CLIContextAwareParser(
                    max_chunk_size=self.max_chunk_size,
                    chunk_overlap=self.chunk_overlap,
                    preserve_code_blocks=self.preserve_code_blocks,
                    preserve_command_context=self.preserve_command_context
                )
                console.print(f"[RAG Engine] Configured CLI context-aware parser (max_chunk_size={self.max_chunk_size})")
            else:
                
                Settings.node_parser = SentenceSplitter(
                    chunk_size=self.max_chunk_size,
                    chunk_overlap=self.chunk_overlap
                )
                console.print(f"[RAG Engine] Configured standard sentence splitter (chunk_size={self.max_chunk_size})")
            
            if not self.use_context_aware_parsing:
                Settings.chunk_size = self.max_chunk_size
                Settings.chunk_overlap = self.chunk_overlap
            console.print(f"[RAG Engine] Set LlamaIndex Settings: context_window={Settings.context_window}, chunk_size={Settings.chunk_size}, chunk_overlap={Settings.chunk_overlap}")

            embedding_model_configured = False
            effective_google_api_key = google_api_key or os.getenv("GOOGLE_API_KEY")
            
                
            env_key = os.getenv("GOOGLE_API_KEY")
            if env_key:
                print(f"  - From os.environ: {env_key[:2]}...{env_key[-2:]}")
            else:
                print("  - From os.environ: None")
                
            if effective_google_api_key:
                print(f"  - Effective key chosen: {effective_google_api_key[:2]}...{effective_google_api_key[-2:]}")
            else:
                print("  - Effective key chosen: None")

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
                    print(f"  - embed_batch_size: {self.embed_batch_size}")

                    Settings.embed_model = GoogleGenAIEmbedding(
                        model_name=final_google_model_name,
                        api_key=effective_google_api_key,
                        embed_batch_size=self.embed_batch_size
                    )
                    console.print(f"[RAG Engine] Configured GoogleGenAIEmbedding model: {final_google_model_name} with batch size {self.embed_batch_size}")
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
                    
                    hf_kwargs = {
                        "model_name": hf_model_name,
                        "embed_batch_size": self.embed_batch_size,
                        "show_progress_bar": self.show_progress_bar
                    }
                    
                    if self.device == "auto" or self.device is None:
                        try:
                            if torch and torch.cuda.is_available():
                                hf_kwargs["device"] = "cuda"
                                console.print(f"[RAG Engine] Auto-detected CUDA device for embeddings")
                            elif torch and hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
                                hf_kwargs["device"] = "mps"
                                console.print(f"[RAG Engine] Auto-detected MPS device for embeddings")
                            else:
                                hf_kwargs["device"] = "cpu"
                                console.print(f"[RAG Engine] Auto-detected CPU device for embeddings")
                        except Exception as e:
                            hf_kwargs["device"] = "cpu"
                            console.print(f"[RAG Engine] Exception during device detection: {e}, using CPU for embeddings")
                    else:
                        hf_kwargs["device"] = self.device
                        console.print(f"[RAG Engine] Using specified device: {self.device}")

                    if self.parallel_process:
                        hf_kwargs["parallel_process"] = True
                        if self.target_devices:
                            hf_kwargs["target_devices"] = self.target_devices
                            console.print(f"[RAG Engine] Enabled parallel processing on devices: {self.target_devices}")
                        else:
                            console.print(f"[RAG Engine] Enabled parallel processing with auto device selection")

                    if self.torch_dtype:
                        model_kwargs = {}
                        if self.torch_dtype == "float16":
                            model_kwargs["torch_dtype"] = "float16"
                        elif self.torch_dtype == "bfloat16":
                            model_kwargs["torch_dtype"] = "bfloat16"
                        elif self.torch_dtype == "float32":
                            model_kwargs["torch_dtype"] = "float32"
                        
                        if model_kwargs:
                            hf_kwargs["model_kwargs"] = model_kwargs
                            console.print(f"[RAG Engine] Using torch dtype: {self.torch_dtype}")
                    
                    Settings.embed_model = HuggingFaceEmbedding(**hf_kwargs)

                    if hf_kwargs.get("device", "").startswith("cuda"):
                        try:
                            if torch and torch.cuda.is_available():
                                device_id = 0 if hf_kwargs["device"] == "cuda" else int(hf_kwargs["device"].split(":")[1])
                                memory_allocated = torch.cuda.memory_allocated(device_id) / 1024**3
                                memory_reserved = torch.cuda.memory_reserved(device_id) / 1024**3
                                console.print(f"[RAG Engine] GPU Memory - Allocated: {memory_allocated:.2f}GB, Reserved: {memory_reserved:.2f}GB")
                        except Exception as e_mem:
                            console.print(f"[RAG Engine] Could not check GPU memory: {e_mem}")
                    
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
                return

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

            if build_index_on_init and documents_path_for_init:
                self.ingest_and_build_index(documents_path_for_init, force_rebuild=False) 
            elif self.vector_store_choice == "default" and documents_path_for_init:
                 console.print("[RAG Engine] Building in-memory index from provided documents_path_for_init.")
                 self.ingest_and_build_index(documents_path_for_init, force_rebuild=False) 
            
            if self.index:
                current_llm_setting = Settings.llm
                self.query_engine = self.index.as_query_engine(similarity_top_k=5, llm=current_llm_setting)
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
                        db = self.vector_store.client 
                        chroma_collection = db.get_or_create_collection(collection_name)
                        self.vector_store = type(self.vector_store)(chroma_collection=chroma_collection)
                        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
                        console.print(f"[RAG Engine] ChromaDB collection '{collection_name}' re-created.")
                        self.index = None 
                    except Exception as e_delete_chroma:
                        console.print(f"[RAG Engine] [bold red]Error deleting/re-creating Chroma collection '{collection_name}':[/] {e_delete_chroma}")
                        
            elif self.vector_store_choice == "duckdb" and force_rebuild:
                if self.vector_store and hasattr(self.vector_store, '_conn'):
                    table_name = self.db_config.get("duckdb_table_name", DEFAULT_DUCKDB_TABLE_NAME)
                    console.print(f"[RAG Engine] DuckDB force_rebuild: Dropping table '{table_name}'...")
                    try:
                        self.vector_store._conn.execute(f"DROP TABLE IF EXISTS \"{table_name}\"")
                        console.print(f"[RAG Engine] DuckDB table '{table_name}' dropped.")
                        self.index = None 
                    except Exception as e_drop_duckdb:
                        console.print(f"[RAG Engine] [bold red]Error dropping DuckDB table '{table_name}':[/] {e_drop_duckdb}")
             
            console.print(f"[RAG Engine] Building/updating index with {len(documents)} documents for '{self.vector_store_choice}' store...")
            if self.vector_store_choice == "default" or not self.storage_context:
                self.index = VectorStoreIndex.from_documents(documents, show_progress=True)
                console.print("[RAG Engine] Built new in-memory index.")
            else:
                
                self.index = VectorStoreIndex.from_documents(
                    documents, 
                    storage_context=self.storage_context, 
                    show_progress=True
                )
                console.print(f"[RAG Engine] Index built/updated for {self.vector_store_choice}.")

            if self.index:
                
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
            
            nodes_by_command = {}
            
            for i, source_node in enumerate(response.source_nodes):
                score = source_node.get_score()
                text_content = source_node.get_text()
                metadata = source_node.node.metadata or {}
                
                file_name = metadata.get('file_name', 'N/A')
                command = metadata.get('command', 'Unknown')
                provider = metadata.get('provider', 'Unknown')
                section_title = metadata.get('section_title', 'Content')
                content_types = metadata.get('content_types', [])
                
                display_score = f"{score:.2f}" if score is not None else "N/A"
                
                if score is not None and score < min_similarity_score:
                    console.print(f"  [RAG Engine] Node {i+1} from '{file_name}' (command: {command}, section: {section_title}) skipped due to low score ({display_score} < {min_similarity_score}).")
                    continue
                
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
            
            if nodes_by_command:
                for command_key, nodes in nodes_by_command.items():
                    provider, command_or_file = command_key.split(':', 1)
                    
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