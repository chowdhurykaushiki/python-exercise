# -*- coding: utf-8 -*-
firstInput=input("please enter the fisrt input: ")
secondInput=input("please enter the fisrt input: ")
firstList=[]
secondList=[]
commonList=[]
for x in firstInput:
    if x != ',':
        firstList.append(x)
print(firstList)
for x in secondInput:
    if x!=',':
        secondList.append(x)
print(secondList)
        
for y in firstList:
    for z in secondList:
        if y==z:
            commonList.append(y)
print('common :',commonList)

    
