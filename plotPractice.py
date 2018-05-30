# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:36:02 2018

@author: 212634012
"""
import matplotlib.pyplot as plt
import pandas as pd
data=[[1,3],[1,2.9],[1,3.1],[1,2.8],[1.1,3],[1.1,2.9],[1.1,3.1],[1.1,2.8],[2,5],[3,9],[7,2],[4,6]]
dataFrame=pd.DataFrame(data,columns=['colx','coly'])
print(dataFrame.head())
dataFrame.plot(kind='scatter',x='colx',y='coly',alpha=0.1,s=dataFrame['colx']*100)
#print(dataFrame['colx']/10)
#plt.show()
