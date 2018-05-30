# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:50:23 2018

@author: 212634012
"""
print('outside fun',__name__)
def fun():
    print('inside fun',__name__)
    num=[4,3,2,1,5]
    length=len(num)
    for i in range(length):
        minIdx=i
        for j in range(i+1,length):
           if num[j]<num[minIdx]:
               minIdx=j
        num[i],num[minIdx]=num[minIdx],num[i]
    print(num)

        