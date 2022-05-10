from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://www.naver.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
item = 1

results = soup.findAll("li", "nav_item")

# r:read(읽기전용)  w:write(덮어쓰기전용)  a:append(추가전용)
search_item_file = open("itemresult.txt", "a", encoding ="UTF-8")

print(datetime.today().strftime("%Y년 %m월 %d일의 네이버 아이템입니다."))

for result in results:
    search_item_file.write(str(item)+"번: "+result.get_text()+"\n")
    print(item, "번 : ", result.get_text(), "\n")
    item += 1