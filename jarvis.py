import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init()          #for taking voice
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("Hello I am Jarvis. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak("Searching Results...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open music' in query:
            music_dir = "D:\\audio"
            songs = os.listdir(music_dir)
            index = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[index]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the time is {strtime}")

        elif 'open code' in query:
            # enter your vs code path in place of Path
            codePath = "Path"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "youremail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am not able to send this email.")

        elif 'quit' in query:
            exit()
