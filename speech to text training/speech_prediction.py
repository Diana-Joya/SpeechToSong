from keras.models import load_model
import numpy as np
from encode_labels import classes

model = load_model('speech_to_text_best_model.hdf5')

def predict(audio):
    p = model.predict(audio.reshape(-1,8000,1))
    idx=np.argmax(p[0])
    return classes[idx]
