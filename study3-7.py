import requests
import json

city = "Seoul"
apikey = "35ec83f2af53b72e4059d1e8892cd03e"

api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)

print(type(result.text))
print(type(data))