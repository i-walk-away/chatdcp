from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.db import Base
from src.models.dto.message import MessageDTO


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(ForeignKey('chats.id'))

    sender: Mapped['User'] = relationship(
        argument='User',
        lazy='joined'
    )
    sender_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    contents: Mapped[str] = mapped_column(String(length=1941))

    reply_to: Mapped[int] = mapped_column(nullable=True)
    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    is_read: Mapped[bool] = mapped_column(default=False)

    def to_dto(self) -> MessageDTO:
        return MessageDTO(
            id=self.id,
            chat_id=self.chat_id,
            sender=self.sender.to_dto(),
            contents=self.contents,
            timestamp=self.timestamp,
            reply_to=self.reply_to,
            is_read=self.is_read
        )
