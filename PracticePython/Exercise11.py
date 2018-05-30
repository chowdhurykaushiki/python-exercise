# -*- coding: utf-8 -*-
"""
Ask the user for a number and determine whether the number is prime or not. 
"""
def prime(num):
    for n in range(2,num):
        '''
        check till square root for prime
        '''
        if num%n==0:
            return 'Not Prime'
    return "Prime"
try:
    num=int(input("Please enter a number: "))
    if num in (1,2):
        print("Prime")
    else:    
        print(prime(num))
except ValueError as v:
    print("Invalid number")
except Exception as e:
    print("Error: ",e)

