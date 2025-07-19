from datetime import datetime

from pydantic import BaseModel, Field

from src.models.dto.user import User


class Message(BaseModel):
    id: int | None = Field(default=None, exclude=True)  # Поле для БД, исключается из схемы
    sender: User
    contents: str
    timestamp: datetime
    status: str


class SendMessageData(BaseModel):
    sender: User
    contents: str
