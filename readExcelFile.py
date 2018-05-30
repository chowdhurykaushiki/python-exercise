# -*- coding: utf-8 -*-
import xlrd
wb = xlrd.open_workbook("C:/KAUSHIKI/Personal/python_exercise/RuleEngine.xlsx")
for sheet in wb.sheets():
    #print(sheet.name)
    for row in range(sheet.nrows):
        if row != 0:
            print(sheet.cell(row,0).value,'and',sheet.cell(row,1).value)
            if sheet.cell(row,0).value == sheet.cell(row,1).value :
                sqVal=sheet.cell(row,1).value**sheet.cell(row,3).value
                print(sqVal)
                fileName = sheet.cell(row,2).value
                with open(fileName,'w') as f:
                    text=str(sheet.cell(row,1).value)+"to the power"+str(sheet.cell(row,3).value)+" is "+str(sqVal);
                    f.write(text)

#read a csv            
with open ("C:/KAUSHIKI/Personal/python_exercise/exampleCSVFile.csv",'r') as f:
    for line in f:
        print(line)

import pandas as pv
file = pv.read_csv("C:/KAUSHIKI/Personal/python_exercise/exampleCSVFile.csv")
print(file)

with open ("C:/KAUSHIKI/Personal/python_exercise/exampleCSVFile.csv",'r') as f:
    listText = f.readlines()
    print(listText)
                   
import unicodecsv as uc
uc.DictReader

            
        