from pydantic import BaseModel

from src.models.dto.message import MessageDTO
from src.models.dto.user import UserDTO


class ChatDTO(BaseModel):
    id: int
    members: list[UserDTO]
    messages: list[MessageDTO]


class CreateChatData(BaseModel):
    members: list[int]
