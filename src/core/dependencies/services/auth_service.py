from fastapi import Depends

from src.core.auth_manager import AuthManager
from src.core.dependencies.repositories.user_repository import get_user_repository
from src.core.dependencies.security.auth_manager import get_auth_manager
from src.repositories.users import UserRepository
from src.services.auth_service import AuthService


def get_auth_service(
        repository: UserRepository = Depends(get_user_repository),
        auth_manager: AuthManager = Depends(get_auth_manager)
) -> AuthService:
    """
    Constructs an instance of ``AuthService`` with ``UserRepository`` and ``AuthManager``
    injected.
    """
    return AuthService(user_repository=repository, auth_manager=auth_manager)
