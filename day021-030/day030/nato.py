# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
import sys
import os

data = pandas.read_csv(os.path.join(sys.path[0], "nato_phonetic_alphabet.csv"))
# TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
done = False
while not done:
    try:
        word = input("Enter a word: ").upper()
        for c in word:
            if not c.isalpha():
                raise ValueError
    except ValueError:
        print("Sorry, only letters in the alphabet please.")
    else:
        done = True

output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
