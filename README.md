# text-to-speech-example
A simple text to speech script written in Python.

**text_to_speech.py:** This is a prototype example of using text to speech and saving the audio as an MP3 file. 

**text_to_speech_read_input.py:** A more robust example of text to speech. It reads from an input file, iterates over the lines, speaks each line, and generates an mp3 file as output for each line.

Works with text-to-speech voices available for Windows 10.

## Check installed voices (optional)
By default Windows 10 comes with 2 voice packs, "David" and "Zira". The program can reference these by id: 0 is male, 1 is female. You may want to install additional text-to-speech voice packs. If you do, this can change the voice index id, i.e.
- index -> 0 -- Microsoft David Desktop - English (United States)
- index -> 1 -- Microsoft Linda - English (Canada)
- index -> 2 -- Microsoft Susan - English (United Kingdom)
- index -> 3 -- Microsoft Heera - English (India)
- index -> 4 -- Microsoft Hazel Desktop - English (Great Britain)
- index -> 5 -- Microsoft Catherine - English (Australia)
- index -> 6 -- Microsoft Zira Desktop - English (United States)

The function check_voice_list() is included to verify which voice packs are installed and available for use, as well as their id's.

## References & Inspiration
https://medium.com/@charles.guinand/installing-wsl2-python-and-virtual-environments-on-windows-11-with-vs-code-a-comprehensive-guide-32db3c1a5847
https://www.geeksforgeeks.org/how-to-save-pyttsx3-results-to-mp3-or-wav-file/
