import logging
import os
from dataclasses import dataclass
from pathlib import Path

from .exceptions import ConfigParseError

logger = logging.getLogger(__name__)


@dataclass
class DatabaseConfig:
    """ Конфиг к базе данных. """

    db_url: str
    # адрес к базе данных


@dataclass
class ServerStatus:
    """ Статус сервера. """

    status: str
    # Статус сервера: prod или dev


@dataclass
class LoggingConfig:
    """ Конфиг для логов. """

    render_json_logs: bool = False
    # рендер логов в json
    path: Path | None = None
    # путь до логов
    level: str = 'DEBUG'
    # уровень логирования


def get_str_env(key: str) -> str:
    """ Получение переменных из переменных окружения. """
    value = os.getenv(key)
    if not value:
        raise ConfigParseError(f'{key} не установлен в переменных окружения')
    return value


def load_server_status() -> ServerStatus:
    """ Загрузить конфиг со статусом сервера. """
    return ServerStatus(status=get_str_env('SERVER_STATUS'))


def load_logging_config() -> LoggingConfig:
    """ Загрузить конфиг для логов. """
    server_status = load_server_status().status
    path = None
    if server_status == 'prod':
        path = Path(get_str_env('LOG_PATH'))
        path.mkdir(exist_ok=True)
    return LoggingConfig(path=path)


def load_database_config() -> DatabaseConfig:
    """ Загрузить конфиг для подключения к базе данных """
    return DatabaseConfig(db_url=get_str_env('DB_URL'))
