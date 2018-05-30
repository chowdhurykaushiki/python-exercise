# -*- coding: utf-8 -*-
"""
Create a program that asks the user for a number and 
then prints out a list of all the divisors of that number. 
"""
import sys
try:
    num= int(input("please enter a number: "))
    divisorList=[]
    for x in range(1,num+1):
        if num%x==0:
            divisorList.append(x)
    print("list of divisor: ",divisorList)
except ValueError as v:
    print("Invalid Number")
except Exception as e:
    print("Error: ",e)
    print(sys.exc_info())