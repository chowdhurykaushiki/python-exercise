# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 15:04:56 2018

@author: 212634012
"""

def addFunction(num1,num2,num3=3,num4=4):
    '''print('num1',num1);
    print('num2',num2);'''
    print('num1',num1,'num2',num2,num3,num4,'done')
    sum=num1+num2
    print('sum is:',sum)
    
addFunction(1,2);

x=6

def modifyVar():
    print(x+5) #allowed
    x=x+5 #not allowed 
    #(Becuase x cannot be modified within local scope)
    #to modify x, declare it as a global var
    global x
    x=x+5 
    print(x)

#func
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)

ask_ok('Do you really want to quit?')