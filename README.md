# anki_gre_vocab

This repository contains a script make_cards.py that makes GRE vocabulary flash cards from a list.

## Dependencies:

To use the docker workflow
- Docker

or

To use the python script:
- beautifulsoup
- requests
- goslate
- PyDictionary

## Usage

To use the docker container, run the docker_run.sh shell script.

Otherwise:

run the python script make_cards.py

```
python make_cards.py

usage: make_cards.py [-h] [-o output_file] vocab_file

This script makes anki flash cards from a text file of vocab words.

positional arguments:
  vocab_file            txt file full of vocab words

optional arguments:
  -h, --help            show this help message and exit
  -o output_file, --output_file output_file
                        output anki deck txt file`
```

## TODO:  
 - add synonyms and antonyms
 - add script to write a sentence when presented with a word and its definition
