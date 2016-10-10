""" This is a simple python script to take a Scrabble rack of 7 letters and return all possible word iterations, with the associated scores."""

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

#
