# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 22:34:44 2018

@author: 212634012
"""
"""
    List comprehension
"""
vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
comprehensiveList=[x*2 for x in vec]
print(comprehensiveList) #[-8, -4, 0, 4, 8]

# filter the list to exclude negative numbers
postvList=[x for x in comprehensiveList if x>=0]
print(postvList) #[0, 4, 8]

# apply a function to all the elements
funcList=[abs(x) for x in comprehensiveList]
print(funcList) #[8, 4, 0, 4, 8]

## call a method on each element
fruits=['apple/','banana/','mango/']
sfruits = [x.strip('/') for x in fruits]
print(sfruits) #['apple', 'banana', 'mango']

# create a list of 2-tuples like (number, square)
numList = [(x,x**2) for x in range(6)]
print(numList)




