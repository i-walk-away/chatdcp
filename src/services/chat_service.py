from src.core.exceptions import UserNotFound
from src.models.db import Chat, User
from src.models.dto.chat import ChatDTO, CreateChatData
from src.models.dto.user import UserDTO
from src.repositories.chats import ChatRepository
from src.repositories.users import UserRepository


class ChatService:
    def __init__(
            self,
            repository: ChatRepository,
            user_repository: UserRepository
    ):
        self.repository = repository
        self.user_repository = user_repository

    async def create_chat(self, chat_data: CreateChatData, user: UserDTO) -> ChatDTO:
        """

        """

        members_ids = list(set(chat_data.members))
        members_ids.append(user.id)

        members: list[User] = []

        for member_id in members_ids:
            member = await self.user_repository.get_by_id(user_id=member_id)

            if member is None:
                raise UserNotFound(f'User with the id {member_id} not found')

            members.append(member)

        chat = Chat(
            members=members
        )

        await self.repository.add(chat)
        await self.repository.session.commit()
        await self.repository.session.refresh(chat)

        return chat.to_dto()

    async def get_by_id(self, chat_id: int) -> ChatDTO:
        """
        Gets a ``Chat`` by id from the database.

        :param chat_id: ``Chat`` id
        :return: ``Chat``
        """
        chat = await self.repository.get_by_id(chat_id)

        return chat.to_dto()

    async def get_users_chats(self, user: UserDTO) -> list[ChatDTO]:
        """

        :param user:
        :return:
        """
        chats = await self.repository.get_chats_by_user_id(user.id)

        return [chat.to_dto() for chat in chats]
