import speech_recognition as sr
import pygame
import threading
import pyttsx3
from nrclex import NRCLex
import random

r = sr.Recognizer()
pygame.mixer.init()

def play_mp3(file_path):
    # pygame.mixer.init()
    pygame.mixer.music.load("audio/" + file_path)
    pygame.mixer.music.play()

def play_voice(text):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    engine = pyttsx3.init()
    newVoiceRate = 160
    engine.setProperty('rate', newVoiceRate)
    engine.setProperty('voice', "com.apple.eloquence.en-US.Grandpa")
    engine.say(text)
    engine.runAndWait()

def greet():
    print("Hello there! How can I assist you?")

def farewell():
    print("Goodbye! Have a great day!")
    pygame.quit()
    exit()

def play_audio(file_path):
    print(f"Playing {file_path}...")
    threading.Thread(target=play_mp3, args=(file_path,)).start()

def failure():
    print("Playing failure tone...")
    threading.Thread(target=play_mp3, args=("failed.mp3",)).start()

def fear():
    print("Playing scary music...")
    threading.Thread(target=play_mp3, args=("kitchen_sound.mp3",)).start()

def mansplain():
    print("Mansplaining...")
    threading.Thread(target=play_voice, args=("Actually",)).start()

def joy():
    print("Playing happy music...")
    threading.Thread(target=play_mp3, args=("yippee.mp3",)).start()

def sadness():
    print("Playing sad sound...")
    threading.Thread(target=play_mp3, args=("sad_violin.mp3",)).start()

def anger():
    print("Playing angry music...")
    threading.Thread(target=play_mp3, args=("metal-pipe-clang.mp3",)).start()

def anticipation(): 
    print("Playing anticipation music...")
    threading.Thread(target=play_mp3, args=("kitchen_sound.mp3",)).start()

def surprise():
    print("Playing surprise music...")
    threading.Thread(target=play_mp3, args=("amongus.mp3",)).start()

def positive():
    print("Playing positive music...")
    threading.Thread(target=play_mp3, args=("happy.mp3",)).start()

def negative():
    print("Playing negative music...")
    threading.Thread(target=play_mp3, args=("spongebob_fail.mp3",)).start()

def disgust():
    print("Playing disgust music...")
    threading.Thread(target=play_mp3, args=("goofy-ahh-sounds.mp3",)).start()

keywords_to_functions = {
    "hello": greet,
    "goodbye": farewell,
    "failed": failure,
    "scared": fear,
    "gloomy": fear,
    "economy": mansplain,
    "happy": joy,
    "cheerful": joy,
    "died": sadness,
    "hard": sadness,
    "fear": fear,
    "anger": anger,
    "surprise": surprise,
    # "positive": positive,
    "negative": negative,
    "disgust": disgust,
    "anticipation": anticipation,
    "sadness": sadness,
    "disgust": disgust,
    "joy": joy,
    "i think": mansplain,
}

def listen_and_trigger():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)

        while True:
            try:
                print("Listening...")
                audio_chunk = r.listen(source, phrase_time_limit=5)

                # Process the audio chunk
                text = r.recognize_google(audio_chunk).lower()
                print("You said:", text)

                text_object = NRCLex(text)
                emotion_scores = text_object.raw_emotion_scores
                print('\n', emotion_scores)

                if len(text_object.raw_emotion_scores) != 0:
                    emotion_scores.pop('trust', None)

                if len(text_object.raw_emotion_scores) != 0:
                    emotion_scores.pop('positive', None)

                if len(text_object.raw_emotion_scores) != 0:
                    max_score = max(emotion_scores.values())
                    highest_score_emotions = [emotion for emotion, score in emotion_scores.items() if score == max_score]
                    selected_emotion = random.choice(highest_score_emotions)
                    print("Dominant emotion:", selected_emotion)
                    keywords_to_functions[selected_emotion]()
                else: 
                    for keyword, function in keywords_to_functions.items():
                        if keyword in text:
                            function()
                            break
                    

            except sr.UnknownValueError:
                print("Unable to recognize speech.")
            except sr.RequestError as e:
                print("Error occurred:", str(e))
            # timeout passed, continue listening

if __name__ == "__main__":
    listen_and_trigger()
