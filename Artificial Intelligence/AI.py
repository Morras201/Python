from multiprocessing.connection import Listener
from tkinter.messagebox import QUESTION
import speech_recognition as sr
import pyttsx3
import pywhatkit
import subprocess
import datetime
import wikipedia
import pyjokes
import webbrowser 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
newVoiceRate = 136
engine.setProperty('rate',newVoiceRate)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)

    # Features

    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%p')
        talk('Current time is ' + time)
    
    if 'date' in command:
        talk('sorry, It sounds lovely but I am not interested')

    if 'open google' in command:
        talk('opening google')
        webbrowser.open('https://www.google.com/')

    if 'what are you' in command:
        talk(' I am a google assistant bot programmed by SX...for more information I can redirect you to wikipedia')
        webbrowser.open('https://en.wikipedia.org/wiki/Google_Assistant#:~:text=Google%20Assistant%20is%20a%20virtual,previous%20virtual%20assistant%2C%20Google%20Now.')
        info = 'Google Assistant is a virtual assistant software application developed by Google that is primarily available on mobile and home automation devices. Based on artificial intelligence, Google Assistant can engage in two-way conversations, unlike the companies previous virtual assistant. Users primarily interact with the Google Assistant through natural voice, though keyboard input is also supported. Assistant is able to answer questions, schedule events and alarms, adjust hardware settings on the users device, show information from the users Google account, play games, and more. Google has also announced that Assistant will be able to identify objects and gather visual information through the devices camera'
        talk(info)
        print(info)

    if 'wallpaper' in command:
        talk('I will recommend wallhaven for new wallapers')
        webbrowser.open('https://wallhaven.cc/')

    if 'are you single' in command:
        info = 'No, I am in a relationship with your motherboard'
        talk(info)
        print(info)

    if 'Who are you' in command:
        talk('My given name is google assistant, but you could call me Alexa')

    if 'typing' in command:
        talk('you can practice typing on monkeytype')
        webbrowser.open("https://monkeytype.com/")

    if 'weather' in command:
        talk(' I will show you the weather forecast for the whole week')
        webbrowser.open("https://www.google.com/search?q=weather+forecast&sxsrf=ALiCzsbKIwNXK7_kZ2V-ouAe37L5kYDmmg%3A1658226798815&ei=bojWYrKmMefO7_UPgMWqgAc&ved=0ahUKEwiylbOa4IT5AhVn57sIHYCiCnAQ4dUDCA4&uact=5&oq=weather+forecast&gs_lcp=Cgdnd3Mtd2l6EAMyDAgjECcQnQIQRhCAAjILCAAQgAQQsQMQyQMyBQgAEJIDMgUIABCSAzIFCAAQgAQyCAgAEIAEELEDMgUIABCABDIFCAAQgAQyCAgAEIAEELEDMgUIABCABDoHCAAQRxCwAzoKCAAQRxCwAxDJAzoHCAAQsAMQQ0oECEEYAEoECEYYAFChE1iSHGDzIGgBcAF4AIABtwKIAYYNkgEFMi01LjGYAQCgAQHIAQnAAQE&sclient=gws-wiz&dlnr=1&sei=kYjWYuSlHNWH9u8PsLe7uAY")

    if 'game' in command:
        QUESTION = input("What game would you like to play... Slavehack 2 or Hack The Box: ")
        if QUESTION == ("slavehack 2"):
            webbrowser.open("https://www.slavehack2.com/")
        elif QUESTION == ("hack the box"):
            webbrowser.open("https://www.hackthebox.com/")

    if 'joke' in command:
        talk(pyjokes.get_joke())
        engine.runAndWait()

    if 'pc specs' in command:
        info = "Intel Celeron CPU N3350 with 4 gigabytes of ram of which 3,87 gigabytes is usable"
        talk(info)
        print(info)

# Quotes

    if "happy" in command:
        QUESTION = input("Choose a number between 1 and 3 for a quote: ")
        if QUESTION == ("1"):
            info = "The greatest glory in living lies not in never falling, but in rising every time we fall"
            talk(info)
            print(info)
        if QUESTION == ("2"):
            info = "Happiness is a direction, not a place"
            talk(info)
            print(info)
        if QUESTION == ("3"):
            info = "You will face many defeats in life, but never let yourself be defeated"
            talk(info)
            print(info)

    if "sad" in command:
        QUESTION = input("Choose a number between 1 and 2 for a quote: ")
        if QUESTION == ("1"):
            info = "Our sweetest songs are those that tell of saddest thought"
            talk(info)
            print(info)
        if QUESTION == ("2"):
            info = "Sadness is also a way of defence"
            talk(info)
            print(info)

while True:
    run_alexa()
