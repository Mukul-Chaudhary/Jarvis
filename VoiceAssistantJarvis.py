import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import random
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening")  

    speak("Hii Sir")
    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'data structure' in query:
            webbrowser.open("https://sites.google.com/site/academicshaili/ppts/data-structure")    

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open visual studio code' in query:
            codePath = "C:\\Users\\MUKUL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open zoom' in query:
            os.startfile("C:\\Users\\MUKUL\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")

        elif 'open wps' in query:
            os.startfile("C:\\Users\\MUKUL\\AppData\\Local\\Kingsoft\\WPS Office\\ksolaunch.exe")      

        elif 'open thonny' in query:
            os.startfile("C:\\Users\\MUKUL\\AppData\\Local\\Programs\\Thonny\\thonny.exe")

        elif 'play music' in query:
            n = random.randint(0,3)
            music_dir = "C:\\Users\\Default\\Music"
            songs = os.listdir(music_dir)
            print(songs)  
            os.startfile(os.path.join(music_dir, songs[n])) 

        elif 'quit' in query:
            exit()    
