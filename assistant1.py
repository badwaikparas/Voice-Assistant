import pyttsx3 as p
# speech to text
import speech_recognition as sr

from selenium_web import inflow

# gets the info of driver being used
engine = p.init()

# adjust speed of voice
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 130)

# voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text1):
    engine.say(text1)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        # increases the spectrum of voice capturing
        r.energy_threshold = 10000
        # removes the ambient noises
        r.adjust_for_ambient_noise(source,1.2)


        print("listening")
        audio = r.listen(source)
        text  = r.recognize_google(audio)
        print(text)
        return text

# help us to retrieve information from a source that is microphone
r = sr.Recognizer()


while(1):
    # with sr.Microphone() as source:
    #     # increases the spectrum of voice capturing
    #     r.energy_threshold = 10000
    #     # removes the ambient noises
    #     r.adjust_for_ambient_noise(source,1.2)
    #
    #
    #     print("listening")
    #     audio = r.listen(source)
    #     text  = r.recognize_google(audio)
    #     print(text)

    text = listen()

    if "what" and "about" and "you" in text:
        speak("I am having a goodday sir")
    speak("what can i do for you")
    if "information" in text:
        speak("you need information related to which topic : ")
        assist = inflow()
        assist.get_info(listen())
    if "exit" in text:
        break

