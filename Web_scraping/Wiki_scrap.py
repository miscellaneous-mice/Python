import requests
from bs4 import BeautifulSoup

res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

soup = BeautifulSoup(res.text, "lxml")

print("\n")
print(soup.select('.vector-toc-text')[1])
print("\n")
print(soup.select('.reference')[0])
print("\n")
print(soup.select('.infobox-label')[0])
print("\n")
print(soup.select('.vector-toc-link')[1])
print("\n")

for item in soup.select('.vector-toc-text'):
    print(item.text)

print("\n\n")

for item in soup.select('.reference'):
    print(item.text)

print("\n\n")

for item in soup.select('.infobox-label'):
    print(item.text)

print("\n\n")

for item in soup.select('.vector-toc-link'):
    print(item.text)

