# -*- coding: utf-8 -*-
"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""
var=input("enter: ")
print(var[0:])
print(var[::-1])
if var[0:] == var[::-1]:
    print("palindrome")
else:
    print("not palindrome")
#================================#
#Another way
var=input("Enter the string: ") 
rev=""
for x in reversed(range(len(var))):
    rev=rev+var[x]
print(rev)
if var==rev:
        print("palindrome")
else:
    print("not palindrome")

#=====================================#

## info
l=[1,2,3,4]
print(l)
l.reverse()
print(l)
print(l.reverse()) 
""" This will return None as the reverse() modifies the list in place
and returns None. Thus printing the function will print none"""

