from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.db.base import Base
from src.models.dto.user import UserDTO


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(length=30))
    gangster: Mapped[bool] = mapped_column()

    def to_dto(self) -> UserDTO:
        return UserDTO(
            username=self.username,
            gangster=self.gangster
        )
