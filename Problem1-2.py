import pandas as pd
import requests

## 날짜를 먼저 만들어준다. -> 시간 데이터 만들기
date = pd.date_range('20180101', '20181231')
date

Time = []
for time in date:    
    Time.append(date.strftime("%Y%m%d").tolist())
    
time_list=Time[0] ##12번 반복됨을 알아서 그중에서 하나만 사용

data = []
key = 'a8e597633acca03091ad5fba598b58a7'
url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=" + key + "&targetDt="
df_default = pd.DataFrame()
for k in range(len(time_list)):
    requestData2 = requests.get(url+str(time_list[k])+'')
    data_2 = requestData2.json()
    data = data_2['boxOfficeResult']['dailyBoxOfficeList']
    df = pd.DataFrame.from_dict(data)
    df_default = df_default.append(df)
    
    df_default.to_csv('data_result.csv',encoding='utf-8', index = False) ## 한글이 포함되어 있으므로, encoding에 utf-8을 넣는다.-> 파일을 저장한다.
    
    pd.read_csv('data_result.csv')