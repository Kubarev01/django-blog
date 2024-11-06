# Используем официальный образ Python
FROM python:3.12.4-alpine3.19



ENV PYTHONDONTWRITBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip


# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

# Выполняем миграции, загружаем данные и запускаем сервер
CMD ["bash", "-c", "python manage.py migrate && python manage.py loaddata fixtures/users/users.json && python manage.py loaddata fixtures/comments/comment.json &&&& python manage.py loaddata fixtures/posts/posts.json && python manage.py runserver 0.0.0.0:8000"]



