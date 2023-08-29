import requests
from bs4 import BeautifulSoup

base_url = 'https://quotes.toscrape.com/page/{}/'
'''
res = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(res.text, "lxml")

print(soup.select(".author")[1].text)

print(soup.select(".next"))

print(soup.select(".text")[0])

res2 = requests.get('https://quotes.toscrape.com/page/100/')

soup2 = BeautifulSoup(res2.text, "lxml")

print(soup2.select(".next"))

print(soup2.select(".text"))
'''
# Check the notebook for checking no quotes found

i = 0

authors = []

while(True):
    i = i+1

    res = requests.get(base_url.format(i))
    soup = BeautifulSoup(res.text, "lxml")

    for author in soup.select(".author"):
        authors.append(author.text)

    if soup.select(".next") == []:
        break
    else:
        continue

print("No of pages is {}".format(i))
print(set(authors))






