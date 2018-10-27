#!/bin/sh

docker build -t anki_gre_vocab -f dockerfile .
docker run -t anki_gre_vocab
