import speech_recognition as sr
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
file = "Sample.wav"
r = sr.Recognizer()
folder = "audio"
sound = AudioSegment.from_wav(file)
chunks = split_on_silence(sound,min_silence_len=500,silence_thresh = sound.dBFS-14,keep_silence=500)
if not os.path.isdir(folder):
    os.mkdir(folder)
for i,chunk in enumerate(chunks,start=1):
    chunk_name = os.path.join(folder,f"chunk{i}.wav")
    chunk.export(chunk_name,format="wav")
    with sr.AudioFile(chunk_name) as src:
        audio_data = r.record(src)
        try:
            text = r.recognize_google(audio_data)
        except:
            print("Error")
        else:
            print(chunk_name,":",text)
