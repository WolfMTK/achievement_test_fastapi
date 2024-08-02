FROM python:3.12.3

RUN pip install gunicorn

COPY src src

COPY pyproject.toml pyproject.toml

COPY alembic.ini alembic.ini

RUN pip install .

CMD gunicorn "app.main:create_app()" --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
