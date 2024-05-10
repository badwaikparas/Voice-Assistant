import requests

import json
from keys import *

api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Nagpur&appid='+ OPEN_WEATHER_API_KEY
json_data1 = requests.get(api_address).json()

def temp():
    temperature  =round(json_data1["main"]["temp"]-273,1)
    return temperature

def des():
    description = json_data1["weather"][0]["description"]
    return description

# print(temp())
# print(des())