
# Шаблон бэкенда на FastAPI

Это базовый шаблон проекта бэкенда, построенный на FastAPI, SQLAlchemy, Alembic и Uvicorn

## Возможности

- **FastAPI**: высокопроизводительный веб-фреймворк на Python для создания API.
- **SQLAlchemy**: инструмент для работы с SQL и ORM для Python.
- **Alembic**: система управления миграциями базы данных.
- **Uvicorn**: ASGI-сервер для запуска приложения.
- **Pydantic**: валидация данных и управление настройками.

## Требования

- Python 3.8 и выше
- PostgreSQL (или другая СУБД, поддерживаемая SQLAlchemy)
- Git

## Установка

1. **Клонировать репозиторий**

   ```bash
   git clone https://github.com/your-username/fastapi-backend-template.git
   cd fastapi-backend-template
   ```

2. **Создать и активировать виртуальное окружение**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

3. **Установить зависимости**

   ```bash
   pip install -r requirements.txt
   ```

4. **Настроить переменные окружения**

   Создайте файл `.env` в корне проекта и добавьте:

   ```ini
   DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/dbname
   ```

5. **Инициализировать базу данных**

   ```bash
   alembic upgrade head
   ```


## Использование

- **Запуск миграций**

  ```bash
  alembic revision --autogenerate -m "Добавить новую таблицу"
  alembic upgrade head
  ```

- **Запуск приложения**

  ```bash
  uvicorn app.main:app --reload
  ```
  или запустите или main.py через IDE.
  
После запуска API будет доступно по адресу `http://127.0.0.1:8000`.

- **Интерактивная документация**

  - Swagger UI: http://127.0.0.1:8000/docs
  - ReDoc: http://127.0.0.1:8000/redoc

## Тестирование

*В разработке...*

## Участие в разработке

Создавайте форк или клонируйте репозиторий, чтобы добавлять любые изменения на ваш вкус.

## Лицензия

Проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).


