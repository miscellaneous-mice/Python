print('Gonna solva some stuff')

import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip','','zip')

# shutil.unpack_archive('unzip_me_for_instructions.zip','another','zip')

with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

# with open('another/Instructions.txt') as f:
#     content = f.read()
#     print(content)

import re
pattern = r'\d{3}-\d{3}-\d{4}'

test_string = 'here is a phone number 123-123-1234'

print(re.findall(pattern, test_string))

def search(file, pattern = r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)

    else:
        return ''

import os

results = []

for folder, sub_folders, files in os.walk(os.getcwd()+'/extracted_content'):

    for f in files:
        full_path = folder + '/' + f
        # print(full_path)
        results.append(search(full_path))

for r in results:
    if r!='':
        print(r.group())
