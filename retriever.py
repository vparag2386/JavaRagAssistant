from typing import List, Dict

import numpy as np
from langchain_community.embeddings import OllamaEmbeddings

from indexer import load_index


# Simple cosine similarity

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def retrieve_relevant_chunks(query: str, index: List[Dict], top_k: int = 5) -> List[Dict]:
    """Return top_k most relevant chunks from the index."""
    if not index:
        return []
    embeddings_model = OllamaEmbeddings(model="mistral")
    query_emb = embeddings_model.embed_query(query)

    scores = []
    for item in index:
        score = cosine_similarity(np.array(query_emb), np.array(item["embedding"]))
        scores.append((score, item))

    scores.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in scores[:top_k]]


# Placeholder function for pgvector support

def retrieve_from_pgvector(query: str, top_k: int = 5) -> List[Dict]:
    """Retrieve from pgvector (not implemented)."""
    return []
