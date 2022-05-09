FROM python:3.8-slim-buster

WORKDIR /app

ARG SYNCER_REMOTE_URL
ARG CRACKER_REMOTE_URL

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "python3", "./main.py"  ]