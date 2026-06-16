from fastapi import APIRouter

from models.chat_models import AskRequest
from services.ollama_service import generate_response
from services.chat_service import save_chat
from services.chat_service import get_chat_history
from services.chat_service import clear_chat_history

router = APIRouter()

@router.post("/ask")
def ask_question(request: AskRequest):

    answer = generate_response(
        request.question
    )

    save_chat(
        request.question,
        answer
    )

    return {
        "question": request.question,
        "answer": answer
    }

@router.get("/history")
def get_history():

    chats = get_chat_history()

    return {
        "history": chats
    }

@router.delete("/history")
def delete_history():

    clear_chat_history()

    return {
        "message": "History cleared successfully"
    }
