import requests
import bs4

# soup.select('div) ---> All elements with 'div' tag
# soup.select('#some_id') ---> Elements containing id 'some_id'
# soup.select('.some_class') ---> Elements containing class 'some_class'
# soup.select('div span') ---> Elements named span within a div element
# soup.select('div > span') ---> Elements named span directly within a div element, with nothing in between

res = requests.get("https://en.wikipedia.org/wiki/Portal_(video_game)")

soup = bs4.BeautifulSoup(res.text, 'lxml')

first_item = soup.select('.toctext')[0]

print(first_item.text)

for item in soup.select('.toctext'):
    print(item.text)