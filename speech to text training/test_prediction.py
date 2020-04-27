from random import randint
from encode_labels import xval, yval, classes
import numpy as np
from speech_prediction import predict

idx = randint(0, len(xval)-1)
samples = xval[idx].ravel()
print("Audio:", classes[np.argmax(yval[idx])])
print("Text:", predict(samples))