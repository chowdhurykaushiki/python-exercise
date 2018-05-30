# -*- coding: utf-8 -*-
"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. 
(Hint: the string "\n is the same as pressing the ENTER button)
"""
import sys
name=input('Enter your name ')
age=input('enter your age ')
try:
    if int(age)>100:
        var = 'Dear '+name+' congratulations on century!'
        print('Dear ',name,' congratulations on century!')
    else:
        var = 'Dear '+name+' you will turn 100 in the year '+str(2018+(100-int(age)))
        print('Dear ',name,' you will turn 100 in the year ',2018+(100-int(age)))
    copies = int(input('Enter a number '))
    print(copies*var)
    print(copies*(var+"\n"))
except Exception as e:
    print('invalid age: ',e)
    print(sys.exc_info())



