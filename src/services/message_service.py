from src.core.exceptions import MessageNotFound
from src.models.db.message import Message
from src.models.dto.message import MessageDTO, SendMessageData
from src.repositories.messages import MessageRepository


class MessageService:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    async def get_by_id(self, message_id: int) -> MessageDTO:
        """
        Gets a ``Message`` by id from the database

        :param message_id: ``Message`` id
        :return: ``Message``
        """
        message = await self.repository.get_by_id(message_id)
        if not message:
            raise MessageNotFound

        return message.to_dto()

    async def get_all(self) -> None | list[MessageDTO]:
        """
        Gets all ``Messages`` from the databes

        :return: list of MessageDTO
        """
        messages = await self.repository.get_all()

        return [message.to_dto() for message in messages]

    async def add(self, data: SendMessageData) -> MessageDTO:
        """
        Create a new ``Message`` instance

        :param data: ``SendMessageData`` object containing data neccessary
        to create an instance of ``Message``
        :return: ``Message`` instance
        """

        message = Message(
            contents=data.contents,
            sender_id=data.sender.id
        )

        await self.repository.add(message)
        await self.repository.session.commit()

        await self.repository.session.refresh(message)

        return message.to_dto()
