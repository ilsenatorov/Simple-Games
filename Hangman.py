#!/usr/bin/env python3
from random import randrange

txt_location = '/home/ilsenatorov/bin/WordList.txt'

txt = open(txt_location).readlines()
the_word = txt[randrange(67655)]

print("Welcome to the game of Hangman!")

def show_state(word):
    state = ''
    for letter in range(len(word)-1):
        state += '_ '
    print(state)
    print()
    print(word)

show_state(the_word)
