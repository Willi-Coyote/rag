from uuid import uuid4, UUID

from fastapi import APIRouter

from chat.chat_api_model import Chat

chat_router = APIRouter()


@chat_router.post("/v1/chat", response_model=Chat)
def create_chat():
    return Chat(chat_id=uuid4())


@chat_router.post("/v1/chat/{id}")
def get_chat(id: UUID, question: str, ):
    pass
