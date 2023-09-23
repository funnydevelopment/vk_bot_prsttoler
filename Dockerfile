FROM ubuntu:latest
LABEL authors="funnydevelopment"

# Используйте базовый образ Python
FROM python:3.8

# Создайте и перейдите в рабочую директорию /app
WORKDIR /app

# Копируйте зависимости и код приложения в рабочую директорию
COPY requirements.txt .
COPY core/ ./core/

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запустите ваше приложение
CMD ["python", "app.py"]
