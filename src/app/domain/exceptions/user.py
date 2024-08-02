class UserException(Exception):
    pass


class UserNotFoundException(UserException):
    def __str__(self) -> str:
        return 'Пользователь не найден'
