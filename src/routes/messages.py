from fastapi import APIRouter, Depends

from src.core.dependencies.security.user import get_user_from_jwt
from src.core.dependencies.services.message_service import get_message_service
from src.models.dto.message import SendMessageData, MessageDTO
from src.models.dto.user import UserDTO
from src.services.message_service import MessageService

router = APIRouter(prefix='/messages', tags=['Messages'])


@router.post(path='', summary='Create new message')
async def send_message(
        data: SendMessageData,
        message_service: MessageService = Depends(get_message_service),
        user: UserDTO = Depends(get_user_from_jwt)
) -> MessageDTO:
    """
    Create a new message.

    :param data: ``SendMessageData`` instance containing the contents of the message.
        create a new message.
    :param user: ``UserDTO`` object representing the current user.
    :param message_service: Injected logic layer responsible for all Message operations.

    :return: ``MessageDTO`` object representing a created message.
    """
    message = await message_service.send_message(message_data=data, sender=user)
    return message


@router.get(path='', summary='Get all messages')
async def get_messages(
        service: MessageService = Depends(get_message_service)
) -> list[MessageDTO]:
    """
    Gets all messages.

    :param service: Injected logic layer responsible for all Message operations.

    :return: List of ``MessageDTO`` objects representing the messages.
    """
    messages = await service.get_all()
    return messages


@router.get(path='/{message_id}', summary='Get message by id')
async def get_message_by_id(
        message_id: int,
        service: MessageService = Depends(get_message_service)
) -> MessageDTO:
    """
    Gets a message by the given ID.

    :param message_id: ID of a message
    :param service: Injected logic layer responsible for all Message operations.
    """
    message = await service.get_by_id(message_id)
    return message
