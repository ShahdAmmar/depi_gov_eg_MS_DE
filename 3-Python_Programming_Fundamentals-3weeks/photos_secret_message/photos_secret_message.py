""" This script converts a user-provided message into a series of image files based on the characters in the message."""
import os
import shutil
import string

# Create a dictionary that contains alphabet and the associated file names
alphabet_fl = dict()
alphabet = string.ascii_uppercase
for i in range(26):
    alphabet_fl[alphabet[i]] = str(i + 1) + '.jpg'
alphabet_fl['.'] = '27.jpg'
alphabet_fl[' '] = '28.jpg'

# Ask the user to input a message
message = input('Enter a message that contains English alphabet, dots, and spaces: ').upper()

script_directory = os.path.dirname(os.path.abspath(__file__))
source_directory = script_directory + '/Alphabet/'
target_directory = script_directory + '/MESSAGE/'
# Create the MESSAGE directory if it doesn't exist 
if not os.path.exists(target_directory):
    os.mkdir(script_directory+'/MESSAGE')
# Delete any old images if the directory exists
else:
    for fl in os.listdir(target_directory):
        fl_path = target_directory + fl
        os.remove(fl_path)

# Add the images of the message characters to the MESSAGE directory 
cnt = 0
for c in message:
    if c in alphabet_fl:
        cnt += 1
        source_path = source_directory + alphabet_fl[c]
        target_path = target_directory + f'{cnt}.jpg'
        shutil.copyfile(source_path, target_path)
    else:
        raise Exception(f'{c} is not a valid character. Use only English alphabet, dots, and spaces.')
