from src.models.dto.message import SendMessageData
from src.models.dto.user import User

chmo = User(username='ev')
msg = SendMessageData(sender=chmo, contents='heheheha')


class Base:
    def __init__(self):
        pass
