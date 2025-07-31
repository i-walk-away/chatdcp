from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from src.models.db.base import Base


class BaseRepository(ABC):
    def __init__(self, session: AsyncSession):
        self.session = session

    @abstractmethod
    async def add(self, model: Base) -> None:
        """
        Adds a given model to the database session.
        Does not commit the session.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, id_: int) -> Base | None:
        """
        Gets a model by its ID from the database.

        :return: SQLAlchemy model inherited from Base if found; otherwise ``None``.
        """
        raise NotImplementedError

    @abstractmethod
    async def get_all(self) -> list[Base] | None:
        """
        Gets a list of all models from the database.

        :return: list of SQLA models inherited from Base if found; otherwise ``None``.
        """
        raise NotImplementedError
