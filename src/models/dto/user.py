from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str
    #hashed_password: str
    gangster: bool = False


class CreateUserData(BaseModel):
    username: str
    plain_password: str
