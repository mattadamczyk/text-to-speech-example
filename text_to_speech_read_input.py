import pyttsx3
import pyaudio
import sys
import traceback
import os
import ffmpeg

engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[2].id)

input_text = "C:\\tmp\\input\\my_file.txt"
output_dir = "C:\\tmp\\output\\"

## Functions
def check_voice_list():
    index = 0
    for voice in voices:
        print(f'index -> {index} -- {voice.name}')
        index +=1
check_voice_list()

# Convert text to speech, and capture audio output to a file
def talk(text, file_name):
    engine.say(text)
    engine.save_to_file(text, file_name)

def main():
    # Read script lines from file
    count = 0
    with open(input_text, 'r') as text_file:
        for line in text_file:
            count += 1
            file_name =  output_dir + str("%03d" % count) + ".mp3"
            print(file_name)
            talk(line, file_name)

    while True:
        engine.runAndWait()

if __name__ == "__main__":
    main()