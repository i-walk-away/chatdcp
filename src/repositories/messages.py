from sqlalchemy import select

from src.core.exceptions import MessageNotFound
from src.models.db.message import Message
from src.models.db.user import User
from src.repositories.base import BaseRepository


class MessageRepository(BaseRepository):
    async def add(self, model: Message) -> None:
        self.session.add(model)

    async def get_by_id(self, id_: int) -> Message | None:
        statement = select(Message).where(Message.id == id_)
        result = await self.session.scalar(statement)

        return result

    async def get_all(self) -> list[Message]:
        statement = select(Message)
        result = await self.session.scalars(statement)

        return list(result)

