import speech_recognition as sr

recognizer = sr.Recognizer()
path = '.\\voice_commands\\'
error = 'error'

def speech_to_text(filename):
    filename = path + filename
    input = sr.AudioFile(filename)
    with input as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.record(source)

    type(audio)
    try:
        recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return error
    return recognizer.recognize_google(audio)