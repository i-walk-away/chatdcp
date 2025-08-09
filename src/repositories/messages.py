from sqlalchemy import select, update

from src.models.db.message import Message
from src.repositories.base import BaseRepository


class MessageRepository(BaseRepository):
    async def add(self, model: Message) -> None:
        self.session.add(model)

    async def get_by_id(self, id_: int) -> Message | None:
        statement = select(Message).where(Message.id == id_)
        result = await self.session.scalar(statement)

        return result

    async def get_all_from_chat(self, chat_id: int) -> list[Message]:
        statement = select(Message).where(Message.chat_id == chat_id)
        result = await self.session.scalars(statement)

        return list(result.unique())

    async def get_unreads_from_chat(self, chat_id: int) -> list[Message]:
        statement = select(Message).where(Message.chat_id == chat_id).where(Message.is_read == False)
        result = await self.session.scalars(statement)

        return list(result.unique())

    async def update(self, id_: int, updated_data: dict) -> Message:
        statement = update(Message).where(Message.id == id_).values(**updated_data)
        await self.session.execute(statement)

        return await self.get_by_id(id_)
