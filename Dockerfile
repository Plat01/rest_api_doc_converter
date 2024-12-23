FROM python:3.12-slim

WORKDIR /app

RUN apt update && apt install -y

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .