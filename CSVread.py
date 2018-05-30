# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 17:13:36 2018

@author: 212634012
"""

import csv
country,age,salary=[],[],[]
with open('C:/KAUSHIKI/Personal/python_exercise/CSVread.csv') as readCSVFile:
    readFile=csv.reader(readCSVFile,delimiter=',')
    
    for row in readFile:
        country.append(row[0].lower())
        age.append(row[1])
        salary.append(row[2])

print(country)
print(age)
print(salary)
inputcountry=input('what country?')
if inputcountry.lower() in country :
    inputage=input('what age?')
    if inputage not in age:
        print('Sorry! Invalid age')
    else:
        ageidx=age.index(inputage)
        theSalary=salary[ageidx]
        print('the avg salary of ',inputcountry.lower(),'for the age ',inputage,'is ',theSalary)
else:
    print('invalid country')