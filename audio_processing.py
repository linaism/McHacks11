# import pandas as pd
# import numpy as np
# import matplotlib.pylab as plt
# import seaborn as sns 

# from glob import glob 

# import librosa
# import librosa.display
# import IPython.display as ipd

# sns.set_theme(style="darkgrid")

import pyaudio
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load your pre-trained model
model = load_model('your_model.h5')

# Configure audio stream
chunk_size = 1024
sample_format = pyaudio.paInt16
channels = 1
fs = 44100

p = pyaudio.PyAudio()

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk_size,
                input=True)

# Placeholder for your real-time audio processing code
while True:
    data = np.frombuffer(stream.read(chunk_size), dtype=np.int16)
    # Process data, extract features, and perform model inference
    # ...
    # Check if the model predicts the target sound, and take action accordingly
    if prediction_above_threshold:
        print("Sneezing detected!")
