FROM python:3.11.4-alpine3.18

WORKDIR /usr/src/app
RUN python -m venv env
RUN source env/bin/activate

COPY ./app/* ./

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
