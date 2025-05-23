import os
import glob
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Paths
DOCS_DIR = os.path.join(os.path.dirname(__file__), 'aws_cli_docs_markdown') # Changed to AWS docs
CHROMA_DB_DIR = os.path.join(os.path.dirname(__file__), 'chroma_db_aws')    # New DB dir for AWS
if not os.path.exists(CHROMA_DB_DIR):
    os.makedirs(CHROMA_DB_DIR)

# Initialize ChromaDB and embedding model
# Ensuring to use the new directory for AWS
chroma_client = chromadb.Client(Settings(persist_directory=CHROMA_DB_DIR, is_persistent=True))
collection_name = "aws_cli_docs" # New collection name for AWS
collection = chroma_client.get_or_create_collection(collection_name)
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_markdown(text, chunk_size=500):
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk_text = ""
    for para in paragraphs:
        # Check if adding the new paragraph (plus a separator) exceeds chunk_size
        if len(current_chunk_text) + len(para) + len("\n\n") > chunk_size and current_chunk_text:
            chunks.append(current_chunk_text.strip())
            current_chunk_text = para + "\n\n" # Start new chunk with current paragraph
        else:
            current_chunk_text += para + "\n\n"
            
    # Add the last accumulated chunk if it's not empty
    if current_chunk_text.strip():
        chunks.append(current_chunk_text.strip())
    return chunks

def ingest_docs():
    if not os.path.exists(DOCS_DIR):
        print(f"Error: AWS CLI Markdown directory not found at {DOCS_DIR}")
        print("Please ensure you have run the 'doc_ext_aws.py' script first.")
        return

    md_files = glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True)
    if not md_files:
        print(f"No Markdown files found in {DOCS_DIR}. Nothing to ingest.")
        return
        
    total_chunks_ingested = 0
    for md_file_path in md_files:
        try:
            with open(md_file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file {md_file_path}: {e}")
            continue # Skip this file

        chunks = chunk_markdown(content)
        if not chunks:
            print(f"No chunks generated for {md_file_path}. Skipping.")
            continue
            
        try:
            embeddings = embedder.encode(chunks)
        except Exception as e:
            print(f"Error encoding chunks from {md_file_path}: {e}")
            continue # Skip this file

        ids_to_add = []
        documents_to_add = []
        embeddings_to_add = []
        metadatas_to_add = []

        for i, (chunk_text, embedding_vector) in enumerate(zip(chunks, embeddings)):
            relative_path = os.path.relpath(md_file_path, DOCS_DIR)
            doc_chunk_id = f"{relative_path}::chunk_{i}"
            
            ids_to_add.append(doc_chunk_id)
            documents_to_add.append(chunk_text)
            embeddings_to_add.append(embedding_vector.tolist())
            metadatas_to_add.append({"source_file": relative_path, "chunk_id": i, "doc_chunk_id": doc_chunk_id})

        if ids_to_add:
            try:
                collection.add(
                    ids=ids_to_add,
                    documents=documents_to_add,
                    embeddings=embeddings_to_add,
                    metadatas=metadatas_to_add
                )
                print(f"Ingested {len(ids_to_add)} chunks from {md_file_path}")
                total_chunks_ingested += len(ids_to_add)
            except Exception as e:
                print(f"Error adding chunks from {md_file_path} to ChromaDB: {e}")
                # Consider if you want to skip the whole file or try chunks individually
    
    # Persist changes to disk. This might not be necessary if auto-persisting is enabled or if Client handles it.
    # For explicit control, especially with `Settings(is_persistent=True)`, it's good practice.
    # However, ChromaDB's newer versions with `is_persistent=True` in Settings should handle persistence.
    # Explicitly calling persist can be a safeguard or for specific versions/behaviors.
    # chroma_client.persist() # This line might be redundant depending on Chroma client version and settings
    
    print(f"Ingestion complete. Total chunks ingested: {total_chunks_ingested}")
    print(f"AWS CLI Docs ChromaDB collection '{collection_name}' stored in: {CHROMA_DB_DIR}")

if __name__ == "__main__":
    ingest_docs() 