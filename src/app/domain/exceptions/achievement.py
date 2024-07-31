class AchievementException(Exception):
    pass


class AchievementExistsException(AchievementException):
    def __str__(self) -> str:
        return 'Достижение с таким названием уже создано'


class AchievementUserExistsException(AchievementException):
    def __str__(self) -> str:
        return 'Достижение уже было добавлено пользователю'


class AchievementUserNotFoundException(AchievementException):
    def __str__(self) -> str:
        return 'Пользователь или достижение не найдено'


class MaxAchievementsNotFound(AchievementException):
    def __str__(self) -> str:
        return 'Пользователя с максимальным количеством достижений не найдено'


class MaxPointsNotFound(AchievementException):
    def __str__(self) -> str:
        return 'Пользователя с максимальными очками достижений не найден'


class MaxPointsDiffNotFoundException(AchievementException):
    def __str__(self) -> str:
        return ('Пользователи с максимальной разностью '
                'очков достижений не найдены')


class MinPointsDiffNotFoundException(AchievementException):
    def __str__(self) -> str:
        return ('Пользователи с минимальной разностью '
                'очков достижений не найдены')
