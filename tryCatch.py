# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 01:22:51 2018

@author: 212634012
"""
class ValueTooless(Exception):
    pass

class ValueTooLarge(Exception):
    pass
    
numberList=[1,2]

try:
    num=int(input('enter a number<100 to be added: '))      
    if num>100:
        raise ValueTooLarge
    elif num<0:
        raise ValueTooless
    print('viola! u made it to the list!')
    numberList.append(num)
    print(numberList)   
except ValueError:
    print('Please enter a number')
except ValueTooLarge:
    print('Not more than a century!')
except ValueTooless:
    print('Be positive!')
except Exception as e:
    print(e)        