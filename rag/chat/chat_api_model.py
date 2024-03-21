from uuid import UUID

from pydantic import BaseModel


class Chat(BaseModel):
    chat_id: UUID
