# api/chat_bot_apis/teams_chat_bot.py

from fastapi import APIRouter, Request, HTTPException
from config.database import  get_model, get_chunk_texts, get_faiss_index
from api.helpers.query_helper import process_query  # Query processing logic

TEAMS_CHAT_BOT = APIRouter()

# Load resources at app startup
model = get_model()  # SentenceTransformer model
index = get_faiss_index()  # FAISS index
chunk_texts = get_chunk_texts()  # Chunked texts from PDF


@TEAMS_CHAT_BOT.post("/chat_bot")
async def chat_bot_api(request: Request):
    """
    Handles the chatbot API request and processes the query.
    """
    data = await request.json()
    query = data.get("query", "").strip()

    if not query:
        raise HTTPException(status_code=400, detail="No query provided.")

    try:
        # Use the helper to process the query
        results = process_query(query, model, index, chunk_texts)
        return {
            "query": query,
            "results": results
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
