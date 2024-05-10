import datetime
from time import sleep

import pyttsx3 as p
# speech to text
import speech_recognition as sr
import re
from selenium_web import inflow
from yt_auto import music
from news_auto import *
import randfacts
# import joke_auto
from joke_auto import *
from weather_auto import *
import datetime

#date
today_date = datetime.datetime.now()

# gets the info of driver being used
engine = p.init()

# adjust speed of voice
rate = engine.getProperty('rate')
# print(rate)
engine.setProperty('rate', 130)

# voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text1):
    engine.say(text1)
    engine.runAndWait()

def remove_indices(text):
    return re.sub(r'\[\d+\]', '', text)

def wishme():
    hour = int(datetime.datetime.now().strftime('%H'))
    if 0 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


# help us to retrieve information from a source that is microphone
r = sr.Recognizer()

with sr.Microphone() as source:
    # increases the spectrum of voice capturing
    r.energy_threshold = 10000
    # removes the ambient noises
    r.adjust_for_ambient_noise(source,1.2)


    # print("listening")
    # audio = r.listen(source)
    # text  = r.recognize_google(audio)
    # print(text)
    #
    # if "what" and "about" and "you" in text:
    #     speak("I am having a goodday sir")
    # speak("what can i do for you")


# with sr.Microphone() as source:
#     # increases the spectrum of voice capturing
#     r.energy_threshold = 10000
#     # removes the ambient noises
#     r.adjust_for_ambient_noise(source,1.2)

    speak(f"{wishme()} Paras How may i assist you today?")
    print("listening")
    audio = r.listen(source)
    text2  = r.recognize_google(audio)
    print(text2)

    if "information" in text2:
            speak("you need information related to which topic : ")
            print("you need information related to which topic : ")
            # with sr.Microphone() as source:
            #     r.energy_threshold = 10000
            #     r.adjust_for_ambient_noise(source, 1.2)

            print("listening")
            audio = r.listen(source)
            info = r.recognize_google(audio)
            print(info)
            assist = inflow()
            speak("Searching {} in wikipidia".format(info))
            print("Searching {} in wikipidia".format(info))
            content = assist.get_info(info)
            speak(remove_indices(content))
    elif "play" and "video" in text2:
            speak("what do you want to play?")
            print("what do you want to play?")
            # with sr.Microphone() as source:
            #     r.energy_threshold = 10000
            #     r.adjust_for_ambient_noise(source, 1.2)

            print("listening")
            audio = r.listen(source)
            vid = r.recognize_google(audio)
            print(vid)
            print("Playing {} on Youtube".format(vid))
            speak("Playing {}".format(vid))
            assist = music()
            assist.play(vid)
    elif "news" in text2:
            arr = news()
            print("Today's Headlines are")
            speak("Today's Headlines are")
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])
    elif "fact" or "facts" in text2:
            speak("Sure, ")
            print("Sure, ")
            x = randfacts.get_fact()
            print("Did you know that, " + x)
            speak("Did you know that, " + x)
    elif "joke" or "jokes" in text2:
            speak("Sure,")
            print("Sure ,")
            jokes = joke()
            speak("Listen to this")
            print("Listen to this")
            for i in range(len(jokes)):
                print(jokes[i][0])
                speak(jokes[i][0])
                sleep(3)
                print(jokes[i][1])
                speak(jokes[i][1])
                sleep(1)
    elif "weather" in text2:
            print("The current temperature in {} is {} degrees Celsius. It's a bit {} outside.".format(json_data1["name"], temp(), des()))
            speak("The current temperature in {} is {} degrees Celsius. It's a bit {} outside.".format(json_data1["name"], temp(), des()))

    elif "date" and "today's" or "today":
    
            day = today_date.strftime('%d').lstrip("0").replace(" 0", " ")
            # speak("Today is {}".format(today_date.strftime("%d"),today_date.strftime("%B"),today_date.strftime("%I"),today_date.strftime("%M"),today_date.strftime("%p")))
            # speak(f"Today is {day} {today_date.strftime('%B')} {today_date.strftime('%I')}:{today_date.strftime('%M')} {today_date.strftime('%p')}")
            formatted_string = f"Today is {day} of {today_date.strftime('%B')} {today_date.strftime('%I')}:{today_date.strftime('%M')} {today_date.strftime('%p')}"
            print(formatted_string)
            speak(formatted_string)
    else:
        exit()
