# a = [(1, 4), (4, 7)]

# for elements in a:
#     print(elements[0])
rank = 3
# rank = "v"

if type(rank) == 'int':
    print("int")

elif type(rank) == 'str':
    print("str")

# def sounds(animal):
#     print(animal.speak())

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("Animal is named {}".format(self.name))

#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class Tiger(Animal):
#     def speak(self):
#         return self.name+' says roar!'
    
# class Cat(Animal):
#     def speak(self):
#         return self.name+' says Meow!' 

# niko = Tiger('Niko')
# felix = Cat('Felix')

# print("\nprint method")
# sounds(niko)
# sounds(felix)

# class Line3d:
    
#     def __init__(self,coor1,coor2,coor3=(0, 0, 0)):
#         self.coor1 = coor1
#         self.coor2 = coor2
#         self.coor3 = coor3
    
#     def distance(self):
#         x1,y1,z1 = self.coor1
#         x2,y2,z2 = self.coor2
#         return ((x2-x1)**2 + (y2-y1)**2)**0.5

#     def height(self):
#         x1,y1,z1 = self.coor1
#         x2,y2,z2 = self.coor2
#         return abs(z1- z2)
    
#     def slope(self):
#         self.run = self.distance()
#         self.rise = self.height()
#         return (self.rise)/(self.run)

# c1 = (1, 1, 0)
# c2 = (4, 5, 6)
# line = Line3d(c1, c2)
# print(line.distance())
# print(line.slope())
# print(f'rise is {line.rise} and run is {line.run}')

#Below example shows not to use variable names and functions as same name
# class sample:

#     def __init__(self, text):
#         self.text = text

#     def text(self):
#         print(f'Fucntion printing {self.text}')

#     def __del__(self):
#         print("content deleted")

# try:
#     s = sample("Hello")
#     print(s.text)
#     s.text()
# except TypeError:
#     # This will only check for an IOError exception and then execute this print statement
#     print("conflicting between variable and function name")
# except:
#     print("Error")
# else:
#     print("no error")
#     del s

# Looking for Error
# val = int(input("Please enter an integer: "))

# def hello_1(name='Pekka'):
#     print('The hello() function has been executed')

#     def greet_1():
#         print('\t This is the greet() function inside hello')

#         def welcome_1():
#             return '\t\t This is the welcome() function inside hello'

#         print(welcome_1())

#     greet_1()

# hello_1()

# print('\nTo make greet executable outside hello function\n')
# def hello(name='Pekka'):
#     print('The hello() function has been executed')

#     def greet():
#         return '\t This is the greet() function inside hello'

#     def welcome():
#         return '\t This is the welcome() function inside hello'

#     print("I am going to return a function!!")
#     if name == 'Pekka':
#         return greet()
#     else:
#         return welcome()

# print(hello('Pekka'))

# print('\nSimple generator')
# def simple_gen():
#     for x in range(3):
#         yield x

# for number in simple_gen():
#     print(number)

# g = simple_gen()
# print(g) # gives the info about the generator
# print("Casting as list {}".format(list(g)))

# print("\n")
# string_pattern = re.compile(r'\w{9} \w{6}')
# words = re.search(string_pattern, text)
# print("Grouped text is {}".format(words.group()))

# try:
#     print("First word is {}".format(words.group(1)))
# except:
#     print("Can't get individual grouped objects")
# else:
#     print("Sucessful in printing grouped objects")

import requests
from bs4 import BeautifulSoup
import csv
import re

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get('http://books.toscrape.com/')
soup = BeautifulSoup(res.text, "lxml")

page_no = re.findall(r'\d{2}', soup.select('.current')[0].text)
page_no = int(page_no[0])

file_to_output = open('Web_scraping_sample.csv', mode='w', newline='') 
csv_writer = csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['Sl no.', 'Title', 'Stock', 'Rating', 'Price']) # We can see delimiter is ,

file_to_output.close()

f = open('Web_scraping_sample.csv', mode='a',newline='') # Mode a is append to the csv file, not overwrite
csv_writer = csv.writer(f)

# titles = []
# # print(base_url.format(page_no))
sl_no = 0
for i in range(1, page_no+1):
    res = requests.get(base_url.format(i))
    soup = BeautifulSoup(res.text, "lxml")

    book = soup.select(".product_pod")

    for example in book:   

        sl_no += 1

        title = example.select("a")[1]['title']

        price = example.select(".price_color")[0].text[1:]

        stock = example.select(".instock.availability")[0].text
        stock = re.findall(r'[^\s]+', stock)
        stock_state = ' '.join(stock)

        rating = example.select("p")[0]["class"]
        rating = ' '.join(rating)

        csv_writer.writerow([sl_no, title, stock_state, rating, price]) # We can see delimiter is ,

f.close()


