# imports
import os

# global variables
replace_with_spaces = False
dir_name = './files'

if not os.path.exists(dir_name):
    os.makedirs(dir_name)
    print(f"Directory '{dir_name}' does not exist")
else:
    # get list of files
    files_list = os.listdir(dir_name)
    # delete spaces or optionally replace with spaces
    for i in range(len(files_list)):
        previous_filename = files_list[i]
        if replace_with_spaces:
            new_filename = files_list[i][:-4].replace('.', ' ') + files_list[i][-4:]
        else:
            new_filename = files_list[i][:-4].replace('.', '') + files_list[i][-4:]
        print(f"{previous_filename} {new_filename}")
