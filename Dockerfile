# Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.12-slim-bookworm

# Install uv using the official distroless image.
# Pinning to a specific version (e.g., :0.6.11) is recommended for reproducibility.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set the working directory in the container
WORKDIR /app

# Copy project definition (pyproject.toml) and lock file (if available)
# Assumes pyproject.toml exists in your project root (shellserver).
# If you generate and use a lock file (uv.lock), uncomment the second COPY line for reproducible builds.
COPY pyproject.toml ./
COPY uv.lock ./

# Install dependencies using uv sync.
# Leverages Docker layer caching via --mount=type=cache.
# --frozen ensures installs match the lock file (if provided and copied). Remove if no lock file.
# --no-install-project skips installing the local project code in this layer, optimizing caching.
# NOTE: This command relies on 'pyproject.toml' correctly listing dependencies, including 'mcp'.
# Ensure the 'mcp' package is resolvable based on your project setup (see pyproject.toml notes).
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# Copy the application code into the container
COPY server.py .
# If you decided to vendor the 'mcp' package (copying it into shellserver), uncomment the next line:
# COPY ./mcp ./mcp

# Install the project itself using uv sync.
# This step makes your 'shellserver' project available in the environment managed by uv.
# Use --frozen if you have a lock file copied.
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Define the command to run the application using 'uv run'
CMD ["uv", "run", "server.py"]
