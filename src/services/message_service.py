from src.core.exceptions import MessageNotFound, ChatNotFound
from src.models.db.message import Message
from src.models.dto.message import MessageDTO, SendMessageData
from src.models.dto.user import UserDTO
from src.repositories.messages import MessageRepository
from src.repositories.users import UserRepository
from src.services.chat_service import ChatService


class MessageService:
    def __init__(
            self,
            repository: MessageRepository,
            user_repository: UserRepository,
            chat_service: ChatService
    ):
        self.repository = repository
        self.user_repository = user_repository
        self.chat_service = chat_service

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

    async def get_all_from_chat(self, chat_id: int) -> None | list[MessageDTO]:
        """
        Gets all ``Messages`` in the Chat from the database.

        :return: list of ``MessageDTO``.
        """
        messages = await self.repository.get_all_from_chat(chat_id=chat_id)
        if not messages:
            raise ChatNotFound

        return [message.to_dto() for message in messages]

    async def get_unreads_from_chat(self, chat_id: int) -> None | list[MessageDTO]:
        unread_messages = await self.repository.get_unreads_from_chat(chat_id=chat_id)

        return [message.to_dto() for message in unread_messages]

    async def get_unreads_from_all_chats(self, user: UserDTO) -> list[MessageDTO]:
        chats_to_fetch = await self.chat_service.get_users_chats(user=user)
        chat_ids = [chat.id for chat in chats_to_fetch]

        unread_messages: list[MessageDTO] = []

        for chat_id in chat_ids:
            unread_messages.extend(await self.get_unreads_from_chat(chat_id))

        return unread_messages

    async def send_message(
            self,
            message_data: SendMessageData,
            sender_data: UserDTO,
    ) -> MessageDTO:
        """
        Create a new ``Message`` instance

        :param sender_data: ``UserDTO`` object representing the user that has sent the message.
        :param message_data: ``SendMessageData`` object containing data neccessary
        to create an instance of ``Message``

        :return: ``MessageDTO`` object representing the Message.
        """
        sender = await self.user_repository.get_by_id(sender_data.id)

        message = Message(
            contents=message_data.contents,
            sender=sender,
            chat_id=message_data.chat_id,
            reply_to=message_data.reply_to

        )

        await self.repository.add(message)
        await self.repository.session.commit()

        await self.repository.session.refresh(message)

        return message.to_dto()
