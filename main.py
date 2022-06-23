from email import message
from time import sleep
from unittest import result
import pyperclip
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from datetime import date
import smtplib
import pywhatkit
import wolframalpha
import requests

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
print(voices[1].id)


def wishMe(name):
    ''' wishes the user and ask them for a command'''
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<10):
        speak(f"Good morning {name}")
    elif(hour>=12 and hour<18):
        speak(f"Good afternoon {name}")
    else:
        speak(f"Good evening {name}")

    speak("Hello sir, I am MARTHA, your personal desktop assistant. Tell me how can I help you?")

def takeCommand():
    '''takes a microphone input from the user and returns the output as a string'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio= r.listen(source)

    try:
        print("Recognizing......")
        query=r.recognize_google(audio)
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def youtubeSearch(term):
    result="https://www.youtube.com/results?search_query="+term
    webbrowser.open(result)
    speak("Sir, this is what I found for you.....")
    print("Sir, this is what I found for you.......")

def googleSearch(term):
    result="https://www.google.com/search?q="+term
    webbrowser.open(result)
    speak("Sir, this is what I found for you.....")
    print("Sir, this is what I found for you.......")

def wolfRam(query):
    api_key = "LKALE4-6ET77PKQ8U"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)
    
    try:
        answer = next(requested.results).text
        return answer

    except:
        speak("I'm sorry sir, I couldn't find the appropriate data.....")

def Temp(query):
    term = str(query)
    if 'outside' in query:
        var1 = "Temparature in Serampore"
        answer = wolfRam(var1)
        print(f"The temperature outside is {answer}")
        speak(f"Sir, the temparature outside is {answer}")
        
    else:
        var2 = query
        answer = wolfRam(var2)
        print(f"{var2} is {answer}")
        speak(f"{var2} is {answer}")       
        

def calculator(query):
    term = str(query)
    term = term.replace("martha", "")
    term = term.replace("plus", "+")
    term = term.replace("into", "*")
    term = term.replace("minus", "-")
    term = term.replace("by", "/")
    

    final = str(term)

    try:
        result = wolfRam(final)
        print(f"The result is {result}")
        speak(f"The result is {result}")
        
    except:
        speak("Sorry sir, I am unable to calculate")


if __name__== "__main__":
    name=input("Enter your name:")
    wishMe(name)
    while True:
        query= takeCommand().lower()

#logic for executing tasks based on the input query user is giving to the computer

        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query=query.replace("wikipedia","") 
            results= wikipedia.summary(query,sentences=2)
            print(f"According to wikipedia......\n {results}")
            speak(f"According to wikipedia.....\n {results}")

        elif 'temperature' in query:
            Temp(query)

        elif 'open youtube' in query:
            speak("Opening Youtube.....")
            webbrowser.open("www.youtube.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stackoverflow.....")
            print("Opening Stackoverflow.....")
            webbrowser.open("www.stackoverflow.com")

        elif 'open google' in query:
            speak("Opening Google.....")
            print("Opening Google.....")
            webbrowser.open("www.google.com")

        elif 'open amazon' in query:
            speak("Opening Amazon.....")
            webbrowser.open("www.amazon.in")

        elif 'open flipkart' in query:
            speak("Opening Flipkart.....")
            webbrowser.open("www.flipkart.com")

        elif 'open facebook' in query:
            speak("Opening Facebook.....")
            webbrowser.open("www.facebook.com")

        elif 'open github' in query:
            speak("Opening GitHub.....")
            webbrowser.open("www.github.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")  

        elif 'date' in query:
            strDate = date.today()
            print(strDate)
            speak(f"Sir, today's date is {strDate}")  

        elif 'word' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Word 2007.lnk"
            os.startfile(codePath)  
        
        elif 'powerpoint' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Powerpoint 2007.lnk"
            os.startfile(codePath)  

        elif 'excel' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007.lnk"
            os.startfile(codePath) 
            
        
        elif 'code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

        elif 'youtube search' in query:
            Query=query.replace("youtube search","")
            youtubeSearch(Query)
            speak("This might help you sir....")
            

        elif 'google search' in query:
            Query=query.replace("google search","")
            googleSearch(Query)
            speak("This might help you sir......")

        elif 'speed test' in query:
            speak("Initialising speed test.....")
            webbrowser.open("https://www.speedtest.net/")
            speak("click on the button to initialize internet speed test.....")

        elif 'whatsapp message' in query:
            speak("who do you want to send a message?")
            name= takeCommand()
            speak("what should i say?")
            message = takeCommand()
            from automate import whatsapp
            whatsapp(name,message)

        elif 'call' in query:
            speak("who do you want to call?")
            name = takeCommand()
            print(name)
            print("Calling.....")
            speak("Calling.....")
            from automate import whatsappCall
            whatsappCall(name)

        elif 'connect video' in query:
            speak("Who do you want to connect with?")
            name = takeCommand()
            print(name)
            print("Connecting.....")
            speak("Connecting.....")
            from automate import whatsappVideoCall
            whatsappVideoCall(name)

        elif 'discord' in query:
            speak("Opening Discord.......")
            print("Opening Discord.......")
            codePath = "C:\\Users\\Pratim\\AppData\\Local\\Discord\\app-1.0.9005\\Discord.exe"
            os.startfile(codePath)

        elif 'download' in query:
            from downloader import download
            download()
            speak("I have downloaded the video for you sir. You can go and check....")

        elif 'calculate' in query:
            result = calculator(query)
            speak(result)
      
        elif 'exit' in query:
            print("Exiting......")
            speak("Spent a wonderful time with you. Call me again. Exiting")
            exit()   

         

        elif 'play music' or 'play songs' in query:
            music_dir = 'E:\\MUSIC'
            # num=random.randint(a,b) un comment when sure about playing a random song and not only the first song
            speak("Playing Music")
            print("Playing Music........")
            songs = os.listdir(music_dir)
            # last=songs[-1]
            # num = random.randint(0,songs.index(last))
            print(songs)
            # print(num)
            os.startfile(os.path.join(music_dir,songs[0]))

        else:
            speak("Sorry sir, I am unable to hear you. Please come again....")
            
