# Modules

import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import googlesearch
import webbrowser as web
import pyaudio
import time
import os
from selenium import webdriver

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[2].id)

# All Function

def speak(audio):
    engine = pyttsx3.init('sapi5')
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour <12):
        speak("good morning user")
    else:
        speak("good evening user")
    speak("I am SMC , how may i help you....")
def taskCommand():
    print("Recognizing......")
    r = sr.Recognizer()
    with sr.Microphone() as source2:
        r.adjust_for_ambient_noise(source2,duration=0.2)
        audio = r.listen(source2)
    try:
        query = r.recognize_google(audio)
        MyText = query.lower()
        print("User said:"+MyText)
    except Exception as e:
        speak("sorry! got glitched")
        speak("Please say that again")
        return "None"
    return(MyText)

# Main Code -

if __name__=="__main__":
    greet()
    while True:
        query = taskCommand()

    #Wikipedia

        if "wikipedia" in query:
            speak("connecting wikipedia....")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences = 2)
            speak("According to wikipedia..")
            print(results)
            speak(results)

    #Shutdown

        elif "shutdown" in query:
            speak("thanks for talking")
            quit()

    #Google

        elif "open" in query:
            speak("please wait")
#Method 1
        # query = query.replace("google" , "")
        # browser = webdriver.Chrome('chromedriver')
        # for i in range(1):
        #     browser.get("https://www.google.com/search?q=" +query + "&start=" + str(i))

#Method 2

            try:
                from googlesearch import search
            except ImportError:
                print("no mudule found:..")
            query = query.replace("google","")
            for i in search(query,tld="co.in",num=1 , stop=1, pause=2):
                a = print(i)

            os.startfile(i)

# Method 3
            # path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            # os.startfile(path).open("youtube.com")


