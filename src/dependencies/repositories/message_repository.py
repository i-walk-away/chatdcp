from src.repositories.messages import MessageRepository


def get_message_repository() -> MessageRepository:
    """
    Constructs an instance of MessageRepository.
    """
    # AsyncSession will be injected here when the app is refactored to use SQLA instead of
    # a self-made JSON database

    return MessageRepository()
