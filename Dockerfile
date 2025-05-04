FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml ./
COPY uv.lock ./

COPY servers/time.py .

RUN uv sync --frozen

ENV PORT=10000
CMD ["uv", "run", "fastmcp", "run", "time.py"]