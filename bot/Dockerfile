FROM python:3.12-slim AS base

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get remove -y curl && apt-get autoremove -y && apt-get clean

WORKDIR /bot


FROM base AS builder

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --only main


FROM builder AS prod

COPY --from=builder /bot /bot/
COPY . .
CMD ["python3", "src/main.py"]