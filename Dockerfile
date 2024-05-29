FROM python:3.12

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=true
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Установка poetry
RUN pip install poetry
ENV PATH="$POETRY_HOME/bin:$HOME/.local/bin:$PATH"

WORKDIR /app

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry install --only main

COPY ./src/ ./src/

COPY ./videomaker/ ./videomaker/
COPY ./manage.py .
