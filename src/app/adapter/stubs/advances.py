from abc import ABC

from app.adapter.sqlalchemy_db.models import Advances
from app.application.protocols import ReadingAll


class StubAdvanceGateway(ReadingAll[Advances], ABC):
    pass
