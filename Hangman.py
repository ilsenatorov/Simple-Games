#!/usr/bin/python3

### game of hangman
from random import randrange
txt_location = '/home/ilya/Projects/Simple-Games/word_rus.txt'
list_of_guesses = []
list_not_in = []

txt = open(txt_location).readlines()
the_word = txt[randrange(len(txt))]
the_word = the_word[:-1]

word_list = []
for letter in the_word:
    word_list.append(letter)

Tries = 7

def show_state():
    for letter in word_list:
        if letter not in list_of_guesses:
            print('_ ', end='')
        elif letter in list_of_guesses:
            print(letter + " ", end='')
    # print('\n' + "".join(word_list))
    print("\nLetters not in: " + " ".join(list_not_in))

def MakeGuess(word):
    Guess = input("Guess a letter: ")
    if len(Guess) !=1:
        print("This guess is too long")
        return False
    elif Guess in list_of_guesses or Guess in list_not_in:
        print("You already guessed this letter")
        return False
    elif Guess not in word:
        print("This letter is not in the word")
        list_not_in.append(Guess)
        return True
    elif Guess in word:
        print("Correct guess")
        list_of_guesses.append(Guess)
        return False
    else:
        print("Unknown error")
        return False

def CheckWin():
    for letter in word_list:
        if letter not in list_of_guesses:
            return False
    return True

def PlayGame(TriesLeft, word):
    print("Welcome to the game of Hangman!")
    show_state()
    while TriesLeft >= 0:
        if CheckWin():
            print("You won!")
            return
        elif MakeGuess(word):
            TriesLeft -= 1
        show_state()
        print("Tries left: " + str(TriesLeft))
PlayGame(Tries, word_list)
