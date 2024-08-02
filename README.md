# Описание

API для работы с достижениями

# Технологии

| Python3.12 | Docker         | FastAPI     |
|------------|----------------|-------------|
| **Nginx**  | **SQLAlchemy** | **Alembic** |

# Локальный запуск проекта

1. Установить python: [официальный установщик](https://www.python.org/downloads/release/python-3124/)

2. Создать виртуальное окружение:

    * Windows: `py -m venv venv`

    * Linux: `python3.12 -m venv venv`

3. Активировать виртуальное окружение:

    * Windows: `. venv\Scripts\Activate`

    * Linux: `. venv/bin/activate`

4. Установить необходимые переменные окружения:

   ```
   DB_URL - URL к базе данных
   SERVER_STATUS - статус сервера (dev или prod)
   LOG_PATH - путь сохранения логов (при выставленом статусе сервера dev логи не сохраняются)
   ```

5. Установить необходимые зависимости: `pip install -e .[dev]`

6. Применить миграции: `alembic upgrade head`

7. Запустить проект: `uvicorn --factory app.main:create_app --reload`

# Запуск проекта с применением Docker Compose

1. Установить [Docker и плагин Docker Compose](https://docs.docker.com/engine/install/)

2. Создать файл с названием **.env** и добавить указанный параметры, которые указаны в примере [example](example.env),
   со своими значениями

3. Создать build: `docker compose build`

4. Запустить сервисы: `docker compose up`

5. Применить миграции: `docker compose -f docker-compose.yml exec backend alembic upgrade head`

**Для удобства запуска создан MakeFile**

3. Создать build: `make build`

4. Запустить сервисы: `make run`

5. Применить миграции: `make migrate`

# Спецификация к API

### При локальном запуске

1. Swagger-UI (вместо port подставьте свой порт): http://localhost:port/docs

2. Redoc (вместо port подставьте свой порт): http://localhost:port/redoc

### При запуске в контейнере

1. Swagger-UI (вместо port и addr подставьте свой адрес и порт): http://addr:port/api/docs

2. Redoc (вместо port и addr подставьте свой адрес и порт): http://addr:port/api/redoc

# Тестовые данные

Файл с тестовыми данными: [data.sql](./data/data.sql)

# Лицензия

[MIT](LICENSE)
