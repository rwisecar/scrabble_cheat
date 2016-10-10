""" This is a simple python script to take a Scrabble rack of 7 letters and return all possible word iterations, with the associated scores."""

import re

# Dictionary of letters and values
scores = {
    "a": 1,
    "c": 3,
    "b": 3,
    "e": 1,
    "d": 2,
    "g": 2,
    "f": 4,
    "i": 1,
    "h": 4,
    "k": 5,
    "j": 8,
    "m": 3,
    "l": 1,
    "o": 1,
    "n": 1,
    "q": 10,
    "p": 3,
    "s": 1,
    "r": 1,
    "u": 1,
    "t": 1,
    "w": 4,
    "v": 4,
    "y": 4,
    "x": 8,
    "z": 10
}

# Script to open and read the sowpods.txt word file, and strip of extraneous characters

access_sowpods = open("sowpods.txt", "r+")
sowpods = []

for i in access_sowpods:
    i = i.strip(' \n\r')
    sowpods.append(i)

# Get the scrabble rack from the user
def intro():
    user_name = raw_input("Hello there! I see you want to win at Scrabble. I can help. First, tell me your name.")
    print "Nice to meet you, %s." % user_name

def get_rack():
    input = raw_input("Now tell me, what 7 letters are we working with here? ").upper()
    rack = ""
    if len(input) < 7:
        print("I'm sorry, you haven't entered a full rack. Please try again.")
        exit()
    else:
        for i in input:
            if re.match(r'^[A-Z]', i):
                rack = rack + i
            else:
                print("I'm sorry, that is not a valid Scrabble rack. Please try again.")
                exit()
    print rack

get_rack()
