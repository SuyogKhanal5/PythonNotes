f = open('practice.txt', 'w')
f.write('This is a test string')
f.close()

import os

print(os.getcwd()) # Shows location of the current working directory (location of script)

print(os.listdir()) # Lists every file in the folder

# You can pass a location into the parameter to see all of the files in a folder
print(os.listdir('C:\\Users\\suyog')) # Two backslashes are neccessary because the computer thinks its an escape sequence

import shutil

source = 'practice.txt'
destination = 'C:\\Users\\suyog'

shutil.move(source, destination)

# os.unlink(path) Deletes a file at the path you provide
# os.rmdir(path) Deletes a folder at the path you provide (only if the folder is empty)
# shutil.rmtree(path) Removes ALL files and folders in the path

# NONE OF THESE METHODS CAN BE REVERSED. IF YOU MAKE A MISTAKE YOU CANNOT RECOVER THE FILE

# Use the send2trash module

import send2trash

shutil.move(destination, os.getcwd())

send2trash.send2trash('practice.txt')

for folder, sub_folders, files in os.walk(os.getcwd()):
    print("Currently looking at " + folder)
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print("Subfolder: " + sub_fold)
    
    print('\n')
    print('The files are: ')

    for f in files:
        print("File: " + f)
    print('\n')