# -*- coding: utf-8 -*-
"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
and makes a new list of only the first and last elements of the given list. 
For practice, write this code inside a function.
"""
def newList(numList):
    newList=[x for x in numList if x==numList[0] or x==numList[-1]]
    return newList
    
num=input("please enter the list of numbers: ")
numList=num.split(",")
print(numList)
newList=newList(numList)
print(newList)
