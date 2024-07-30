import datetime as dt
from dataclasses import dataclass

from app.domain.models import UserId, AdvanceId
from .advance import Advances
from .user import Users


@dataclass
class UsersAdvances:
    user_id: UserId
    advance_id: AdvanceId
    date_on: dt.datetime
    advance: Advances
    user: Users
