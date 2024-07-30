from sqlalchemy.orm import DeclarativeBase, declared_attr


class BaseModel(DeclarativeBase):
    """ Базовая модель алхимии. """

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
