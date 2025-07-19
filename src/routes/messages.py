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
