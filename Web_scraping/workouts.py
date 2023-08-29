import requests
from bs4 import BeautifulSoup
 
url = 'https://crawler-test.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
 
# Extract any HTML tag
# print(soup)
print("\n")
print(soup.find('title'))
print("\n")

title = soup.find('title')
h1 = soup.find('h1')
links = soup.find_all('a', href=True)
 
# Print the outputs
print('Title: ', title)
print('h1: ', h1)
print('Example link: ', links[1]['href'])

print("\n")
print(soup.find(id="header"))

print("\n")
print(soup.find_all('div', {'class': 'panel-header'})[0])

# Find Elements by Class
boxes = soup.find_all('div', {'class': 'panel'})

# print(boxes)

box_names = []
for box in boxes:
    title = box.find('h3')
    box_names.append(title.text)
 
print("\n")
print(box_names)

print("\n")
print(soup.select('div .panel-header'))

# print("\n")
# print(soup.select('div', {'class': 'panel-header'}))

print("\n")
logo = soup.find('a', {'id': 'logo'})
print(logo.text)

import re

# Parse using regex
print("\n")
soup = BeautifulSoup(response.text, 'lxml')
print(re.findall(r'\d{3} \w{4} \w{6}', soup.text))

# print("\n")	
# print(soup.find_all('a', href=True))


from urllib.parse import urljoin

print("\n")
domain = 'https://crawler-test.com/'
menu = soup.find('div', {'id': 'header'})
# Find all links within the div
menu_links = menu.find_all('a', href=True)

# print(menu_links[:5])
# Print output
for link in menu_links:
    print(link['href'])
    print(urljoin(domain, link['href']) )

