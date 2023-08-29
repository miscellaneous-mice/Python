import requests

print("Grabbing a Page Title")

res = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
print(type(res))

# print(res.text) # Contents of website is displayed

import bs4

'''
Beautiful soup goes through
- Which is a CSS tag
- What is a CSS id
- Which are different html elements
- etc.
'''
soup = bs4.BeautifulSoup(res.text, "lxml") # lxml decyphers res.text

print("\nUsing soup\n{}".format(soup)) # We create soup objects

# Using this soup object we basically select elements off this object
print("\nSelecting html elements {}".format(soup.select('TITLE')))
print("\nSelecting html elements {}".format(soup.select('TITLE')[0].getText()))

print("\n")
print("\nSelecting html elements {}".format(soup.select('p')))
print("\nSelecting html elements {}".format(soup.select('p')[0].getText()))

print("\n")
print("\nSelecting html elements {}".format(soup.select('link')))
print("\nSelecting html elements {}".format(soup.select('link')[0]['href']))

print("\n")
print("\nSelecting html elements {}".format(soup.select('iframe')))
print("\nSelecting html elements {}".format(soup.select('iframe')[0]['src']))

# 00-Guide-to-Web-Scraping.ipynb after code cell 14 See syntaxes

