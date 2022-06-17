#program to read small audio files
import speech_recognition as sr
file = "Sample.wav"
r = sr.Recognizer()
with sr.AudioFile(file) as src:
    audio_data=r.record(src)
    text = r.recognize_google(audio_data)
    print(text)