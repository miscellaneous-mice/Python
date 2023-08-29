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


