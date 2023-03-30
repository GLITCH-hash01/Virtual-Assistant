import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import googlesearch as gs
import webbrowser
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
             if 'Alexa' in command:
                command = command.replace('Alexa','')    
                print(command) 
     except:
         pass
     return command
     
def run_alexa():
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
    else:
        talk('please say the command again.')    
          
    '''elif "location" in command:
        loc = location.Location()
        loc.valid_fix
        locpo=loc.position
        print(loc.reverse(locpo))'''
        
        
        
while True:           
    run_alexa()

    #.