import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

myVA = pyttsx3.init()
vaName = 'Lisa'

myVA.runAndWait()
listener = sr.Recognizer()
myVA = pyttsx3.init()
voices = myVA.getProperty('voices')

myVA.setProperty('voice', voices[1].id)
myVA.setProperty('rate', 180)

def talk(txt):
    myVA.say(txt)
    myVA.runAndWait()


talk('Hello! My name is Lisa!!! How can i help you?')

def talk_time():
    time = 'Okay! it\'s   ' + datetime.datetime.now().strftime('%I:%M %p')
    return time


def how_to(txt):
    if 'youtube' in txt:
        pywhatkit.playonyt(txt)
    elif 'google' in txt:
        talk(pywhatkit.info(txt, 2))
    else:
        talk('Where to search ? youtube or google?')
        cmd = take_command()
        if cmd is None:
            cmd = 'google'
        if 'google' in cmd:
            talk('Okay! searching on google')
            talk(pywhatkit.info(txt, 5))
        else:
            talk('okay! searching on youtube')
            pywhatkit.playonyt(txt)


def take_command():
    try:
        while True:
            with sr.Microphone() as source:
                print('listening...')
                voice = listener.listen(source, 5, 6)
                command = listener.recognize_google(voice).lower()
                print('command is', command)
                return command
    except:
        pass


def run_VA():
    command = take_command()
    if command is None:
        return
    if ('time' in command):
        talk(talk_time())
    elif 'how to' in command:
        how_to(command)
    elif 'play' in command:
        playing = command.replace('play', '')
        talk('Playing ' + playing + ' for you now!')
        pywhatkit.playonyt(playing)
    elif 'tell me about' in command:
        info = wikipedia.summary(command.replace('tell me about', ''), 2)
        talk(info)
    elif ('wh' in command):
        if 'what\'s your' in command or 'what is your' in command:
            talk('No personal questions please! Ha ha!')
        else:
            talk(wikipedia.summary(command, 2))
    elif 'are you' in command:
        talk('Not like you!! Hu hu!')
    elif 'joke' in command:
        talk(pyjokes.get_joke(category='all'))
    else:
        talk('sorry! either your English is weak, or my knowledge is too little to understand this!')


while True:
    run_VA()