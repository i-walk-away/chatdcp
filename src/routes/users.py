from fastapi import APIRouter, Depends

from src.core.dependencies.security.user import get_user_from_jwt
from src.core.dependencies.services.chat_service import get_chat_service
from src.core.dependencies.services.user_service import get_user_service
from src.models.dto.chat import ChatDTO
from src.models.dto.user import CreateUserData, UserDTO
from src.services.chat_service import ChatService
from src.services.user_service import UserService

router = APIRouter(prefix='/user', tags=['Users'])


@router.get(path='', summary='Get all users')
async def get_users(
        user_service: UserService = Depends(get_user_service)
) -> list[UserDTO]:
    """
    Gets list of all users.
    """
    users = await user_service.get_all()
    return users


@router.get(path='/profile', summary='Current user\'s profile')
async def get_current_user_profile(
        user: UserDTO = Depends(get_user_from_jwt)
) -> UserDTO:
    """
    # Markdown string placeholder
    Endpoint description.

    ## Args
    `arg` - explanation
    """
    return user


@router.get(path='/chats', summary='Current user\'s list of chats')
async def get_current_users_chats(
        user: UserDTO = Depends(get_user_from_jwt),
        chat_service: ChatService = Depends(get_chat_service)
) -> list[ChatDTO]:
    """
    docst
    """
    chats = await chat_service.get_users_chats(user=user)

    return chats


@router.post(path='/create', summary='Create a new user')
async def create_user(
        user_data: CreateUserData,
        user_service: UserService = Depends(get_user_service)
) -> UserDTO:
    """
    Creates a new user.

    :param user_data: CreateUserData object, containing data neccessary to create a new user.
    :param user_service: Injected logic layer responsible for User operations.

    :return: UserDTO object representing a user.
    """
    user = await user_service.create_user(data=user_data)
    return user
