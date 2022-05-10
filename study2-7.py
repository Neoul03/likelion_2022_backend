import requests

url = "https://www.daum.net/"
response = requests.get(url)

#print(response.text) : http text를 받음

#print(response.url)

#print(response.content)

#print(response.encoding) : UTF-8

#print(response.headers) 

#print(response.json)

#print(response.links)

#print(response.ok)

#print(response.status_code)