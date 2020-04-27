# SpeechToSong

This application utilizes Speech-to-Text deep learning methods to convert speech input from the user into a string that will be used by the Genius API to find a song which contains such words. Once a song is found by the Genius API, the song and artist returned will be used to search the song in the Spofity API so it can be played for the user. 

## Demo

A demo of this project can be viewed starting at minute 04:15 here: https://www.youtube.com/watch?v=yrBIzegxFpw&t=273s

## Setup

To run this project, you'll need the following:
- Spotify Client Id & Client Secret

  To get a Spotify Client Id & Secret, you can follow the instructions provided by the following website: 
  https://developer.spotify.com/dashboard/
  Once you've acquired your client Id & secret, you must replace the authentication strings in lines 57 and 58 of the 
  IntegrateAPIs.py file.
- Genius Access Token

  To get a Genius Access Token, you can follow the instructions provided by the following website:
  https://docs.genius.com/
  Once you've acquired your access token, you must replace the authentication string in line 8 of the IntegrateAPIs.py file.
- Flask

  To run this project, you will need to have Flask installed in your local machine. If you don't have Flask, you can follow the
  installation instructions provided by the Flask documentation: https://flask.palletsprojects.com/en/1.1.x/

## Getting Started

The SpeechToSong repository contains the files needed to run a) the SpeechToSong web application developed using Python's SpeechRecognizer library, and b) The Speech to Text Training files to develop a simple small-scale speech to text training model for one word commands. 

### a) SpeechToSong Web Application
#### Python Packages: 
SpeechToSong utilizes the following Python libraries:
- Flask
- SpeechRecognition
- Spotipy
- Requests
- Sounddevice & Soundfile

#### Installing:

1. In the main page of the repository, use the dropdown menu to 'clone or download' the repository. 
2. Once you have the files in your local machine, make sure to update the IntegrateAPIs.py file with your Spotify and Genius authentication keys. 
3. Run the **speech_to_song.py** file.
   A window should pop up with the following information:
```
* Serving Flask app "speech_to_song" (lazy loading)
* Enviroment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
* Debug mode: on
* Restarting with stat

* Debuger is active!
* Debugger PIN: 307-145-361
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
4. Run the localhost address ( http://127.0.0.1:5000/ ) in your preferred browser.

### b) Speech to Text Training
#### Python Packages: 
Speech To Text Training utilizes the following Python libraries:
- Tensorflow
- Keras
- librosa
- sklearn

#### Setup:
1. Make sure you have the required python packages installed in your IDE. To create this project, I used PyCharm 2019.2.3 and Python 3.6.
2. Download the data set from Kaggle ( https://www.kaggle.com/c/tensorflow-speech-recognition-challenge/data ). Then replace the contents inside 'speech to text training/training_data_set/' with the files inside the Kaggle data set folder. 
3. Run 'training_model.py' to train the speech to text model. 

#### Testing the Model:
1. After training the model, run 'test_prediction.py'. A random interger will serve as the index to pick an audio file from the data set, then the application will compare it's prediction with the actual audio file label.


## More Information
For more information on:

- **Genius API:** https://docs.genius.com/#/getting-started-h1
- **Spotify API:** https://developer.spotify.com/

### Note: 
This application is a student project for CPSC 481 - Artificial Intelligence 

