#!/usr/bin/python3

import random
import argparse

import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-difficulty", help="choose the difficulty:\n1 = easy\n2 = medium\n3 = hard\n0 = debug", type=int)
args = parser.parse_args()
print(args.difficulty)

class Number(object):
    def __init__(self, numlist):
        self.numlist = numlist
    def checkBulls(self, guess):
        Bulls = 0
        integer = 0
        for c in guess:
            if c == self.numlist[integer]:
                Bulls += 1
            integer += 1
        return Bulls
    def checkCows(self, guess):
        Cows = 0
        for c in guess:
            if c in self.numlist:
                Cows += 1
        return Cows - self.checkBulls(guess)


class Guess(object):
    def __init__(self, guesslist):
        self.guesslist = guesslist
    def HasRepeats(self):
        return len(self.guesslist) != len(set(self.guesslist))
    def CheckLength(self, numlist):
        return len(self.guesslist) == len(numlist)





number = Number([1,2,3,4])
guess = Guess(list(input("Please enter your guess: ")))
print(number.numlist)
print(guess.guesslist)
print("Repeats: " + str(guess.HasRepeats()))
print("Same Length: " + str(guess.CheckLength(number.numlist)))
print("Bulls: " + str(number.checkBulls(guess.guesslist)))
print("Cows: " + str(number.checkCows(guess.guesslist)))
