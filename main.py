import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import googlesearch as gs
import webbrowser

from geopy.geocoders import Nominatim
from AppOpener import open, close


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.runAndWait()

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
             if 'Jarvis' in command:
                command = command.replace('Jarvis','')    
                print(command) 
     except:
         pass
     return command
     
def run_alexa(command):
    command  = take_command()
    print(command) 
    if 'play' in command:
        song = command.replace('play', '')    
        talk('playing' + song) 
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')  
        talk('The current time is' + time) 
        print(time) 
    elif 'who is' in command:
        person = command.replace('who is' , '') 
        info = wikipedia.summary(person, 1)
        print(info)  
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke()) 
    elif 'hello' in command:
        talk('Hi!')  
    elif 'how are you doing' in command:
        talk('i am doing good! Thanks for asking!')   
    elif 'bye' in command:
        quit()  
    elif "search" in command:
        command=command.replace("search","")
        result = gs.search(command, num_result=1)
        chrome = "c:\\program files (86)\\Google\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome))
        query = result.replace("open", "")
        webbrowser.get('chrome').open_new_tab(f"www.{query}.com")
    elif "open" in command:
        app_name = command.replace("open ","")
        open(app_name, match_closest=True)    
          
    elif "location" in command:
        loc = Nominatim(user_agent="GetLoc")

        # entering the location name
        getLoc = loc.geocode(command)
        print(getLoc.address)
        print("Latitude = ", getLoc.latitude, "\n")
        print("Longitude = ", getLoc.longitude)
    else:
        talk('please say the command again.')

        
        
        
        
while True:
    command=take_command()            
    run_alexa(command)
