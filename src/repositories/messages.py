from src.database.jsondb import JsonDB
from src.models.dto.message import Message
from src.utils.logger.logger import logger


class MessageRepository:
    def __init__(self):
        self.db = JsonDB(Message, 'Message')

    def create(self, model: Message):
        self.db.insert(model)

    def get(self, id_: int) -> None | Message:
        try:
            return self.db.get(id_)
        except Exception as e:
            logger.error(f'failed to find an item with the id {id_} in database: {e}')
            return None
