# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:07:09 2018

@author: 212634012
"""
import importlib
import insertionSortList as insSort
importlib.reload(insSort)
insSort.fun()

try:
    numList=[7,1,3,5,8,2]
    length=len(numList)
    print('length: ',length)
    for i in range(length):
        print('i: ',i)
        for j,val in enumerate(numList[:length-(i+1)]):
            if numList[j]>numList[j+1]:
                numList[j],numList[j+1]=numList[j+1],numList[j]
                print('j: ',numList[j])
                print('j+1: ',numList[j+1])
                print(numList)
    print('srted list: ',numList)
except Exception as e:
    print(e)
print(__name__)