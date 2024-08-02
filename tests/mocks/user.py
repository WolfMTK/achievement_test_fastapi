import uuid
from typing import Any

from app.adapter.stubs import StubUserGateway
from app.domain.enums import Language
from app.domain.models import Users


class UserGatewayMock(StubUserGateway):
    def __init__(self):
        self.is_user = True
        self._user_id = uuid.uuid4()

    @property
    def user_id(self) -> uuid.UUID:
        return self._user_id

    async def get(self, **kwargs: Any) -> Users | None:
        if self.is_user:
            return Users(
                id=self.user_id,
                name='test',
                language=Language.RU
            )
