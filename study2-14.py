import imp
from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://www.naver.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
item = 1

results = soup.findAll("li", "nav_item")

print(datetime.today().strftime("%Y년 %m월 %d일의 네이버 아이템입니다."))

for result in results:
    print(item, "번 : ", result.get_text(), "\n")
    item += 1