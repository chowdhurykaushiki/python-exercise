# -*- coding: utf-8 -*-
"""
Created on Fri May  4 09:43:38 2018

@author: 212634012
"""
#base class
class rocket():
    def __init__(self,name,distance):
        self.rocketName=name
        self.rocketDist=distance
        name=name
    
    def launch(self):
        print("%s has reached %s" % (self.rocketName,self.rocketDist))
        print(self.rocketName,"has reached ",self.rocketDist)
        return "%s has reached %s" % (self.rocketName,self.rocketDist)

#inherited class 
class marsRover(rocket):
    def __init__(self,name,distance,maker):
        rocket.__init__(self,name,distance)
        # or 
        #super().__init__(name,distance)
        self.marsMaker=maker
    
    def maker(self):
        return "% was made by %" % (rocket.rocketName,self.maker)
    def launch(self):
        print("this is launch of subclass")

if __name__=="__main__":
    marsRover=marsRover("mars_rover2", "till Mars", "ISRO")
    marsRover.launch();
