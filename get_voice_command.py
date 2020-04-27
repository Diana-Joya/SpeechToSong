import sounddevice
import soundfile

sample_rate = 16000
duration = 3 # in seconds
commands_path = 'voice_commands\\'
filename = 'userinput.wav'
audio = commands_path + filename

def get_voice_command():
    print("start recording")
    data = sounddevice.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, blocking=True)
    print("end recording")
    sounddevice.wait()
    soundfile.write(audio, data, sample_rate)
    return filename
