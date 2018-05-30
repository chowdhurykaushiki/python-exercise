# -*- coding: utf-8 -*-
"""
Given two .txt files that have lists of numbers in them, 
find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, 
and the other .txt file has a list of happy numbers up to 1000.
"""
class common:
    fList=[]
    def fileToList(self,fileName):
        with open(fileName) as f:
          fileTxt=f.read()
        fList=fileTxt.split('\n')
        return fList
    
if __name__=="__main__":
    commonObj=common()
    HappyList=commonObj.fileToList('happy.txt')
    PrimeList=commonObj.fileToList('prime.txt')
    print(HappyList)
    print(PrimeList)
    commonList=[x for x in HappyList if x in PrimeList]
    print(commonList)
    with open("common.txt",'w') as f:
        for x in commonList:
            f.write(x+'\n')
    

