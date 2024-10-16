FROM python:3.11-slim

VOLUME staging_data
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .