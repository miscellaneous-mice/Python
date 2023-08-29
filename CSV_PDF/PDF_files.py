import PyPDF2
# https://pypi.org/project/PyPDF2/

f = open('Working_Business_Proposal.pdf', 'rb') # Read Binary

pdf_reader = PyPDF2.PdfReader(f)

print(len(pdf_reader.pages))

page = pdf_reader.pages[0]
text = page.extract_text()
print(text)

f.close()

f = open('Working_Business_Proposal.pdf', 'rb')

pdf_reader = PyPDF2.PdfReader(f)

pdf_text = []

for num in range(len(pdf_reader.pages)):

    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())

print(pdf_text)

print(pdf_text[1])

f.close()


