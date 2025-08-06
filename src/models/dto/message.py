from datetime import datetime

from pydantic import BaseModel

from src.models.dto.user import UserDTO


class MessageDTO(BaseModel):
    id: int
    sender: UserDTO
    contents: str
    timestamp: datetime
    is_read: bool = False


class SendMessageData(BaseModel):
    contents: str
