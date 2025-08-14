from typing import Optional

from pydantic import BaseModel

from src.models.dto.message import MessageDTO
from src.models.dto.user import UserDTO


class ChatDTO(BaseModel):
    id: int
    members: list[UserDTO]
    messages: list[MessageDTO]


class ChatOverview(BaseModel):
    id: int
    last_message: Optional[MessageDTO]


class CreateChatData(BaseModel):
    members: list[int]
