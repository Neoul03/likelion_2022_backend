import requests
from bs4 import BeautifulSoup

url = "http://www.daum.net/"
response = requests.get(url)
print(response.text[:500])

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title)
print(soup.title.string)
print(soup.span)
print(soup.findAll('span'))