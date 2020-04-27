from audio_preprocessing import *
from encode_labels import *
from keras.layers import Dense, Dropout, Flatten, Conv1D, Input, MaxPooling1D
from keras.models import Model
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.optimizers import Adam
from keras import backend

backend.clear_session()


# ------------- Variables -------------
batch_size = 32
epochs = 100

optimizer = 'adam'
monitor = 'val_loss'
# Note: You can also monitor 'val_accuracy'.
# However, monitoring and saving the weights based on the highest val_accuracy may not give you the "best" answer.
# Monitoring 'val_loss' is usually a better answer.
# val_loss and val_accuracy are calculated in entirely different ways.
# In the end you want to use a model with the lowest validation loss.
# If you do that make sure to change mode='min' in the checkpoint callback.


# Convolutional Neural Network Architecture
model_inputs = Input(shape=(8000, 1))

# 1st Layer
conv_model = Conv1D(8, 13, padding='valid', activation='relu', strides=1)(model_inputs)
conv_model = MaxPooling1D(3)(conv_model)
conv_model = Dropout(0.3)(conv_model)

# 2nd Layer
conv_model = Conv1D(16, 11, padding='valid', activation='relu', strides=1)(conv_model)
conv_model = MaxPooling1D(3)(conv_model)
conv_model = Dropout(0.3)(conv_model)

# 3rd Layer
conv_model = Conv1D(32, 9, padding='valid', activation='relu', strides=1)(conv_model)
conv_model = MaxPooling1D(3)(conv_model)
conv_model = Dropout(0.3)(conv_model)

# 4th Layer
conv_model = Conv1D(64, 7, padding='valid', activation='relu', strides=1)(conv_model)
conv_model = MaxPooling1D(3)(conv_model)
conv_model = Dropout(0.3)(conv_model)

# Fully Connected Network Layers
conv_model = Flatten()(conv_model)

conv_model = Dense(256, activation='relu')(conv_model)
conv_model = Dropout(0.3)(conv_model)

conv_model = Dense(128, activation='relu')(conv_model)
conv_model = Dropout(0.3)(conv_model)

model_outputs = Dense(len(labels), activation='softmax')(conv_model)

model = Model(model_inputs, model_outputs)

# Get model summary
model.summary()

# ------------- Fit Model -------------

model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

# Groups trackable objects, saving and restoring them
checkpoint = ModelCheckpoint('speech_to_text_best_model.hdf5',
                             monitor=monitor,
                             mode='min',
                             save_best_only=True,
                             verbose=1)

# Stop training when a monitored quantity has stopped improving
earlystop = EarlyStopping(monitor=monitor,
                          mode='min',
                          min_delta=0.0001,
                          patience=7,
                          verbose=1)

callbacks = [earlystop, checkpoint]

hist = model.fit(
    xtr,
    ytr,
    epochs=epochs,
    callbacks=callbacks,
    batch_size=batch_size,
    validation_data=(xval, yval))
