from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt import decode
from jwt.exceptions import InvalidTokenError

from cfg.cfg import settings
from src.core.dependencies.services.user_service import get_user_service
from src.core.exceptions import UserNotFound, InvalidCredentials
from src.models.dto.user import UserDTO
from src.services.user_service import UserService

scheme_factory = HTTPBearer(auto_error=False)


async def get_user_from_jwt(
        user_service: UserService = Depends(get_user_service),
        jwt: HTTPAuthorizationCredentials = Depends(scheme_factory)
) -> UserDTO:
    """
    Gets user from the given JSON Web Token.

    :param user_service:
    :param jwt:
    :return:
    """

    if not jwt:
        raise InvalidCredentials

    try:
        decoded_token: dict = decode(
            jwt=jwt.credentials,
            key=settings.auth.jwt_secret_key,
            algorithms=[settings.auth.jwt_algorithm]
        )
        username = decoded_token.get('sub')
        if not username:
            raise InvalidCredentials
    except InvalidTokenError as e:
        raise InvalidCredentials from e

    try:
        user = await user_service.get_by_username(username=username)
    except UserNotFound:
        raise InvalidCredentials

    return user
