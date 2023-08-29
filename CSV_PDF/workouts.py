text = 'h'
if isinstance(text, str):
    print("True")
else:
    print("False")

print(int('1'))
# print(int('a'))

text = 'My phone number is 435.543.6654@@ also my friends phone number is ##432-543-5533+_'

import re

for ph_no in re.finditer(r'\d{3}(\W|\w)\d{3}(\W|\w)\d{4}', text):
    print(ph_no.group())