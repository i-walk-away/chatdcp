from src.database.jsondb import JsonDB
from src.models.dto.user import User
from src.utils.logger.logger import logger


class UserRepository:
    def __init__(self):
        self.db = JsonDB(User, 'User')

    def create(self, model: User):
        self.db.insert(model)

    def get_by_id(self, id_: int) -> None | User:
        try:
            return self.db.get_by_id(id_)
        except Exception as e:
            logger.error(f'failed to find a User with the id {id_} in database: {e}')
            return None

    def get_all(self) -> list[User]:
        return self.db.get_all()
