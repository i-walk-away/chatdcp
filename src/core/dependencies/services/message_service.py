from fastapi import Depends

from src.core.dependencies.repositories.message_repository import get_message_repository
from src.repositories.messages import MessageRepository
from src.services.message_service import MessageService


def get_message_service(
        repository: MessageRepository = Depends(get_message_repository)
) -> MessageService:
    """
    Constructs an instance of MessageService with MessageRepository injected.
    """
    return MessageService(repository)
