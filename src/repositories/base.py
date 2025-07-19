from abc import ABC, abstractmethod

from pydantic import BaseModel


class BaseRepository(ABC):

    @abstractmethod
    def create(self, model: BaseModel):
        raise NotImplementedError

    @abstractmethod
    def get(self, id_: int) -> None | BaseModel:
        raise NotImplementedError
