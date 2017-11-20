#!/usr/bin/python3

import random
import argparse

import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-difficulty", help="choose the difficulty:\n1 = easy\n2 = medium\n3 = hard\n0 = debug", type=int)
args = parser.parse_args()

if args.difficulty == 1:
  print("Your number contains 3 digits")
  NumLength = 3
  Tries = 8
elif args.difficulty == 2:
  print("Your number contains 4 digits")
  Tries = 7
  NumLength = 4
elif args.difficulty == 3:
  print("Your number contains 5 digits")
  NumLength = 5
  Tries = 10
elif args.difficulty == 0:
  print("Welcome to debug")#DEBUGGING MODE
  NumLength = 3
  Tries = 3
else:
  print("You chose the default difficulty - medium. Your number contains 4 digits")
  Tries = 7
  NumLength = 4
