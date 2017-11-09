#!/usr/bin/python3
from random import randrange
#
txt_location = '/home/ilya/Projects/Simple-Games/word_rus.txt'
# txt_location = '/home/ilya/Projects/Simple-Games/WordList.txt'

list_of_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
list_of_guesses = []
txt = open(txt_location).readlines()
the_word = txt[randrange(len(txt))]
the_word = the_word[:-1]
word_list = []
for letter in the_word:
    word_list.append(letter)
print("Welcome to the game of Hangman!")

def show_state(word):
    for letter in word_list:
        if letter not in list_of_guesses:
            print('_ ', end='')
        elif letter in list_of_guesses:
            print(letter + " ", end='')
    print('\n')
    print("".join(word_list))

show_state(the_word)


def MakeGuess(word):
    Guess = input("Guess a letter: ")
    if len(Guess) != 1:
        print("Your guess is too long")
        return
    list_of_guesses.append(Guess)
    if Guess not in word:
        print("This letter is not in the word")
        return
    show_state(the_word)
    # elif Guess in word:

MakeGuess(the_word)
