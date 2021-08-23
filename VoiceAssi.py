import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
#email_data= {"Saumya": "saumya.gupta.19cse@bmu.edu.in", "Shikhar": "socialshikhar@gmail.com"}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning")
    elif hour >=12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am Jarvis Ma'am. Please tell me how can i help you!")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening to you....!")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User Said: ", query)
    except Exception as e:
        # print(e)
        print("Please say that again")
        return "None"
    return query
password = open("accpasswprd.txt", "r")
data = password.read()
def sendEmail(to, content):
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('saumya.gupta.19cse@bmu.edu.in', password)
    server.sendmail('saumya.gupta.19cse@bmu.edu.in', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia..")
            query=query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open Youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open Google' in query:
            webbrowser.open("google.com")
        elif 'open Stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif'play music' in query:
            music_dir = 'C:\\Users\\saumya gupta\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
#random song utility to be used
        elif 'the time' in query:
            strTime=datetime.datetime.now().strTime("%H:%MP:%S")
            speak(f"Ma'am the time is :{strTime}")

        elif 'send email' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "saumya.gupta.19cse@bmu.edu.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! Saumya ma'am , i was not able to send email!")









