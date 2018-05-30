# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:17:49 2018

@author: 212634012
"""

a,b,c,d,e=1,2,3,4,1
if a<c>b :
    print('c greater than a and b')
    
if a<c>b<d :
    print('d greater than b')

if a==e:
    print('a and e are equal')

if a!=b:
    print('a and b are not equal')
    
if a<b:
    print('a is less than b')
elif a>b:
    print('a is greater than b')
else :
    print('a and b are equal')