from src.core.auth_manager import AuthManager
from src.core.exceptions import InvalidCredentials
from src.models.dto.auth import LoginCredentials
from src.repositories.users import UserRepository


class AuthService:
    def __init__(
            self,
            user_repository: UserRepository,
            auth_manager: AuthManager
    ):
        self.user_repository = user_repository
        self.auth_manager = auth_manager

    async def login(self, credentials: LoginCredentials) -> str:
        """
        Authenticates given credentials.

        :param credentials: LoginCredentials model
        :return: JSON Web Token
        """
        is_authenticated = await self._is_user_authenticated(
            username=credentials.username,
            password=credentials.plain_password
        )
        if not is_authenticated:
            raise InvalidCredentials

        return self.auth_manager.generate_jwt(input_data={"sub": credentials.username})

    async def _is_user_authenticated(self, username: str, password: str) -> bool:
        user = await self.user_repository.get_by_username(username=username)
        if not user:
            return False

        if not self.auth_manager.verify_password_against_hash(
                plain_password=password,
                hashed_password=user.hashed_password
        ):
            return False

        return True
