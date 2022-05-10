from bs4 import BeautifulSoup
import requests

url = "https://www.naver.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# html 문서에서 모든 li 태그를 가져오는 코드

result = soup.findAll("li", "nav_item")