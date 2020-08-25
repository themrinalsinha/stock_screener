FROM python:3.6.12-slim-buster

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

