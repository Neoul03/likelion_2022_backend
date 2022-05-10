import requests
from bs4 import BeautifulSoup

url = "http://www.daum.net/"
response = requests.get(url)
print (type(response.text))

print (type(BeautifulSoup(response.text, 'html.parser')))