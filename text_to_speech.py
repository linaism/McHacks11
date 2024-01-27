import pyttsx3

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)
# engine.setProperty('voice', "com.apple.speech.synthesis.voice.Fred")
# engine.say("Hey, how are you doing?")
# engine.runAndWait()

for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Bless you")
    engine.runAndWait()
    engine.stop()

# karen 
# maged 
# princess 
# rocko (deep)
# sandy (like her name)
# shelley 

