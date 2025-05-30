FROM python:3.12-slim AS base

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONUNBUFFERED=1 

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

WORKDIR /bot


FROM base AS builder

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main


FROM builder AS dev

WORKDIR /bot

COPY --from=builder /bot /bot/
RUN poetry install --no-root
COPY . .
CMD ["python3", "bot/src/main.py"]


FROM builder AS prod

COPY --from=builder /bot /bot/
COPY . .
CMD ["python3", "bot/src/main.py"]