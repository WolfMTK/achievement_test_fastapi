import logging

from app.adapter.stubs import StubUserGateway
from app.application.dto import UserInfoDTO
from app.application.protocols import Interactor
from app.domain.models import UserId
from app.domain.services import UserService

logger = logging.getLogger(__name__)


class GetUserInfo(Interactor[UserId, UserInfoDTO]):
    """ Получение информации о пользователе. """

    def __init__(
            self,
            service: UserService,
            gateway: StubUserGateway,
    ) -> None:
        self.service = service
        self.gateway = gateway

    async def __call__(self, data: UserId) -> UserInfoDTO:
        user = await self.gateway.get(id=data)
        self.service.check_user(user)
        logger.debug(f'Get info about the user {user.id}')
        return UserInfoDTO(
            id=user.id,
            name=user.name,
            language=user.language
        )
