from fastapi import Depends

from src.core.dependencies.repositories.chat_repository import get_chat_repository
from src.core.dependencies.repositories.user_repository import get_user_repository
from src.repositories.chats import ChatRepository
from src.repositories.users import UserRepository
from src.services.chat_service import ChatService


def get_chat_service(
        repository: ChatRepository = Depends(get_chat_repository),
        user_repository: UserRepository = Depends(get_user_repository)
) -> ChatService:
    """
    Constructs an instance of ``ChatService`` with ``ChatRepository`` injected.
    """
    return ChatService(repository=repository, user_repository=user_repository)
