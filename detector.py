import speech_recognition as sr
import pygame
import threading

r = sr.Recognizer()

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def greet():
    print("Hello there! How can I assist you?")

def farewell():
    print("Goodbye! Have a great day!")
    
def failure():
    print("I'm sorry to hear that. I hope you have a better day tomorrow.")
    threading.Thread(target=play_mp3, args=("failed.mp3",)).start()
    
keywords_to_functions = {
    "hello": greet,
    "goodbye": farewell,
    "failed": failure,
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
