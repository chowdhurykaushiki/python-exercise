# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 01:30:14 2018

@author: 212634012
"""
dictVal={}
dictVal['kol']= int('033')
dictVal['bang']= int('088')
print(dictVal)
print(dictVal.keys())
dictVal.values()
dictVal.items()
l=dictVal.values()
print(l)
print(list(l))
print(tuple(l))

#dict.item()
for k in dictVal.items():
    print(k)

#dict()
d=[(x,x**2) for x in range(6)]
dict(d)

#use dictionary
keyList=['tuki','dripto','tuk','babtu','kaushiki','driptaroop']
ageTuple=(21,22,23,24,25,26)

combiDict={}
for key in keyList:
    combiDict[key]=ageTuple[keyList.index(key)]
print(combiDict)
    
l=[1,2,5,3]
sorted(l)
print(l)
l.sort()
print(l)