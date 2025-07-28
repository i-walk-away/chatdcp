from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str
    gangster: bool = False
