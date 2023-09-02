# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /phonebook

RUN pip install fastapi uvicorn sqlalchemy psycopg2

# Копируем файлы приложения в контейнер
COPY main.py /phonebook/main.py

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /phonebook

# Открываем порт, на котором будет работать приложение
EXPOSE 8000

# Запускаем приложение при старте контейнера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
