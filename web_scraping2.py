# GOAL: Get title of every book with a 2 star rating

import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
page_num = 12
base_url.format(page_num)

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text,'lxml')

soup.select('.product_pod')




