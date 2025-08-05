from datetime import datetime

from sqlalchemy import String, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.models.db.base import Base
from src.models.dto.message import MessageDTO


class Message(Base):
    __tablename__ = 'messages'

    id: Mapped[int] = mapped_column(primary_key=True)
    contents: Mapped[str] = mapped_column(String(length=255))

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    # sender: Mapped['User'] = relationship(lazy='joined')
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def to_dto(self) -> MessageDTO:
        return MessageDTO(
            id=self.id,
            sender_id=self.sender_id,
            contents=self.contents,
            timestamp=self.timestamp
        )
