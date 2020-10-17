FROM python:3

WORKDIR /app

RUN pip install --no-cache-dir django-ninja mariadb;

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
