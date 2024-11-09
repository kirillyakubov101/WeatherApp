import requests
from  ApiDatabase import getApiKey
import json

user_input = input("Enter City Name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={getApiKey()}&units=metric"
req = requests.get(url).json()
# print(req)
weather_obj = (req["name"],str(req["main"]["temp"]) + "°C")
print(weather_obj)