FROM python:alpine

WORKDIR /usr/src/app

COPY microblog/requirements.txt ./

RUN apk update && apk add tk
RUN pip install --no-cache-dir -r requirements.txt

CMD flask run
