from datetime import datetime

from src.models.dto.message import Message, SendMessageData
from src.repositories.messages import MessageRepository


class MessageService:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def get(self, message_id) -> None | Message:
        """
        Gets a Message by id from the database

        :param message_id: message id
        :return: Message
        """
        message = self.repository.get(message_id)
        if not message:
            return None

        return message

    def add(self, data: SendMessageData) -> Message:
        """
        Create a new Message instance

        :param data: SendMessageData object containing data neccessary
        to create an instance of Message
        :return: Message instance
        """
        message = Message(
            sender=data.sender,
            contents=data.contents,
            timestamp=datetime.now(),
            status='unread'
        )
        self.repository.create(message)

        return message
