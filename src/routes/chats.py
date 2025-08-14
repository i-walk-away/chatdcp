from fastapi import APIRouter, Depends

from src.core.dependencies.security.user import get_user_from_jwt
from src.core.dependencies.services.chat_service import get_chat_service
from src.models.dto.chat import ChatDTO, CreateChatData
from src.models.dto.user import UserDTO
from src.services.chat_service import ChatService

router = APIRouter(prefix='/chats', tags=['Chats'])


@router.post(path='/create', summary='Create a new chat')
async def create_chat(
        chat_data: CreateChatData,
        user: UserDTO = Depends(get_user_from_jwt),
        chat_service: ChatService = Depends(get_chat_service)
) -> ChatDTO:
    """

    :param user:
    :param chat_data:
    :param chat_service:
    :return:
    """
    chat = await chat_service.create_chat(chat_data=chat_data, user=user)

    return chat
