from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.dependencies.db import get_session
from src.repositories.users import UserRepository


def get_user_repository(
        session: AsyncSession = Depends(get_session)
) -> UserRepository:
    """
    Constructs an instance of ``UserRepository`` with SQLA Async Session injected.
    """

    return UserRepository(session=session)
