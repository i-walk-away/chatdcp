from sqlalchemy import select

from src.models.db import User
from src.models.db.chat import Chat
from src.repositories.base import BaseRepository


class ChatRepository(BaseRepository):
    async def add(self, model: Chat) -> None:
        self.session.add(model)

    async def get_by_id(self, id_: int) -> Chat | None:
        statement = select(Chat).where(Chat.id == id_)
        result = await self.session.scalar(statement)

        return result

    async def get_chats_by_user_id(self, user_id: int) -> list[Chat]:
        statement = select(Chat).join(Chat.members).where(User.id == user_id)
        result = await self.session.scalars(statement)

        return list(result.unique())
