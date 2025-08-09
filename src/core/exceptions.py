from fastapi.exceptions import HTTPException


class MessageNotFound(HTTPException):
    def __init__(self, detail: str = 'Message not found'):
        super().__init__(status_code=404, detail=detail)


class UserNotFound(HTTPException):
    def __init__(self, detail: str = 'User not found'):
        super().__init__(status_code=404, detail=detail)


class UserAlreadyExists(HTTPException):
    def __init__(self, detail: str = 'User already exists'):
        super().__init__(status_code=409, detail=detail)


class InvalidCredentials(HTTPException):
    def __init__(self, detail: str = 'Invalid username or password.'):
        super().__init__(status_code=401, detail=detail)


class ChatNotFound(HTTPException):
    def __init__(self, detail: str = 'Chat not found'):
        super().__init__(status_code=404, detail=detail)
