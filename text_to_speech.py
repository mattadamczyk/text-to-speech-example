import pyttsx3
import pyaudio
import sys
import traceback
import os
import ffmpeg

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)

## Functions
def check_voice_list():
    index = 0
    for voice in voices:
        print(f'index -> {index} -- {voice.name}')
        index +=1
check_voice_list()

# Save output to a file
def talk(text):
    engine.say(text)
    engine.save_to_file(text, 'speech.mp3')

def main():
    talk('This is an example of using text to speech and saving it as an MP3 file.')

    while True:
        engine.runAndWait()

if __name__ == "__main__":
    main()