import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import sys

def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening...')
        
        r.pause_threshold = 0.7
        audio = r.listen(source)
        
        try:
            print("Recognizing")
            
            Query = r.recognize_google(audio,language='en-us')
            print("You said=", Query)
            
        except Exception as e:
            print(e)
            print("Sorry, I didn't understand. Can you rephrase it??")
            speak("Sorry, I didn't understand. can you rephrase it???")
            return "None"
        
        return Query
    
def speak(audio):
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[0].id)
    
    print('Bagley:' + audio)
    engine.say(audio)
    engine.runAndWait()
    
def tellDay():
    day = datetime.datetime.today().weekday() + 1
    
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 
                6: 'Saturday', 
                7: 'Sunday'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
        
def tellTime():
    
    time = str(datetime.datetime.now())
    
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is" + hour + "Hours and" + min + "Minutes")
    
def Hello():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
        
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
        
    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')
    
    speak("How can i help you today?")
    
def Take_query():
    Hello()
    
    while(True):
        
        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue
        
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
        
        elif "tell this man to stop talking" in query:
            speak("Hey you, stop Disturbing Mr. Hrithvik!!")
            continue
        
        elif "open my youtube channel" in query:
            speak("Opening your yt channel")
            webbrowser.open("https://www.youtube.com/channel/UCj-YgHAXSK2R62hMOytdMew")
            continue
        
        elif "open my discord server" in query:
            speak("Opening your discord server")
            webbrowser.open("https://discord.com/channels/832490246649151499/832490247098859563")
            continue
        
        elif "open whatsapp" in query:
            speak("Opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
            continue
        
        elif "open online computer language" in query:
            speak("Opening Replit")
            webbrowser.open("https://replit.com/~")
        
        elif "open gmail" in query:
            speak("Opening Google Mail ")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            continue
        
        elif "open studio" in query:
            speak("Opening Youtube Studio ")
            webbrowser.open("https://studio.youtube.com/channel/UCj-YgHAXSK2R62hMOytdMew?c=UCj-YgHAXSK2R62hMOytdMew")
            continue
        
        elif "open drive" in query:
            speak("Opening Google Drive ")
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
            continue
        
        elif "introduce yourself to eklavya" in query:
            speak("Hi Eklavya, I am Bagley a digital assistant made by Mr. Hrithvik Bhardwaj.")
            continue
        
        elif "eat my poop" in query:
            speak("I was about to say the same thing to you!")
            continue
        
        elif "eat poop" in query:
            speak("I was about to say the same thing to you!")
        
        elif "introduce yourself to google" in query:
            speak("Hey Google, I am Bagley")
            continue
        
        elif "play ltt videos" in query:
            speak("Playing Linus Tech Tips Videos On youtube ")
            webbrowser.open("https://www.youtube.com/watch?v=27DE26j5n8w&list=RDCMUCXuqSBlHAE6Xw-yeJA0Tunw")
            continue
        
        elif "open spotify developer" in query:
            speak("Opening Spotify Developers ")
            webbrowser.open("https://developer.spotify.com/dashboard/applications")
            continue
        
        elif "who made you" in query:
            speak("Technically i'm a character from Watch Dogs Legion, but i was brought to life by Mr. Hrithvik Bhardwaj. Thank you Mr. Hrithvik for bringing me to life. I owe you my life as debt.")
            continue
        
        elif "who are you" in query:
            speak("I am Bagley. Your Personalized Digital Assistant.")
        
        elif "what is the day" in query:
            tellDay()
            continue
        
        elif "who am i" in query:
            speak("you are a human")
            continue
        
        elif "what is the time" in query:
            tellTime()
            continue
        
        elif "how are you" in query:
            speak("I'm Good, Thanks for asking.  How can i help you with??")
            continue
        
        elif "bye" in query:
            speak("Bye. see you later")
            exit()
            
        elif "thank you" in query:
            speak("My pleasure!")
            exit()
        
        elif "thanks" in query:
            speak("My Pleasure!")
            exit()
        
        elif "stop" in query:
            speak("ok")
            speak("See you later!")
            exit()
        
        elif "thanks bags" in query:
            speak("Your Welcome!")
            speak("by the way i'll be here if you need me. ")
            exit()
        
        elif "search wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia"," ")
            result = wikipedia.summary(query, sentences=20)
            speak(result)
            
        elif "introduce yourself" in query:
            speak("I am Bagley. Your Personalized Assistant")
            
if __name__ == '__main__':
	Take_query()