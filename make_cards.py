import argparse
from PyDictionary import PyDictionary
import csv

class Anki(object):

    def __init__(self,  vocab_file, output_file):
        self.vocab_file = vocab_file
        self.output_file = output_file

    def read_vocab_file(self):
        vocab_list = [word.rstrip() for word in  open(self.vocab_file).readlines()]
        return vocab_list

    def define_vocab(self,vocab_list):
        dictionary = PyDictionary()
        defs_list = list()
        for word in vocab_list:
            defs_list.append(dictionary.meaning(word))
        return  defs_list

    def make_deck(self,vocab_list,defs_list):
        with open(self.output_file,"w") as csvfile:
            writer = csv.writer(csvfile, delimiter='\t')
            for word, definition in zip(vocab_list,defs_list):
                writer.writerow([word, definition])

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='This script makes anki flash cards from a text file of vocab words.')
    parser.add_argument('vocab_file', metavar='vocab_file', action="store", help='txt file full of vocab words')
    parser.add_argument('-o', '--output_file', metavar='output_file', default='anki_gre_vocab.txt', action="store", help='output anki deck txt file')
    args = parser.parse_args()

    anki = Anki(args.vocab_file, args.output_file)
    vocab_list = anki.read_vocab_file()
    defs_list = anki.define_vocab(vocab_list)
    anki_deck = anki.make_deck(vocab_list,defs_list)
