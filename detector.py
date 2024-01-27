import speech_recognition as sr
import pygame
import threading
import pyttsx3

r = sr.Recognizer()

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def play_voice(text):
    engine = pyttsx3.init()
    newVoiceRate = 160
    engine.setProperty('rate',newVoiceRate)
    engine.setProperty('voice', "com.apple.speech.synthesis.voice.Fred")
    engine.say(text)
    engine.runAndWait()

def greet():
    print("Hello there! How can I assist you?")

def farewell():
    print("Goodbye! Have a great day!")
    exit()
    
def failure():
    print("Playing failure tone...")
    threading.Thread(target=play_mp3, args=("failed.mp3",)).start()
    
def scary():
    print("Playing scary music...")
    threading.Thread(target=play_mp3, args=("scary.mp3",)).start()

def mansplain():
    print("Mansplaining...")
    threading.Thread(target=play_voice, args=("Actually",)).start()
    
keywords_to_functions = {
    "hello": greet,
    "goodbye": farewell,
    "failed": failure,
    "scary": scary,
    "gloomy": scary,
    "dark": scary,
    "barbie": mansplain,
    
}

# Function to listen to the microphone and trigger functions
def listen_and_trigger():
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Processing...")
            text = r.recognize_google(audio).lower()
            print("You said:", text)
            for keyword, function in keywords_to_functions.items():
                if keyword in text:
                    function()
                    break

        except sr.UnknownValueError:
            print("Unable to recognize speech.")
        except sr.RequestError as e:
            print("Error occurred:", str(e))

listen_and_trigger()
