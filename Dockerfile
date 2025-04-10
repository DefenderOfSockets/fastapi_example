# --- Базовый образ с Python ---
FROM python:3.12-slim

# --- Переменные окружения ---
ENV POETRY_VERSION=1.8.2 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# --- Установка poetry ---
RUN pip install --no-cache-dir poetry==$POETRY_VERSION

# --- Установка зависимостей ---
WORKDIR /app
COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi

# --- Копирование приложения ---
COPY backend /app/backend

# --- Команда запуска ---
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
