from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.db import Base
from src.models.dto.user import UserDTO


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(length=30))
    hashed_password: Mapped[str] = mapped_column(String(length=255))

    chats: Mapped[list['Chat']] = relationship(
        argument='Chat',
        back_populates='members',
        secondary='chat_members',
        lazy='joined'
    )

    gangster: Mapped[bool] = mapped_column(default=False)

    def to_dto(self) -> UserDTO:
        return UserDTO(
            id=self.id,
            username=self.username,
            gangster=self.gangster,
        )
