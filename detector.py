import tkinter as tk
from tkinter import ttk
from functools import partial

import speech_recognition as sr
import pygame
import threading
import pyttsx3
from nrclex import NRCLex
import random

class SoundPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SoundPlayerApp")

        self.is_listening = False

        self.start_button = ttk.Button(root, text="Start", command=self.start_listening)
        self.stop_button = ttk.Button(root, text="Stop", command=self.stop_listening)
        self.start_button.grid(row=0, column=0, padx=10, pady=10)
        self.stop_button.grid(row=0, column=1, padx=10, pady=10)

        self.r = sr.Recognizer()
        pygame.mixer.init()

    def play_audio(self, file_path):
        print(f"Playing {file_path}...")
        threading.Thread(target=self.play_mp3, args=(file_path,)).start()

    def play_mp3(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        pygame.mixer.music.wait()

    def play_voice(self, text):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        engine = pyttsx3.init()
        new_voice_rate = 160
        engine.setProperty('rate', new_voice_rate)
        engine.setProperty('voice', "com.apple.eloquence.en-US.Grandpa")
        engine.say(text)
        engine.runAndWait()

    def start_listening(self):
        if not self.is_listening:
            self.is_listening = True
            threading.Thread(target=self.listen_and_trigger).start()

    def stop_listening(self):
        self.is_listening = False

    def listen_and_trigger(self):
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=1)

            while self.is_listening:
                try:
                    print("Listening...")
                    audio_chunk = self.r.listen(source, phrase_time_limit=5)

                    text = self.r.recognize_google(audio_chunk).lower()
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
                        # Call the corresponding function based on the selected emotion
                        self.keywords_to_functions[selected_emotion]()

                except sr.UnknownValueError:
                    print("Unable to recognize speech.")
                except sr.RequestError as e:
                    print("Error occurred:", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = SoundPlayerApp(root)
    root.mainloop()
