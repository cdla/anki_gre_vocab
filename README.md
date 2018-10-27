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

Of note: beautiful soup will prompt a user message asks to add a parser to use by passing the argument 'features="html.parser"'. Change this line within the utils.py of PyDictionary in order to have the python script work.

Recommended Usage: the docker version

## Usage

To use the docker container, run the docker_run.sh shell script.

Otherwise:

run the python script make_cards.py

```
python make_cards.py

This script makes anki flash cards from a text file of vocab words.

positional arguments:
  vocab_file            txt file full of vocab words

optional arguments:
  -h, --help            show this help message and exit
  -o output_file, --output_file output_file
                        output anki deck txt file
  -e error_file, --error_file error_file
                        error file for the words that there were no
                        definitions
  -m, --edit_mode       manually edit mode allows for the editing of an
                        existing deck file to manually edit definitions
```

## TODO:  
 - add synonyms and antonyms
 - add script to write a sentence when presented with a word and its definition
