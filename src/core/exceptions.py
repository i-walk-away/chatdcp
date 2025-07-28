from fastapi.exceptions import HTTPException


class MessageNotFound(HTTPException):
    def __init__(self):
        super().__init__(status_code=404, detail='Message not found')
