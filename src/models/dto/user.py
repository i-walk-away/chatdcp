from pydantic import BaseModel, Field


class User(BaseModel):
    id: int | None = Field(default=None, exclude=True)  # Поле для БД, исключается из схемы
    username: str
    gangster: bool = False
