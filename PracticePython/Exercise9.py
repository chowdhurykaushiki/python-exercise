# -*- coding: utf-8 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, 
too high, or exactly right. 

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random
randNum=random.randint(1,9)
#print(randNum)
count = 0
tries='Y'
while tries in ('y','Y'):
    num=int(input("Enter your guess between 1 and 9 : "))
    if num>randNum:
        print("You guessed too high")
    elif num<randNum:
        print("You guessed too low")
    else:
        count=count+1
        print("Viola! you guessed correct")
    tries = input("Please press 'y' to play again and 'n' to exit ")
    if tries not in ('Y','y'):
        print("Your correct guess: ",count,"! Good bye")
        break
