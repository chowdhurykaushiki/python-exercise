# -*- coding: utf-8 -*-


#when number of parameters to be passed are not fixed, then we can pass the 
#...arguments as a tuple
def noFixedParam(*params):
    print(params)

noFixedParam(1,'ad',2.355)
noFixedParam(45,13,78,23,456)

#when we want to pass dictionary as arguments
def dictParams(**dictparam):
    print(dictparam)
    
dictParams(x=1,y=2,z=3)

# .join method on parameter obj
def sepFunc(*params,separater='1'):
    print(separater.join(params))

sepFunc('a','b','c')


def func(n):
    return n

num=func(4)
print(func)


