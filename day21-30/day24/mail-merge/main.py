

# TODO: Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os
import sys

with open(os.path.join(sys.path[0], 'Input/Names/invited_names.txt')) as invited_names_file:
    invited_names = invited_names_file.readlines()
    for i in range(len(invited_names)):
        invited_names[i] = invited_names[i].strip()

with open(os.path.join(sys.path[0], 'Input/Letters/starting_letter.docx')) as starting_letter_file:
    starting_letter = starting_letter_file.read()
    for invited_name in invited_names:
        letter = starting_letter.replace("[name]", invited_name)
        with open(os.path.join(sys.path[0], f'Output/ReadyToSend/letter_for_{invited_name}.docx'), 'w') as letter_file:
            letter_file.write(letter)
