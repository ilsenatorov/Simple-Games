#!/usr/bin/python3
from random import randrange
import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument("-ru", help="Russian", action='store_true')
parser.add_argument("-en", help="English", action='store_true')
parser.add_argument("-d", help="Print Answer for Debug", action='store_true')
parser.add_argument("-t", help="choose the number of tries", type=int)


args = parser.parse_args()

if args.ru:
    txt_location = '/home/ilya/Projects/Simple-Games/word_rus.txt'
elif args.en:
    txt_location = '/home/ilya/Projects/Simple-Games/word_en.txt'
else:
    txt_location = '/home/ilya/Projects/Simple-Games/word_rus.txt'

list_in = []
list_not_in = []

class Guess(object): #this is a letter that person guessed
    def __init__(self, guess):
        self.guess = guess
    def CheckLen(self):
        if len(self.guess) == 1:
            return True
        else:
            print("This is more than one letter!")
            return False

    def CheckAlreadyTried(self):
        if self.guess in list_in or self.guess in list_not_in:
            return False
            print("You have already tried this letter!")
        else:
            return True

    def CheckIssues(self):
        return self.CheckLen() and self.CheckAlreadyTried

    def CheckIn(self, word):
        if self.guess in word:
            print("Correct guess!")
            list_in.append(self.guess)
            return True
        else:
            print("This letter is not in the word")
            list_not_in.append(self.guess)
            return False




    def CheckWin(self, word):
        for letter in word:
            if letter not in list_in:
                return False
        return True


def print_state(word):
    for letter in word:
        if letter not in list_in:
            print('_ ', end='')
        elif letter in list_in:
            print(letter + " ", end='')
    print("\nLetters not in: " + " ".join(list_not_in))
    # print(list_in)
    if args.d:
        print(word)

txt = open(txt_location, 'r').readlines()
word = txt[randrange(len(txt))]
word = word[:-1]
if args.t is None:
    _Tries = 7
else:
    _Tries = args.t
def PlayGame(the_word, Tries):
    while True:
        print_state(the_word)
        guess = Guess(input("Type in: "))
        if not guess.CheckIssues():
            continue
        if guess.CheckIn(the_word):
            pass
        else:
            Tries -= 1
        if guess.CheckWin(the_word):
            print("You Won!")
            break
        if Tries == 0:
            print("You ran out of Tries! The Word you were trying to guess was:\n" + the_word)
            break
        print("Tries Left: " + str(Tries))
PlayGame(word, _Tries)
