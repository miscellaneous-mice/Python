import requests
from bs4 import BeautifulSoup

res = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(res.text, "lxml")

# # print(soup.select('.thumbnail'))

i = 0
for image in soup.select('.thumbnail'):
    i = i+1
    image_link = "http://books.toscrape.com/"+image['src']
    image_format = image['src'][-5:]
    image_format = image_format.split('.')[1]
    org_image = requests.get(image_link)
    f = open("book_images/image"+str(i)+"."+image_format, 'wb')
    f.write(org_image.content)
    f.close()


import re

page_no = re.findall(r'\d{2}', soup.select('.current')[0].text)

# print(page_no)
# http://books.toscrape.com/catalogue/page-2.html
# http://books.toscrape.com/

for j in range(2, int(page_no[0])+1):

    res = requests.get('http://books.toscrape.com/catalogue/page-'+str(j)
    +'.html')

    soup = BeautifulSoup(res.text, "lxml")
    for image in soup.select('.thumbnail'):
        i = i+1
        image_link = "http://books.toscrape.com/"+image['src']
        image_format = image['src'][-5:]
        image_format = image_format.split('.')[1]
        org_image = requests.get(image_link)
        f = open("book_images/image"+str(i)+"."+image_format, 'wb')
        f.write(org_image.content)
        f.close()
