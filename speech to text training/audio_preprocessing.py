import os
import librosa
import numpy as np
from scipy.io import wavfile

# import pathlib
# print(pathlib.Path(__file__).parent.absolute())

'''
Librosa is a python module for audio and music processing.
matplotlib is a python module to help us plot a visual representation of our audio wave.
SciPy is another python module we'll be using for help with audio processing.
'''

train_audio_path = '.\\training_data_set\\train\\audio\\'
labels = os.listdir(train_audio_path)

processed_waves = []
processed_labels = []
for label in labels:
    print(label)
    waves = [f for f in os.listdir(train_audio_path + label) if f.endswith('.wav')]
    for wav in waves:
        samples, s_rate = librosa.load(train_audio_path + label + '\\' + wav, sr=16000)
        samples = librosa.resample(samples, s_rate, 8000)
        if (len(samples)== 8000):
            processed_waves.append(samples)
            processed_labels.append(label)

np.save('processed_labels', processed_labels)
np.save('processed_waves', processed_waves)