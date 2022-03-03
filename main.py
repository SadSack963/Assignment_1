"""
This program converts an input text to Morse Code printed in the console.
An audio simulation is also generated.
"""

import csv
import simpleaudio
from time import sleep


def to_morse(char):
    # If character is a space between words, then print an extra 3 spaces
    if char == " ":
        print(" " * 3, end="")
        sleep(0.4)
        return
    # Print the morse code with a spaces between characters
    morse_code = dict_characters[char]
    print(morse_code, end=" ")
    # Play the appropriate audio
    for ch in morse_code:
        if ch == ".":
            play_dit = dit.play()
            play_dit.wait_done()
        else:
            play_dah = dah.play()
            play_dah.wait_done()


# Create a dictionary from the CSV file
with open("data/characters.csv") as fp:
    reader = csv.reader(fp)
    reader.__next__()  # Ignore the header row
    dict_characters = {row[0]: row[1] for row in reader}
    # print(dict_characters)

# Define the dot/dash wave objects
dit = simpleaudio.WaveObject.from_wave_file("audio/dit.wav")
dah = simpleaudio.WaveObject.from_wave_file("audio/dah.wav")

text = input("Enter your text: ").upper()
for character in text:
    to_morse(character)
    sleep(0.2)
print()
