from fastapi import APIRouter, Depends

from src.dependencies.services.message_service import get_message_service
from src.models.dto.message import SendMessageData
from src.services.message_service import MessageService

router = APIRouter(prefix='/messages')


@router.post(path='/', summary='Create new message')
def send_message(
        data: SendMessageData,
        service: MessageService = Depends(get_message_service)
):
    message = service.add(data)
    return message


@router.get(path='/', summary='Get all messages')
def get_messages(
        service: MessageService = Depends(get_message_service)
):
    messages = service.get_all()
    return messages


@router.get(path='/{message_id}', summary='Get message by id')
def get_message_by_id(
        message_id: int,
        service: MessageService = Depends(get_message_service)
):
    message = service.get_by_id(message_id)
    return message
