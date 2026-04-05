'''
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file 'Hi-score.txt' which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.
'''

import random

def game():
    f = open(r"D:\learn python\chapter 9\problems\Hi-score.txt")
    usr_name = input("Enter your name: ")
    print("Ypu are playing the game....")
    usr_score = random.randint(1, 10000)
    print(f"your score is: {score}")
    with open(r"D:\learn python\chapter 9\problems\Hi-score.txt") as f:
        old_score = f.read()
        
    