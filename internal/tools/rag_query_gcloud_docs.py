import os
import sys
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# Paths
CHROMA_DB_DIR = os.path.join(os.path.dirname(__file__), 'chroma_db')

# Initialize ChromaDB and embedding model
chroma_client = chromadb.Client(Settings(persist_directory=CHROMA_DB_DIR))
collection = chroma_client.get_or_create_collection("gcloud_docs")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def query_gcloud_docs(query, top_k=5):
    query_embedding = embedder.encode([query])[0]
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )
    docs = results.get('documents', [[]])[0]
    metadatas = results.get('metadatas', [[]])[0]
    ids = results.get('ids', [[]])[0]
    print(f"\nTop {top_k} results for query: '{query}'\n" + "-"*60)
    for i, (doc, meta, doc_id) in enumerate(zip(docs, metadatas, ids)):
        print(f"Result {i+1}:")
        print(f"doc_chunk_id: {meta.get('doc_chunk_id')}")
        print(f"source_file: {meta.get('source_file')}")
        print(f"Chunk:\n{doc}\n")
        print("-"*60)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rag_query_gcloud_docs.py <your query>")
        sys.exit(1)
    user_query = " ".join(sys.argv[1:])
    query_gcloud_docs(user_query) 