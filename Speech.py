"""
//user speech
import speech_recognition as sr

# Record Audio

with sr.Microphone() as source:
r = sr.Recognizer()
    print("Say something!")
    audio = r.listen(source)

try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))



import pyaudio
import wave
from pygame import mixer
# Load the required library


FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("recording...")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open("C:/Users/yiren/PycharmProjects/nlp/file.wav", 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
mixer.init()
mixer.music.load("C:/Users/yiren/PycharmProjects/nlp/file.wav")
mixer.music.play()

//text to speech part of project
import playsound

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'zxddxzzxdd ffgy'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file

playsound.playsound('C:/Users/yiren/PycharmProjects/nlp/welcome.mp3', True)

this is a test

from pydub import AudioSegment
import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

sound = AudioSegment.from_mp3("C:/Users/yiren/PycharmProjects/nlp/fightback.mp3")
sound.export("C:/Users/yiren/PycharmProjects/nlp/fightback.mp3", format="wav")

AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
"""

"""
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
"""
import playsound
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
usertext=""
textnumber=0
while(True):
    if(textnumber<1):
        usertext = input("Type something ^-^ ")
    else:
        usertext = input("I'm amazing aren't I. I can speak whatever you type.")
    # The text that you want to convert to audio
    if(usertext!="stop"):
        mytext = usertext

        # Language in which you want to convert
        language = 'en'

        # Passing the text and language to the engine,
        # here we have marked slow=False. Which tells
        # the module that the converted audio should
        # have a high speed
        myobj = gTTS(text=mytext, lang=language, slow=False)
        # Saving the converted audio in a mp3 file named
        # welcome
        temp = str(textnumber)
        myobj.save("text" + temp + ".mp3")
        textnumber += 1
        # Playing the converted file

        playsound.playsound('C:/Users/yiren/PycharmProjects/nlp/text' + temp + '.mp3', True)