# -*- coding: utf-8 -*-
"""
Write a program (using functions!) that asks the user for a long string containing multiple words. 
Print back to the user the same string, 
except with the words in backwards order.
"""
string=input("Enter a long string:\n ")
strList=string.split(" ")
strList.reverse()
revStr=" ".join(strList)
print(revStr)