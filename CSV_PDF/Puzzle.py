import PyPDF2
import csv
import re
# import requests

data = open("Exercise_Files/find_the_link.csv")

csv_reader = csv.reader(data)

data_lines = list(csv_reader)

letters =''
# print(data_lines[0])

# Extract only word from list of string, with numbers also as string in list.
for alphabets in data_lines: 
    for word in alphabets:
        try:
            int(word)
        except ValueError:
            letters = letters + word
        else:
            pass

print(letters)

text = ''
for row_num, data in enumerate(data_lines):
    text = text + data[row_num]

print(text)

pdf_text = []

f = open("Exercise_Files/Find_the_Phone_Number.pdf", 'rb')
pdf_reader = PyPDF2.PdfReader(f)

for pages in pdf_reader.pages:
    pdf_text.append(pages.extract_text())

pdf_text = ' '.join(pdf_text)
# print(pdf_text)

for ph_no in re.finditer(r'\d{3}(\W|\w)\d{3}(\W|\w)\d{4}', pdf_text):
    print(ph_no.group())
f.close()


