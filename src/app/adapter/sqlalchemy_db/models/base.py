import uuid

from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """ Базовая модель алхимии. """

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True,
        default=uuid.uuid4,
        comment='Уникальный идентификатор',
        autoincrement=False  # Генерация ID будет происходить не на стороне БД
    )

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()
