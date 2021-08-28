# Get the title of every book with a two star rating

import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue.page-{}.html'

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text, 'lmxl')

print(len(soup.select(".product_pod")))