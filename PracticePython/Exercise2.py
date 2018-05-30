# -*- coding: utf-8 -*-
"""
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) 
and one number to divide by (check). If check divides evenly into num, 
tell that to the user. If not, print a different appropriate message.
"""

try:
    num=int(input("Enter an integer number: "))
    if num%2==0:
        print("You entered an even number")
        if num%4==0:
            print("Number is multiple of 4")
    else:
        print("You entered an odd number")
except Exception as e:
    print("Please enter an Integern number ")

# ternary operator
num=16
print("odd") if num%2!=0 else (print("even and multiple of 4") if num%4==0 else print("even"))