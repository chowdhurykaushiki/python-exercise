# -*- coding: utf-8 -*-
"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game)
"""

print("rock/scissors/paper")
playerA=input("Call from Player A : ")
playerB=input("Call from Player B: ")
if playerA not in ('rock','scissors','paper') or playerB not in ('rock','scissors','paper'):
    print("Invalid input, Game over!")
else:
    if playerA == playerB :
        print("None won!")
    elif playerA == 'rock':
        print("playerA won!") if playerB == 'scissors' else print("playerB won")
    elif playerA == 'scissors':
        print("playerA won!") if playerB == 'paper' else print("playerB won")
    elif playerA == 'paper':
        print("playerA won!") if playerB =='rock' else print("playerB won")
  
