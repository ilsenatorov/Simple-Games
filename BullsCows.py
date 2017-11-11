#!/usr/bin/python3
'''
add the replay feature, with choosing difficulty. Need to turn the whole game into a function,
so I can add recursion
'''
import random

print("Welcome to the game of Bulls and Cows!")
print("In order to win you need to guess a number, digits do not repeat.\nWhenever you make a guess you receive hints - Bulls and Cows.")
print("A Bull means that you guessed a digit and a place correctly.\nA Cow means that you guessed a digit, but not the place.")
print()

def game():
    difficulty = input("Type easy, medium or hard to choose the difficulty: ") #allows player to choose the difficulty
    if difficulty == "easy" or difficulty == "Easy":
      print("Your number contains 3 digits")
      NumLength = 3
      Tries = 8
    elif difficulty == "medium" or difficulty == "Medium":
      print("Your number contains 4 digits")
      Tries = 7
      NumLength = 4
    elif difficulty == "hard" or difficulty == "Hard":
      print("Your number contains 5 digits")
      NumLength = 5
      Tries = 10
    elif difficulty == "Insane" or difficulty == "insane":
      NumLength = 6
      Tries = 15
      print("Wow you are insane!")
      print("Your number contains 6 digits")
    elif difficulty == "debug":#DEBUGGING MODE
      NumLength = 3
      Tries = 3
    else:
      print("You chose the deafult difficulty - medium. Your number contains 4 digits")
      Tries = 7
      NumLength = 4

    MyNum = random.sample(range(9), NumLength)#creates the number to guess
    MyNumList = []
    for c in MyNum:#turns the number to be guessed into a readable form to print in the end
      MyNumList.append(str(c))

    if difficulty == "debug": #DEBUGGING FEATURE
      print("".join(MyNumList))

    def CheckBulls(TheGuess): #checks for presence of Bulls in the number
      Bulls = 0
      integer = 0
      for c in TheGuess:
        if c == MyNum[integer]:
          Bulls += 1
        integer += 1
      return Bulls

    def CheckCows(TheGuess): #checks for presence of cows including bulls in the number
      Cows = 0
      for c in TheGuess:
        if c in MyNum:
          Cows += 1
      return Cows

    def HasRepeats(Number): #Checks if integer has any repeated digits.
      digits = Number
      return len(digits) != len(set(digits))

    Guesslist = []

    def PlayTheGame(TriesLeft): #defines the function that starts the game
      while TriesLeft >= 0:
        Guesslist = []
        if TriesLeft == 0: #checks lose condition, breaks the loop and prints the right answer
          print("You are out of tries! The number you were trying to guess was:" + "".join(MyNumList))
          break
        Guess = input("Please make a guess:") #takes user input
        if HasRepeats(Guess): #check for repeats
          print("Your guess contains repeat digits!")
          print("You have " + str(TriesLeft) + " Tries left!")
          PlayTheGame(TriesLeft)
        elif len(Guess) > NumLength: #check for correct length
          print("Your guess has more digits than the number I guessed!")
          print("You have ", TriesLeft, "Tries left!")
          PlayTheGame(TriesLeft)
        elif len(Guess) < NumLength: #check for correct length
          print("Your guess has less digits than the number I guessed!")
          print("You have ", str(TriesLeft), "Tries left!")
          PlayTheGame(TriesLeft)
        for q in Guess: #turns the Guess into a list
          Guesslist.append(int(q))
        print("Number of Bulls:" + str(CheckBulls(Guesslist))) #tells number of Bulls
        print ("Number of Cows:", CheckCows(Guesslist) - CheckBulls(Guesslist)) #tells number of Cows
        if Guesslist == MyNum: #checks for win condition
          print("You Won!")
          return
        TriesLeft -= 1
        print("You have ", TriesLeft, "Tries left!")

    PlayTheGame(Tries)
    print('Thanks for playing!')
    if_replay = input('If you want to play again, type "y". Type anything else if you don\'t: ')
    if if_replay == 'y':
        game()
    else:
        print('See you next time')
        return
game()
