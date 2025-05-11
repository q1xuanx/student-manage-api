FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY . /app

WORKDIR /app
RUN uv venv
RUN uv sync --frozen --no-cache

CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--port", "80", "--host", "0.0.0.0", "--workers", "16"]
