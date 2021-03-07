import requests

url = "http://13.212.74.216:8081/machines/123"

response = requests.request("GET", url)

print(response.json)
