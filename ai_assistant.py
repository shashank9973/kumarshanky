import kit as kit
import pyttsx3
import datetime

import query as query
import speech_recognition as sr
from numpy import source
from wikipedia import wikipedia
import webbrowser
import smtplib
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("subah ho gayi")
    elif hour >= 12 and hour < 18:
        speak("kitna sota hai dopahar ho gaya")
    else:
        speak("shaam ho gaya hai utho")

    speak("my name is ramu kaka. Shashank is my creator")


def takeCommand():
    """
    It takes microphone input from user and return string statement
    :return:
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("zor se bol na...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP ('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your_password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if _name_ == "_main_":
    wishme()
    while True:
        query = takeCommand().lower()

        # logic for task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            speak("what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'email' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "subrotokumar@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry email nahi gaya")
        elif "send message" in query:
            kit.sendwhatmsg("+917061517492","this is testing protocol",2,25)
