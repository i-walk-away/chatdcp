from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.db import get_session
from src.repositories.messages import MessageRepository


def get_message_repository(
        session: AsyncSession = Depends(get_session)
) -> MessageRepository:
    """
    Constructs an instance of MessageRepository with AsyncSession injected
    """

    return MessageRepository(session=session)
