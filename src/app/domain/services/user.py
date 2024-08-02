from app.domain.exceptions import UserNotFoundException
from app.domain.models import Users


class UserService:
    def check_user(self, user: Users | None) -> None:
        if user is None:
            raise UserNotFoundException()
