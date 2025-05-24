from ragflow import RagFlow, RagFlowConfig
import glob
import os

INDEX_PATH = os.path.join(os.path.dirname(__file__), 'ragflow_index')
DOCS_DIR = os.path.join(os.path.dirname(__file__), 'gcloud_online_docs_markdown')

config = RagFlowConfig(
    index_path=INDEX_PATH,
    embedding_model="all-MiniLM-L6-v2",
)
ragflow = RagFlow(config)

md_files = glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True)
for md_file in md_files:
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
    ragflow.add_document(content, metadata={"source_file": md_file})

ragflow.build_index()
print("RAGFlow ingestion complete.") 