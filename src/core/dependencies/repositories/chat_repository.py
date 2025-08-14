from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.db import get_session
from src.repositories.chats import ChatRepository


def get_chat_repository(
        session: AsyncSession = Depends(get_session)
) -> ChatRepository:
    """
    Constructs an instance of ``ChatRepository`` with SQLA Async Session injected.
    """

    return ChatRepository(session=session)
