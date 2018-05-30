# -*- coding: utf-8 -*-
"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
 Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python """
Flist=input('Enter elements of first list: ')
Slist=input('Enter elements of second list: ')
Flist=Flist.split(",")
Slist=Slist.split(",")
print(Flist)
print(Slist)
#common=[x for x in Flist for y in Slist if x==y]
common=[x for x in Flist if x in Slist]
common=list(sorted(set(common)))
print(common)


