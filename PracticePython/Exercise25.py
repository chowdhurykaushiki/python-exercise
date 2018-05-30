# -*- coding: utf-8 -*-
"""
You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, 
and you, the user, will say whether it is too high, too low, or your number.
At the end of this exchange, 
your program should print out how many guesses it took to get your number.
"""
class inputError(Exception):
    pass
class guessGame:
    def guessNum(self,minRange,maxRange):
        nguess=random.randint(minRange,maxRange)
        return nguess
    
    def printGuess(self,guess):
        print('Guess: ',guess)
        userInp=int(input("Press 1: if the guess was too high \n Press 2: if the guess was too low \n Press 3: if correct!\n"))
        if userInp not in (1,2,3):
            raise inputError
        return userInp

if __name__=="__main__":
    import random
    try:
        print("Hey there!\n pick a range of number and I will guess it!!")
        minRange=int(input('minRange: '))
        maxRange=int(input('maxRange: '))
        numList=list(range(minRange,maxRange+1))
        midNumIdx=numList[int(len(numList)/2)]
        guess=numList[midNumIdx]
        gOBJ=guessGame()
        userInp=int(gOBJ.printGuess(guess))
        count=1
        print('count: ',count)
        print('userInp: ',userInp)
        while userInp != 3:
            count=count+1
            if userInp == 1:
                maxRange=guess-1
                guess=gOBJ.guessNum(minRange,maxRange)
                userInp=int(gOBJ.printGuess(guess))
            elif userInp==2:
                minRange=guess+1
                guess=gOBJ.guessNum(minRange,maxRange)
                userInp=int(gOBJ.printGuess(guess))
            else:
                break
        
        print('Viola! I guessed correct with ',count,' attempt!!')
    except inputError :
        print('invalid input')
    except ValueError:
        print('Invalid value entered,Better Luck next time!')
    except Exception as e:
        print('Error: ',e)



    
        
        