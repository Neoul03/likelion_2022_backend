from bs4 import BeautifulSoup
import requests
from datetime import datetime

url = "https://datalab.naver.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

file = open("naverdatalab.html","w", encoding = 'UTF-8')
file.write(response.text)
file.close()

results = soup.findAll('ul','rank_list')

search_rank_file = open("rankresult.txt","w", encoding = 'UTF-8')

for result in results:
    search_rank_file.write(str(rank)+"번:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1
    