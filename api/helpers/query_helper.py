# api/helpers/query_helper.py

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def process_query(query: str, model: SentenceTransformer, index: faiss.Index, chunk_texts: list, top_k: int = 3):
    """
    Processes the user query by embedding it, searching the FAISS index,
    and retrieving the top-k relevant chunks.

    Args:
        query (str): The user's query.
        model (SentenceTransformer): The loaded SentenceTransformer model.
        index (faiss.Index): The loaded FAISS index.
        chunk_texts (list): A list of chunked text strings.
        top_k (int): Number of top similar chunks to retrieve.

    Returns:
        list: A list of dictionaries containing 'score' and 'chunk'.
    """
    logger.info(f"Processing query: {query}")

    # Embed the user query
    query_embedding = model.encode(query, convert_to_numpy=True).astype("float32")
    # Normalize for cosine similarity
    faiss.normalize_L2(query_embedding.reshape(1, -1))

    # Search top-k results
    distances, ids = index.search(query_embedding.reshape(1, -1), top_k)
    logger.info(f"FAISS search completed. Retrieved IDs: {ids[0]}, Distances: {distances[0]}")

    # Collect the best matches
    matches = []
    for dist, idx in zip(distances[0], ids[0]):
        matches.append({
            "score": float(dist),
            "chunk": chunk_texts[idx]
        })

    logger.info(f"Retrieved {len(matches)} relevant chunk(s).")
    return matches
