from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.db import Base
from src.models.dto.chat import ChatDTO


class Chat(Base):
    __tablename__ = 'chats'

    id: Mapped[int] = mapped_column(primary_key=True)

    members: Mapped[list['User']] = relationship(
        argument='User',
        secondary='chat_members',
        lazy='joined'
    )

    messages: Mapped[list['Message']] = relationship(
        argument='Message',
        lazy='joined'
    )

    def to_dto(self) -> ChatDTO:
        return ChatDTO(
            id=self.id,
            members=[user.to_dto() for user in self.members],
            messages=[message.to_dto() for message in self.messages]
        )


class ChatMembers(Base):
    __tablename__ = 'chat_members'

    chat_id: Mapped[int] = mapped_column(ForeignKey('chats.id'), primary_key=True)
    member_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
