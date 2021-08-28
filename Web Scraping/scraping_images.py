import bs4
import requests

res = requests.get("https://en.wikipedia.org/wiki/Portal_(video_game)")

soup = bs4.BeautifulSoup(res.text, 'lxml')

portal_game = soup.select('.thumbinner')[2]

# print(portal_game['src'])

image_link = requests.get('https://upload.wikimedia.org/wikipedia/en/thumb/7/7e/Portalgame.jpg/220px-Portalgame.jpg')

f = open('portal_image.jpg', 'wb')
f.write(image_link.content)
f.close