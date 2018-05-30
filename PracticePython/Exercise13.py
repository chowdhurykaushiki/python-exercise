# -*- coding: utf-8 -*-
"""
Write a program that asks the user how many Fibonnaci numbers to generate 
and then generates them. 
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
"""
def fibonacci(num):
    a,b=1,1
    fibList=[]
    fibList.append(a)
    fibList.append(b)
    for x in range(3,num+1):
        a,b=b,a+b
        fibList.append(b)
    return (fibList)

try:
    num=int(input("Enter the number to generate Fibonacci series: "))
    if num < 0 :
        raise Exception
    fibList=fibonacci(num)
    print(fibList)
except ValueError:
    print("Invalid number")
except Exception as e:
    print("Error: ",e)