import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split as tts
import numpy as np
from keras.utils import np_utils

audio_path = '.\\training_data_set\\train\\audio\\'
trainlabels = os.listdir(audio_path)
processed_labels = np.load('processed_labels.npy')
processed_waves = np.load('processed_waves.npy')

le = LabelEncoder()
y = le.fit_transform(processed_labels)
classes = list(le.classes_)
print(processed_labels)

y = np_utils.to_categorical(y, num_classes=len(trainlabels))
processed_waves = np.array(processed_waves).reshape(-1, 8000, 1)
xtr, xval, ytr, yval = tts(np.array(processed_waves), np.array(y),
                            stratify=y, test_size=0.2, random_state=777, shuffle=True)
