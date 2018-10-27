FROM python:alpine3.7
MAINTAINER Carlo de los Angeles <carlo.delosangeles@gmail.com>

RUN apk update
RUN apk upgrade

RUN apk add git

RUN pip install PyDictionary

#fix for parser message
RUN sed -i "s/.text/.text,features=\"html.parser\"/g" /usr/local/lib/python3.7/site-packages/PyDictionary/utils.py


COPY . /app
WORKDIR /app

ENTRYPOINT ["python","make_cards.py"]
