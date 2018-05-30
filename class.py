# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:19:49 2018

@author: 212634012
"""

class pen:
    pen_model = 'cello'
    def change_model(self,new_model):
        self.pen_model=new_model
        pen_model=new_model
        return(pen_model)
class car:
    def __init__(self,model):
        self.carModel=model
    def changeCarModel(self,newModel):
        self.carModel=newModel  

if __name__=="__main__" :
    pen = pen()
    print('================================')
    print(pen.pen_model)
    pen.change_model('Marker')
    print(pen.change_model('Marker'))
    print(pen.pen_model)
    print('================================')
    car=car('HondaCity')
    print(car.carModel)
    car.changeCarModel('Tiago')
    print(car.carModel)
    print('================================')
    