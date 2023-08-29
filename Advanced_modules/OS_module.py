# Mainly used for opening, closing, moving, etc.
print("Writing text to a simple text file")
f = open('practice.txt','w+')
f.write('This is a test string')
f.close()

import os
print("\nImported OS module")

print("\nCurrent Working directory is: {}".format(os.getcwd()))
print("\nList Current Working directory: {}".format(os.listdir()))
print("\nList Home directory: {}".format(os.listdir('/home/megame')))
print("\nList Python-Udemy directory: {}".format(os.listdir('/home/megame/Python-Udemy-New/Python-Udemy')))

import shutil
print("\nImported shutil module, used for moving files")

# Creating a move.txt file
f = open('move.txt', 'w+')
f.write('File that travels across directories via python airlines')
f.close()

# Deleting the existing file in practice directory
os.unlink('/home/megame/Python-Udemy-New/Python-Udemy/Advanced_modules/practice/move.txt')

# Moving the move.txt from current dir to practice dir
shutil.move('move.txt', '/home/megame/Python-Udemy-New/Python-Udemy/Advanced_modules/practice')

# Seeing if move.txt has moved to specified dir i.e., practice dir
print("\nSeeing the move.txt directory: {}".format(os.listdir('/home/megame/Python-Udemy-New/Python-Udemy/Advanced_modules/practice')))

# Deleting see jupyter notebook

# import send2trash # Mainly used as deleted files go to trash
# print("\nImported send2trash module")

print("\nLooking into a directory tree specified in the file_path")
file_path = '/home/megame/Python-Udemy-New/Python-Udemy/Advanced_modules/Example_Top_Level'
for folder, sub_folders, files in os.walk(file_path):

    print("Currently looking at {}".format(folder))
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print("\tSubfolder : {}".format(sub_fold))

    print('\n')
    print("the files are: ")
    for f in files:
        print("\tFile: {}".format(f))
    print('\n')




