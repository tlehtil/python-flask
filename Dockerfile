FROM python:alpine

WORKDIR /usr/src/app

COPY microblog/requirements.txt ./

RUN apk update && apk add tk
RUN pip install --no-cache-dir -r requirements.txt

COPY microblog/*.py ./
COPY microblog/app ./app
#COPY microblog/migrations ./migrations

ENV FLASK_APP microblog.py
RUN flask db init
RUN flask db upgrade
RUN flask db migrate
EXPOSE 5000
CMD flask run
