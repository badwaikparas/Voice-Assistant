# import requests
# import json
#
#
# def jokes(url):
#     data = requests.get(url)
#     tt = json.loads(data.text)
#     return tt
#
# url = "https://official-joke-api.appspot.com/random_ten"
# # a = jokes(url)
#
# # for i in a:
# #     print(i["type"])
# #     print(i["setup"])
# #     print(i["punchline"], "\n")


import requests

url = "https://official-joke-api.appspot.com/random_ten"
json_data = requests.get(url).json()

jokes = []

for i in range(3):
    # jokes.append([])
    # jokes[i][0].append(json_data[i]["setup"])
    # jokes[i][1].append(json_data[i]["punchline"])
    joke = [json_data[i]["setup"], json_data[i]["punchline"]]
    jokes.append(joke)  # Add the joke list to the main jokes list

def joke():
    return jokes

# print(jokes)