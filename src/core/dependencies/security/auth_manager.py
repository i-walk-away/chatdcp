from fastapi import Depends
from passlib.context import CryptContext

from src.core.auth_manager import AuthManager
from src.core.dependencies.security.crypt_context import get_crypt_context


def get_auth_manager(
        context: CryptContext = Depends(get_crypt_context)
) -> AuthManager:
    """
    Constructs an instance of ``AuthManager`` with ``passlib.CryptContext`` injected.

    :return: ``AuthManager`` object.
    """
    return AuthManager(context=context)
