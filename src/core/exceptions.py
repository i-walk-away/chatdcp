from fastapi.exceptions import HTTPException


class MessageNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail='Message not found')


class UserNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail='User not found')


class UserAlreadyExists(HTTPException):
    def __init__(self):
        super().__init__(status_code=409, detail='User already exists')


class InvalidCredentials(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail='Invalid username or password')
