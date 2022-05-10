import requests
import pandas as pd
from bs4 import BeautifulSoup
import bs4
import json

key = 'a8e597633acca03091ad5fba598b58a7'
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=" + key
parameter = {"directorNm": "봉준호"}
req = requests.get(url, parameter)
#공공데이터에 등록된 xml파일에 접
html= req.json()
html
DF = pd.DataFrame(html['movieListResult']["movieList"])
## 연도로 다시 정렬
DF = DF.sort_values("prdtYear")

## 컬럼 형식 바꾸기
DF['directors'] = DF['directors'].apply(lambda x : x[0]['peopleNm'])
DF['companys'] = DF['companys'].apply(lambda x : x[0]['companyNm'] if x else x)

print(DF)