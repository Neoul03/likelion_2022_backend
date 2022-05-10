from http.client import ResponseNotReady
from bs4 import BeautifulSoup
import requests

url = "https://www.naver.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

file = open("naver.html","w", encoding = 'UTF-8')
file.write(response.text)
file.close()

print(soup.title)
print(soup.title.string)
print(soup.span)
print(soup.findAll('span'))