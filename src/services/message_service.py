from datetime import datetime

from src.models.dto.message import Message, SendMessageData
from src.repositories.messages import MessageRepository


class MessageService:
    def __init__(self, repository: MessageRepository):
        self.repository = repository

    def get_by_id(self, message_id: int) -> None | Message:
        """
        Gets a Message by id from the database

        :param message_id: message id
        :return: Message
        """
        message = self.repository.get_by_id(message_id)
        if not message:
            return None

        return message

    def get_all(self) -> None | list[Message]:
        """
        Gets all messages from the databes

        :return:
        """
        messages = self.repository.get_all()
        return messages


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
