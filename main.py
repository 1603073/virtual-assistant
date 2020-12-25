import pyttsx3
import datetime
import speech_recognition as sr 
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

#path
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
codepath = "C:/Users/WIN 10/AppData/Local/Programs/Microsoft VS Code/Code.exe"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning mam!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon mam!")   

    else:
        speak("Good Evening mam!")  

    speak("Hello mam i am Here to Help You!")       

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except:   
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'shutdown' in query:
            quit(speak ('Shutting Down.... Good Bye Mam'))

        elif 'open youtube' in query:
            try:
                speak("opening youtube")
                webbrowser.get(chrome_path).open("youtube.com")
            except:
                speak("opening youtube")
                webbrowser.open("youtube.com")

        elif 'open google' in query:
            try:
                speak("opening google")
                webbrowser.get(chrome_path).open("google.com")
            except:
                speak('opening Google')
                webbrowser.open("google.com")
        
        elif 'open mail' in query:
            try:
                speak("opening gmail")
                webbrowser.get(chrome_path).open("mail.google.com")
            except:
                speak('opening mail')
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")        

        elif 'open drive' in query:
            try:
                speak("opening google drive")
                webbrowser.get(chrome_path).open("drive.google.com")
            except:
                speak('opening google drive')
                webbrowser.open("https://drive.google.com/drive/u/0/my-drive")

        elif 'open chrome' in query:
            try:
                speak("opening chrome")
                webbrowser.get(chrome_path).open("chrome.com")
            except:
                speak('opening chrome')
                webbrowser.open("chrome.com")

        elif 'open stackoverflow' in query:
            try:
                speak("opening stackoverflow")
                webbrowser.get(chrome_path).open("stackoverflow.com")
            except:
                speak('opening stackoverflow')
                webbrowser.open("https://stackoverflow.com/") 

        elif 'open facebook' in query:
            try:
                speak("opening facebook")
                webbrowser.get(chrome_path).open("facebook.com")
            except:
                speak("opening facebook")
                webbrowser.open("facebook.com")

        elif 'open codeforces' in query:
            try:
                speak("opening codeforces")
                webbrowser.get(chrome_path).open("codeforces.com")
            except:
                speak("opening codeforces")
                webbrowser.open("https://codeforces.com/problemset")

        elif 'open twitter' in query:
            try:
                speak("opening twitter")
                webbrowser.get(chrome_path).open("twitter.com")
            except:
                speak("opening Twitter")
                webbrowser.open("twitter.com")

        elif 'open instagram' in query:
            try:
                speak("opening instagram")
                webbrowser.get(chrome_path).open("instagram.com")
            except:
                speak("opening instagram")
                webbrowser.open("instagram.com")        

        elif 'open github' in query:
            try:
                speak("Opening! please wait!")
                webbrowser.get(chrome_path).open("https://github.com/1603073")  
            except:
                speak("Opening github!")
                webbrowser.open("https://github.com/1603073")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")

        elif 'open vscode' in query:
            try:
                os.startfile(codepath)
            except:
                speak("please Install VScode First") 
                webbrowser.open("https://code.visualstudio.com/")   
