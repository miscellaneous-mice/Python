import requests
from bs4 import BeautifulSoup

print("Printing the titles of books of rating 2 stars")

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(res.text, "lxml")

import re

page_no = re.findall(r'\d{2}', soup.select('.current')[0].text)
page_no = int(page_no[0])

example = soup.select(".product_pod")[0]

# One way of doing this
print(str(example))
print("\n")
print('star-rating Three' in str(example))


print("\nInside the book class")
print(example)
print("\nStar rating")
# Best way of doing this is
print(example.select(".star-rating.Three")) # "rating Three" = "rating.Three"
print("\nDefinition of book and a reference link")
print(example.select("a"))
print("\nOnly definition of book")
print(example.select("a")[1])
print("\nTitle")
print(example.select("a")[1]['title'])


'''
titles = []
# print(base_url.format(page_no))
for i in range(1, page_no+1):
    res = requests.get(base_url.format(i))
    soup = BeautifulSoup(res.text, "lxml")

    book = soup.select(".product_pod")

    for product in book:   

        if len(product.select('.star-rating.Two')) != 0:

            titles.append(product.select('a')[1]['title'])

        else:
            pass

print("Titles having > 2 stars are: ")
for title in titles:
    print(title)

'''