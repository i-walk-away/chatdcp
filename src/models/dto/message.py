from datetime import datetime

from pydantic import BaseModel


class MessageDTO(BaseModel):
    id: int
    sender_id: int
    contents: str
    timestamp: datetime
    is_read: bool = False


class SendMessageData(BaseModel):
    contents: str
