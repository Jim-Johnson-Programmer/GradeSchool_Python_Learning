import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=40&longitude=-88&hourly=temperature_2m"

response = requests.get(url)
weather = response.json()

for t, temp in zip(weather["hourly"]["time"], weather["hourly"]["temperature_2m"]):
    print(t, temp)
