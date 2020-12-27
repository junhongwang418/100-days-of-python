import pandas
import os
import sys

file = pandas.read_csv(os.path.join(sys.path[0], "nato_phonetic_alphabet.csv"))

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet = {
    row.letter: row.code for (index, row) in file.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
print([nato_phonetic_alphabet[c] for c in word])
