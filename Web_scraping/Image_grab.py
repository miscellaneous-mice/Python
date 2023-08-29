import requests
from bs4 import BeautifulSoup

res = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup = BeautifulSoup(res.text, "lxml")

image_all = soup.select('.mw-file-element')

image_some = soup.select('.mw-file-description')

image_main = soup.select('.mw-default-size')

print("\n")
print(image_all[1])
print("\n")
print(image_some[1])
print("\n")
print(image_main[1])

computer = soup.select('.mw-default-size')[0]
print("\nLevel 1")
print(computer.select('a')[0])
print("\nLevel 2")
print(computer.select('a')[0].select('img'))
print("\nLevel 3")
print(computer.select('a')[0].select('img')[0]['src']) # Same as below code
computer = computer.findChild().findChild()

# computer = soup.select('.mw-file-element')[1]
print("\n")
print('https:'+computer['src'])

image_format = computer['src'][-5:] # Grabbing the last 7 string
image_format = image_format.split('.')[1]

print(image_format)

image_link = requests.get('https:'+computer['src'])

# print(image_link.content) # Had info of image

f = open("computer_image."+image_format, 'wb') # Write binary mode
f.write(image_link.content)
f.close()

print("\nDownloading all the images from the wikipedia page")

i = 0
for image in soup.select('.mw-default-size'):
    i=i+1
    image = image.findChild().findChild()
    image_format = image['src'][-5:] # Grabbing the last 7 string
    image_format = image_format.split('.')[1]
    image_link = requests.get('https:'+image['src'])
    f = open("main_images/computer_image"+str(i)+"."+image_format, 'wb') # Write binary mode
    f.write(image_link.content)
    f.close()

i=0
for image in soup.select('.mw-file-element'):
    i=i+1
    image_format = image['src'][-5:] # Grabbing the last 7 string
    image_format = image_format.split('.')[1]
    image_link = requests.get('https:'+image['src'])
    f = open("all_images/all_computer_image"+str(i)+"."+image_format, 'wb') # Write binary mode
    f.write(image_link.content)
    f.close()
