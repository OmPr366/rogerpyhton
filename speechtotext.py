import speech_recognition as sr
import pyttsx3 as p
import webbrowser
import re
from gtts import gTTS
from web_automation import *
import datetime
import os
import time
import pyautogui

now = str(datetime.datetime.now())
print(now)

now = now.split()
print(now)

t = now[1].split(':')
hour = int(t[0])
min = int(t[1])
if hour < 12:
    r = sr.Recognizer()
    engine = p.init()
    engine.say("Good Morning!")
   # greetings = 'Good Morning!'
   # lang = 'en'
   # obj = gTTS(text=greetings,lang=lang,slow=True)
   # obj.save('greetings.mp3')
   # os.system('greetings.mp3')
   # time.sleep(2)
   # pyautogui.moveTo(1910, 10)
   # pyautogui.click()
elif hour > 12 and hour <+16:
    r = sr.Recognizer()
    engine = p.init()
    engine.say("Good Afternoon!")
   # lang = 'en'
   # obj = gTTS(text=greetings, lang=lang)
   # obj.save('greetings.mp3')
   # os.system('greetings.mp3')
   # time.sleep(1.6)
   # pyautogui.moveTo(1910, 10)
   # pyautogui.click()
elif hour > 16 and hour<21:
    r = sr.Recognizer()
    engine = p.init()
    engine.say("Good Afternoon!")
   # lang = 'en'
   # obj = gTTS(text=greetings, lang=lang, slow=True)
   # obj.save('greetings.mp3')
   # os.system('greetings.mp3')
   # time.sleep(1.6)
   # pyautogui.moveTo(1910, 10)
   # pyautogui.click()

r = sr.Recognizer()
engine = p.init()
engine.say("Hello! How are you doing?")
engine.runAndWait()
print("...Listening...")
with sr.Microphone() as source:
    text = r.listen(source)

    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)

    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")
    engine.say("What do you want me to do?")
    engine.runAndWait()
    # text1 = r.listen(source)

    try:
        r1 = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening..')
            engine.say('Listening')
            engine.runAndWait()
            audio = r1.listen(source)
            audio = r1.recognize_google(audio)
            if 'weather' in audio:
                print('..')
                words = audio.split(' ')
                w = f'https://weather.com'
                webbrowser.open(w)
                # print("The weather is good!")

            elif 'open' in audio:
                print('..')
                words = audio.split('open')
                print(words[-1])
                link = str(words[-1])
                link = re.sub(' ', '', link)
                engine.say('Opening')
                engine.say(link)
                engine.runAndWait()
                link = f'https://{link}.com'
                print(link)
                webbrowser.open(link)

            elif 'play songs on YouTube' in audio:
                url = 'https://www.youtube.com/results?search_query=play+songs'
                webbrowser.open(url)

            elif 'where is' in audio:
                print('..')
                words = audio.split('where is')
                print(words[-1])
                link = str(words[-1])
                link = re.sub(' ', '', link)
                engine.say('Locating')
                engine.say(link)
                engine.runAndWait()
                link = f'https://www.google.co.in/maps/place/{link}'
                print(link)
                webbrowser.open(link)


            else:
                print(audio)
                print('Sorry, I do not understand that!')
                engine.say('Sorry, I do not understand that!')
                engine.runAndWait()
                #     recognised_text1 = r.recognize_google(text1)
    #     print(recognised_text1)
    #     if recognised_text1 == "play music":
    #         music()
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as e:
        print("")