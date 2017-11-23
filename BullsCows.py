#!/usr/bin/python3

import random
import argparse

import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-l", help="choose the length of the number", type=int)
parser.add_argument("-t", help="choose the number of tries", type=int)
parser.add_argument("-d", help="show answer for debug", action="store_true")
args = parser.parse_args()


class Guess(object):
    def __init__(self, guess):
        self.guess = guess
    def HasRepeats(self):
        return len(self.guess) != len(set(self.guess))
    def CheckLength(self, num):
        return len(self.guess) != len(num)
    def CheckLonger(self, num):
        return len(self.guess) > len(num)
    def CheckShorter(self, num):
        return len(self.guess) < len(num)
    def CheckProblems(self, num):
        if self.HasRepeats():
            print("Your guess contains repeats!")
            return True
        elif self.CheckLonger(num):
            print("Your guess is too long")
            return True
        elif self.CheckShorter(num):
            print("Your guess is too short")
            return True
        else:
            return False
    def CheckCows(self, num):
        Cows = 0
        for c in self.guess:
            if c in num:
                Cows += 1
        return Cows - self.CheckBulls(num)
    def CheckBulls(self, num):
        Bulls = 0
        integer = 0
        for c in self.guess:
            if c == num[integer]:
                Bulls += 1
            integer += 1
        return Bulls
    def CheckWin(self, num):
        return self.guess == num

def game(NumLength, Tries):
    print("Welcome to the game of Bulls and Cows!")
    print("In order to win you need to guess a number, digits do not repeat.\nWhenever you make a guess you receive hints - Bulls and Cows.")
    print("A Bull means that you guessed a digit and a place correctly.\nA Cow means that you guessed a digit, but not the place.")
    print("Type the command with -h at the end to see help")
    numblist = random.sample(range(9), NumLength)
    numlist = []
    for numb in numblist:
        numlist.append(str(numb))
    num = "".join(numlist)
    while Tries > 0:
        if args.d:
            print(num)
        print("Tries left: " + str(Tries))
        guess = Guess(str(input("Please enter your guess: ")))
        # print(guess.CheckProblems(num))
        if guess.CheckProblems(num) is True:
            print("issue found")
        elif guess.CheckWin(num):
            print("You Won!")
            return
        else:
            print("Bulls: " + str(guess.CheckBulls(num)))
            print("Cows: " + str(guess.CheckCows(num)))
            Tries -= 1
    print("The number was: " + num)
if args.l is None:
    leng = 4
else:
    leng = args.l
if args.t is None:
    tries = 7
else:
    tries = args.t

game(leng, tries)
