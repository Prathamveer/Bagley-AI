import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def takeCommand():
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening')
        
        r.pause_threshold = 0.7
        audio = r.listen(source)
        
        try:
            print("Recognizing")
            
            Query = r.recognize_google(audio)
            print("You said=", Query)
            
        except Exception as e:
            print(e)
            print("Sorry, I didn't understand. Can you rephrase it??")
            return "None"
        
        return Query
    
def speak(audio):
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[0].id)
    
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
        speak("The day is" + day_of_the_week)
        
def tellTime():
    
    time = str(datetime.datetime.now())
    
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is" + hour + "Hours and" + min + "Minutes")
    
def Hello():
    speak("Hello Mr. Hrithvik I am Bagley. Tell me how may i help you")
    
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
        
        elif "open whatsapp" in query:
            speak("Opening Whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
            continue
        
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
        
        elif "what is the day" in query:
            tellDay()
            continue
        
        elif "what is the time" in query:
            tellTime()
            continue
        
        elif "bye" in query:
            speak("Bye. see you later Mr. Hrithvik")
            exit()
            
        elif "thanks" in query:
            speak("My pleasure!")
            exit()
        
        elif "search wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia"," ")
            result = wikipedia.summary(query, sentences=4)
            speak(result)
            
        elif "introduce yourself" in query:
            speak("I am Bagley. Your Personalized Assistant")
            
if __name__ == '__main__':
	Take_query()