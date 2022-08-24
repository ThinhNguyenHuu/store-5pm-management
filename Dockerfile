FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "--workers", "3", "--bind", "0:8000", "root.wsgi:application"]
