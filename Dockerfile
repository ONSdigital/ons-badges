# ==============================
# 1. Builder Stage (Python Dependencies)
# ==============================
FROM python:3.13-slim AS builder

# Set environment variables for Poetry
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    PATH="/app/.venv/bin:/root/.local/bin:$PATH"

# Install system dependencies (only required for build)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry in builder
RUN curl -sSL https://install.python-poetry.org | python3 -

# Set working directory
WORKDIR /app

# Copy only dependency files to leverage caching
COPY pyproject.toml poetry.lock ./

# Install dependencies inside the project virtual environment
RUN poetry install --no-root --no-dev

# ==============================
# 2. Frontend Builder Stage (Vite + Tailwind)
# ==============================
FROM node:20 AS frontend-builder

# Set working directory inside frontend folder
WORKDIR /frontend

# Copy package.json and install dependencies (better caching)
COPY frontend/package.json frontend/package-lock.json ./
RUN npm install --frozen-lockfile

# Copy the rest of the frontend source files
COPY frontend ./

# Build Vite output directly into FastAPI's `app/static/`
RUN npm run build

# ==============================
# 3. Final Stage (Runtime)
# ==============================
FROM python:3.13-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:/root/.local/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy Poetry from builder
COPY --from=builder /root/.local /root/.local

# Copy installed Python dependencies (Poetry virtual environment)
COPY --from=builder /app/.venv /app/.venv

# Copy app
COPY app ./app

# Copy the frontend build output
COPY --from=frontend-builder /frontend/app/static ./app/static

# Copy the pyproject.toml file
COPY pyproject.toml pyproject.toml

# Run Poetry
CMD ["poetry", "run", "main"]
