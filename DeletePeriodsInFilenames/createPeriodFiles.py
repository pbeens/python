# imports
import os
import random
import string
from pathlib import Path

# global variables
num_files = 10  # used when creating files

# create files folder
dir_name = './files'
if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' created")
else:
    print(f"Directory '{dir_name}' already exists -- not created")

# create files
num_chars = 10
num_periods = 4
for i in range(num_files):
    filename = ''
    # random characters
    for j in range(num_chars):
        filename += random.choice(string.ascii_letters)
    # insert random periods
    for j in range(num_periods):
        location = random.randint(1, len(filename) - 1) # -1 to ensure period isn't at the end
        filename = filename[:location] + '.' + filename[location:]
    # append filename extension
    filename += '.pdf'
    # warm fuzzy
    print(filename)
    # create the file
    file_path = Path(dir_name + '/' + filename)
    open(file_path, 'w').close()  # this immediately closes the open file!
