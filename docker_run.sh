#!/bin/sh

docker build -q -t anki_gre_vocab -f dockerfile .
docker run -v ${PWD}:/app anki_gre_vocab -v vocab_file.txt
