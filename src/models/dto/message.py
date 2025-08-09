from datetime import datetime

from pydantic import BaseModel

from src.models.dto.user import UserDTO


class MessageDTO(BaseModel):
    """
    DTO Model representing a ``Message``.

    :var id: Message id
    :var chat_id: ChatDTO object representing the ``Chat`` where the message belongs.
    :var sender: UserDTO object representing the sender (User) of the message
    :var contents: The contents of the message. Essentially the message itself.
    :var reply_to: Reference to the Message this one is a reply to.
    :var timestamp: Date and time at which the message was sent.
    :var is_read: Boolean indicating whether the message was read by the recipient.
    """
    id: int
    chat_id: int
    sender: UserDTO
    contents: str

    reply_to: int

    timestamp: datetime
    is_read: bool = False


class SendMessageData(BaseModel):
    """
    Object containing the data neccessary to construct a ``Message``.

    :var chat: ChatDTO object representing the ``Chat`` where the message belongs.
    :var contents: The contents of the message. Essentially the message itself.
    :var reply_to: Reference to the Message this one is a reply to.
    """
    chat_id: int
    contents: str

    reply_to: int
