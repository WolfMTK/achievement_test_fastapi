import os
from dataclasses import dataclass

from .exceptions import ConfigParseError


@dataclass
class DatabaseConfig:
    """ Конфиг к базе данных. """

    db_url: str
    # адрес к базе данных


def get_str_env(key: str) -> str:
    """ Получение переменных из переменных окружения. """
    value = os.getenv(key)
    if not value:
        raise ConfigParseError(f'{key} не установлен в переменных окружения')
    return value


def load_database_config() -> DatabaseConfig:
    """ Загрузить конфиг для подключения к базе данных """
    return DatabaseConfig(db_url=get_str_env('DB_URL'))
