class AdvanceException(Exception):
    pass


class AdvanceExistsException(AdvanceException):
    def __str__(self) -> str:
        return 'Достижение с таким названием уже создано'


class AdvanceUserExistsException(AdvanceException):
    def __str__(self) -> str:
        return 'Достижение уже было добавлено пользователю'


class AdvanceUserNotFoundException(AdvanceException):
    def __str__(self) -> str:
        return 'Пользователь или достижение не найдено'
