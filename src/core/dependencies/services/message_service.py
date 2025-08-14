from fastapi import Depends

from src.core.dependencies.repositories.chat_repository import get_chat_repository
from src.core.dependencies.repositories.message_repository import get_message_repository
from src.core.dependencies.repositories.user_repository import get_user_repository
from src.repositories.chats import ChatRepository
from src.repositories.messages import MessageRepository
from src.repositories.users import UserRepository
from src.services.message_service import MessageService


def get_message_service(
        repository: MessageRepository = Depends(get_message_repository),
        user_repository: UserRepository = Depends(get_user_repository),
        chat_repository: ChatRepository = Depends(get_chat_repository)
) -> MessageService:
    """
    Constructs an instance of ``MessageService`` with ``MessageRepository``
    and ``UserRepository`` injected.
    """
    return MessageService(
        repository=repository,
        user_repository=user_repository,
        chat_repository=chat_repository
    )
