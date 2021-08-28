import requests
import bs4

result = requests.get("http://www.example.com")

print(type(result))

print(result.text) # Prints entire html page

soup = bs4.BeautifulSoup(result.text, 'lxml') # Organizes the string to look exactly like it does on the webpage

print('-----------------------------------------------------------------------------------')
print(soup)
print('-----------------------------------------------------------------------------------')
print('\n')

print(soup.select('title')) # Put in the HTML element you want to select in the string

print(soup.select('title')[0].getText()) # Prints the string