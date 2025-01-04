import faiss
import pickle
from sentence_transformers import SentenceTransformer
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_model(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    """
    Loads the SentenceTransformer model.

    Args:
        model_name (str): The name of the SentenceTransformer model to load.

    Returns:
        SentenceTransformer: The loaded model.
    """
    logger.info(f"Loading SentenceTransformer model: {model_name}")
    model = SentenceTransformer(model_name)
    logger.info("Model loaded successfully.")
    return model


def get_faiss_index(index_path: str = "hrpolicy.index"):
    """
    Loads the FAISS index from the specified path.

    Args:
        index_path (str): Path to the FAISS index file.

    Returns:
        faiss.Index: The loaded FAISS index.
    """
    full_index_path = os.path.join(os.path.dirname(__file__), index_path)
    logger.info(f"Loading FAISS index from: {full_index_path}")

    if not os.path.exists(full_index_path):
        raise FileNotFoundError(f"FAISS index file not found: {full_index_path}")

    index = faiss.read_index(full_index_path)
    logger.info("FAISS index loaded successfully.")
    return index


def get_chunk_texts(chunks_path: str = "chunk_texts.pkl"):
    """
    Loads the chunked texts from a pickle file.

    Args:
        chunks_path (str): Path to the pickle file containing chunked texts.

    Returns:
        list: A list of chunked text strings.
    """
    full_chunks_path = os.path.join(os.path.dirname(__file__), chunks_path)
    logger.info(f"Loading chunked texts from: {full_chunks_path}")

    if not os.path.exists(full_chunks_path):
        raise FileNotFoundError(f"Chunked texts file not found: {full_chunks_path}")

    with open(full_chunks_path, "rb") as f:
        chunk_texts = pickle.load(f)

    logger.info("Chunked texts loaded successfully.")
    return chunk_texts
