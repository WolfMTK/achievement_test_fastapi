import datetime as dt
from dataclasses import dataclass

from app.domain.models import UserId, AchievementId
from .achievement import Achievements
from .user import Users


@dataclass
class UsersAchievements:
    user_id: UserId
    achievement_id: AchievementId
    date_on: dt.datetime
    achievement: Achievements
    user: Users
