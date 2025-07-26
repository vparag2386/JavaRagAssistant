import json
import os
from typing import List, Dict

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings

INDEX_FILE = "code_index.json"


def index_codebase(codebase_path: str = "codebase") -> List[Dict]:
    """Index all .java files under codebase_path.

    Returns a list of dictionaries with text chunks, embeddings and metadata.
    """
    docs = []
    for root, _, files in os.walk(codebase_path):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        docs.append({"path": file_path, "content": f.read()})
                except FileNotFoundError:
                    continue

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = []
    metadata = []
    for doc in docs:
        chunks = splitter.split_text(doc["content"])
        for chunk in chunks:
            texts.append(chunk)
            metadata.append({"path": doc["path"]})

    embeddings_model = OllamaEmbeddings(model="mistral")
    embeddings = embeddings_model.embed_documents(texts)

    index = [
        {"text": text, "embedding": emb, "metadata": meta}
        for text, emb, meta in zip(texts, embeddings, metadata)
    ]

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    return index


def load_index() -> List[Dict]:
    """Load index from disk if available."""
    if not os.path.exists(INDEX_FILE):
        return []
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# Placeholder functions for future pgvector support

def save_to_pgvector(index: List[Dict]):
    """Save embeddings into pgvector (not implemented)."""
    pass


def load_from_pgvector() -> List[Dict]:
    """Load embeddings from pgvector (not implemented)."""
    return []
