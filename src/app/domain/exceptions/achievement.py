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


class MaxAchievementsNotFoundException(AchievementException):
    def __str__(self) -> str:
        return 'Пользователя с максимальным количеством достижений не найдено'
