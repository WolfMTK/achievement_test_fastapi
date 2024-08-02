from abc import ABC

from app.adapter.sqlalchemy_db.models import Users
from app.application.protocols import (
    Reading,
)


class StubUserGateway(Reading[Users],
                      ABC):
    pass
