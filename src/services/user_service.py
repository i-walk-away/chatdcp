from src.core.auth_manager import AuthManager
from src.core.exceptions import UserNotFound, UserAlreadyExists
from src.models.db.user import User
from src.models.dto.user import UserDTO, CreateUserData
from src.repositories.users import UserRepository


class UserService:
    def __init__(self, repository: UserRepository, auth_manager: AuthManager):
        self.repository = repository
        self.auth_manager = auth_manager

    async def get_by_username(self, username: str) -> UserDTO | None:
        """
        Gets a user by username from the database.

        :param username: user's username
        :return: UserDTO representing a user.
        """
        user = await self.repository.get_by_username(username=username)

        if not user:
            return None

        return user.to_dto()

    async def get_by_id(self, user_id: int) -> UserDTO:
        """
        Get a user by id from the database.

        :param user_id: user's id
        :return: UserDTO representing a user.
        """
        user = await self.repository.get_by_id(user_id=user_id)

        if not user:
            raise UserNotFound

        return user.to_dto()

    async def get_all(self) -> list[UserDTO]:
        """
        Gets all users from the database.

        :return: A list of UserDTO objects each representing a user.
        """
        users = await self.repository.get_all()

        return [user.to_dto() for user in users]

    async def create_user(self, data: CreateUserData) -> UserDTO:
        """
        Creates a new user in the database.

        :param data: ``CreateUserData`` model containing data neccessary to create a new user.

        :return: ``UserDTO`` object representing a newly created user.

        :raises UserAlreadyExists: if the username provided in ``CreateUserData``
            already points to an existing user.
        """
        user = await self.get_by_username(data.username)
        if user:
            raise UserAlreadyExists

        hashed_password = self.auth_manager.hash_password(data.plain_password)

        user = User(
            username=data.username,
            hashed_password=hashed_password
        )

        await self.repository.add(user)
        await self.repository.session.commit()

        await self.repository.session.refresh(user)

        return user.to_dto()

    # async def get_user_info(self, user_id: int) -> UserDTO:
    #     """
    #     Gets given User's info.
    #
    #     :param user_id: user's ID
    #     :return: `UserDTO` object representing
    #     """
    #     user = await self.repository.get_by_id(id_=user_id)
    #     return user.to_dto()
