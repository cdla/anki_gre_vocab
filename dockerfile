FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install PyDictionary

CMD python make_cards.py
