# SpeechToSong

This application utilizes Speech-to-Text deep learning methods to convert speech input from the user into a string that will be used by the Genius API to find a song which contains such words. Once a song is found by the Genius API, the song and artist returned will be used to search the song in the Spofity API so it can be played for the user. 

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
To run this project, you will need to have Flask installed in your local machine. If you don't have Flask, you can follow the installation instructions provided by the Flask documentation: https://flask.palletsprojects.com/en/1.1.x/

1. In the main page of the repository, use the dropdown menu to 'clone or download' the repository. 
2. If you choose to download the repository: 
- Unzip the files inside the downloaded zip folder into your preferred local folder. 
- If you have python installed in your local machine, double click the **speech_to_song.py** file.
- A window should pop up with the following information:
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
- Run the localhost address ( http://127.0.0.1:5000/ ) in your preferred browser.



For more information on:

- **Genius API:** https://docs.genius.com/#/getting-started-h1
- **Spotify API:** https://developer.spotify.com/

### Note: 
This application is a student project for CPSC 481 - Artificial Intelligence 




To use speech to text training:
- Tensorflow
- Keras
- librosa
- sklearn
