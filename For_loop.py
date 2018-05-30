# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 20:02:13 2018

@author: 212634012
"""

#for loop with a list
for each in [1,2,3,4]:
    print(each)
    
v_list=[1,2,3,4,5,6]
for i in v_list:
    print(i)

# for loop with Tuples
for each in (1,2,3,4):
    print(each)

v_tuple=(1,2,3,4,5,6)
for i in v_tuple:
    print(i)

# for loop with range of values
for i in range(1,10):
    print(i)

for i in range(10):
    print(i,end=',')


for i in reversed(range(1,10)):
    print(i)

for i in range(10,1,-1):
    print(i)
    
for i in 'ABCD':
    print(i)

l=[range(5)]
print(l)# prints [range(0, 5)]

l=list(range(5))
print(l)

a=(1,2,3,4)
l=list(a)
print(l)