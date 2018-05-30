# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 22:56:38 2018

@author: 212634012
"""

x_list=['blue','white','green','red','black']
#print the entire list
print(x_list)
#access list elements
a=x_list[1]
print(a)
#slice list
small_list=x_list[1:4]
print(small_list)
print(x_list[:4])
print(x_list[0:])
print(x_list[-1:])
print(x_list[-2:-1])
print(x_list[-2:0])#invalid

#length of list
print(len(x_list))

#count occurence of element in a list
print(x_list.count('blue'))

#get the index of a list element
print(x_list.index('green'))

#sort a list
x_list.sort()
print(x_list) #this sorts the existing list
sorted(x_list) #this returns a new list which is sorted, but doesnot modify the original list

#append to a list
x_list.append('violet')
print(x_list)

#insert an element in an index
x_list.insert(1,'scarlet')
print(x_list)

#assign a list to another variable
y_list=x_list
print(y_list)
print(x_list)

#Remove first occurance of any element
x_list.remove('black')
print(x_list)
x_list.remove(x_list[1])
print(x_list)

#remove last element from list
x_list.pop()
print(x_list)

#reverse a list
x_list.reverse()
print(x_list)

#delete an element from list
del x_list[1]
#delete a slice of element from the list
del x_list[1:3]
#delete entire list
y_list=x_list
del y_list

#list with if
if 'violet' in x_list:
    print('violet is in list')
#list with for
for item in x_list:
    print(item)
#list with while
while len(x_list)>0:
    print(x_list)
    x_list.pop()
#multi dimensional list
multi_list = [[5,6,7],
              [1,2],
              1,
              ['a','b','c','d']
             ]
print(multi_list[3][1])
#we can put data of different type in the same list
c=[1,'a',2,1.44444]

