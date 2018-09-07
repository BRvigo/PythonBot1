from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import requests
from click.decorators import command
from click.core import Command
import pyttsx3

def talkToMe(audio):
    "speaks audio passed as argument"    
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')
        
def myCommand():
    "listens for commands"
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();
        
    return command

def assistant(command):
    "If statements for executing commands"
    
    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
            
    elif 'open netflix' in command:
        reg_ex = re.search('open netflix (.*)', command)
        url = 'https://www.netflix.com/es/'
        webbrowser.open(url)
        print('Done!')
        
    elif 'close netflix' in command:
        reg_ex = requests.delete('close netflix (.*)', command)
        url = 'https://www.netflix.com/es/'
        webbrowser.open(url)
        print('Done!')
    
    else:
        pass
    
    
        
talkToMe('I am ready for your command')

while True:
    assistant(myCommand())
