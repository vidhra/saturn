import os
import glob
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Paths
DOCS_DIR = os.path.join(os.path.dirname(__file__), 'gcloud_online_docs_markdown')
CHROMA_DB_DIR = os.path.join(os.path.dirname(__file__), 'chroma_db')

# Initialize ChromaDB and embedding model
chroma_client = chromadb.Client(Settings(persist_directory=CHROMA_DB_DIR))
collection = chroma_client.get_or_create_collection("gcloud_docs")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_markdown(text, chunk_size=500):
    paragraphs = text.split('\n\n')
    chunks = []
    current = ""
    for para in paragraphs:
        if len(current) + len(para) < chunk_size:
            current += para + "\n\n"
        else:
            if current.strip():
                chunks.append(current.strip())
            current = para + "\n\n"
    if current.strip():
        chunks.append(current.strip())
    return chunks

def ingest_docs():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True)
    total_chunks = 0
    for md_file in md_files:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        chunks = chunk_markdown(content)
        if not chunks:
            continue
        embeddings = embedder.encode(chunks)
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            rel_path = os.path.relpath(md_file, DOCS_DIR)
            doc_chunk_id = f"{rel_path}::chunk_{i}"
            collection.add(
                ids=[doc_chunk_id],
                documents=[chunk],
                embeddings=[embedding.tolist()],
                metadatas=[{"source_file": rel_path, "chunk_id": i, "doc_chunk_id": doc_chunk_id}]
            )
            total_chunks += 1
        print(f"Ingested {len(chunks)} chunks from {md_file}")
    chroma_client.persist()
    print(f"Ingestion complete. Total chunks: {total_chunks}")

if __name__ == "__main__":
    ingest_docs() 