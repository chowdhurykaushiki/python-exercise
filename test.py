# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 22:41:03 2018

@author: 212634012
"""
import json

keyList=['tuki','dripto','tuk','babtu','kaushiki','driptaroop']
ageTuple=(21,22,23,24,25,26)

dictVal={}
for key in keyList:
    dictVal[key]=ageTuple[keyList.index(key)]

with open('test.txt','w') as f:
    json.dump(dictVal,f)