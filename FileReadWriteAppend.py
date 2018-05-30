# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 16:42:41 2018

@author: 212634012
"""
'''Write in a file'''
writeFile = open('C:/KAUSHIKI/Personal/python_exercise/writeFile.txt','w')
with open('C:/KAUSHIKI/Personal/python_exercise/writeFile.txt','w') as writeFile:
    writeFile.write('Hey\n\tI am a nw text')
    writeFile.close()

'''Append in a file'''
appendFile = open('C:/KAUSHIKI/Personal/python_exercise/appendFile.txt','a')
appendFile.write('This is new file\n')
appendFile.write('keep appending\n')
appendFile.close()

'''Read file'''
# way 1 
readFile = open('writeFile.txt','r')
print(readFile.read())
# way 2
readfile2 = open('writeFile.txt','r').read()
print(readfile2)
# way 3 --> converts the whole text in list,where eachline is list element
readFile3=open('writeFile.txt','r').readlines()
print(readFile3)
#way 4 read a single line from file
with open ('python_excercise.txt','r') as f:
    print(f.readline())

#way 5 --> read in a for loop, but there will be a new line character at the end of each line
with open('python_excercise.txt','r') as f:
    for lines in f:
        print(lines)
