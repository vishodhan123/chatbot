import pdfplumber
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import pickle

pdf_path = "hrpolicy.pdf"
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def extract_pdf_text(path: str):
    texts = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            txt = page.extract_text()
            if txt:
                texts.append(txt)
    return "\n".join(texts)


def chunk_text(text: str, size=500):
    words = text.split()
    chunks = []
    current_chunk = []
    for w in words:
        current_chunk.append(w)
        if len(current_chunk) >= size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks


def main():
    doc_text = extract_pdf_text(pdf_path)
    chunks = chunk_text(doc_text)

    # Embed each chunk
    chunk_texts = []
    embeddings = []
    for c in chunks:
        emb = model.encode(c, convert_to_numpy=True)
        embeddings.append(emb)
        chunk_texts.append(c)

    embeddings = np.array(embeddings).astype("float32")
    dim = embeddings.shape[1]

    # Normalize for cosine similarity (inner product)
    faiss.normalize_L2(embeddings)
    index = faiss.IndexFlatIP(dim)

    # Add vectors to the index
    index.add(embeddings)

    # Write the index to disk
    faiss.write_index(index, "hrpolicy.index")

    # Save the chunk texts for reference
    with open("chunk_texts.pkl", "wb") as f:
        pickle.dump(chunk_texts, f)

    print("Index built and saved successfully.")


if __name__ == "__main__":
    main()
