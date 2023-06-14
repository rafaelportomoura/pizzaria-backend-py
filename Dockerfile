FROM python:3.11.4-alpine3.18

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY manage.py ./
COPY admin ./
COPY pizzaria ./
CMD python manage.py migrate
