from fastapi import APIRouter

from models.chat_models import AskRequest
from services.ollama_service import generate_response
from services.chat_service import save_chat

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