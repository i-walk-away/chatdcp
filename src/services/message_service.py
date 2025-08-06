from src.core.exceptions import MessageNotFound
from src.models.db.message import Message
from src.models.dto.message import MessageDTO, SendMessageData
from src.models.dto.user import UserDTO
from src.repositories.messages import MessageRepository
from src.repositories.users import UserRepository


class MessageService:
    def __init__(
            self,
            repository: MessageRepository,
            user_repository: UserRepository,
    ):
        self.repository = repository
        self.user_repository = user_repository

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

        :return: list of ``MessageDTO``
        """
        messages = await self.repository.get_all()

        return [message.to_dto() for message in messages]

    async def send_message(
            self,
            message_data: SendMessageData,
            sender_data: UserDTO
    ) -> MessageDTO:
        """
        Create a new ``Message`` instance

        :param sender_data: ``UserDTO`` object representing the user that has sent the message.
        :param message_data: ``SendMessageData`` object containing data neccessary
        to create an instance of ``Message``
        :return: ``Message`` instance
        """
        sender = await self.user_repository.get_by_id(sender_data.id)

        message = Message(
            contents=message_data.contents,
            sender=sender
        )

        await self.repository.add(message)
        await self.repository.session.commit()

        await self.repository.session.refresh(message)

        return message.to_dto()
