FROM python:3.13-alpine
WORKDIR /app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # Poetry's configuration:
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry' \
  POETRY_HOME='/usr/local' \
  POETRY_VERSION=2.0.1

RUN apk --no-cache add curl
RUN curl -sSL https://install.python-poetry.org | python -
COPY pyproject.toml poetry.lock /app/
RUN poetry install $(test "$YOUR_ENV" == production && echo "--only=main") --no-interaction --no-ansi

COPY . /app

EXPOSE 5000/tcp
CMD ["uvicorn", "--workers", "4", "cc.app:app", "--port", "5000", "--host", "0.0.0.0"]
