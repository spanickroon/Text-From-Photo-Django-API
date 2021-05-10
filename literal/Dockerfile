FROM python:3.9.2-slim-buster

RUN apt-get update; \
	apt-get install -y --no-install-recommends;

COPY requirements.txt /

RUN pip install --upgrade pip; \
    pip install -r /requirements.txt

COPY . /app
WORKDIR /app

EXPOSE 8000
