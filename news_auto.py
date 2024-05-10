import requests
from keys import *

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + NEWS_API_KEY
json_data = requests.get(api_address).json()

ar = []

def news():
    for i in range(3):
        ar.append("Number "+ str(i+1) +" : "+ json_data["articles"][i]["title"]+".")

    return ar

# arr = news()

# print(arr)