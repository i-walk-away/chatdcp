from sqlalchemy import select

from src.models.db.user import User
from src.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    async def add(self, model: User) -> None:
        self.session.add(model)

    async def get_all(self) -> list[User]:
        statement = select(User)
        result = await self.session.scalars(statement)

        return list(result)

    async def get_by_username(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        result = await self.session.scalar(statement)

        return result

    async def get_by_id(self, id_: int) -> User | None:
        statement = select(User).where(User.id == id_)
        result = await self.session.scalar(statement)

        return result
