from fastapi import APIRouter, Depends

from src.core.dependencies.services.user_service import get_user_service
from src.models.dto.user import CreateUserData, UserDTO
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

