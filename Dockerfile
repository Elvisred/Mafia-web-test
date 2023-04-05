FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /code
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt /code/
RUN pip install -r requirements.txt
ADD Dockerfile-mysql /
COPY . .
ENTRYPOINT ["./entrypoint.sh"]
COPY . /code/
