FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "--workers", "3", "--bind", "0:8000", "root.wsgi:application"]
