# -*- coding: utf-8 -*-
class A:
    def __init__(self):
        self.x = 1
    def printVal(self):
        return "I'm in A"

class B(A):
    def __init__(self, y):
#        super().__init__()
        self.y = y
    def printVal(self, m = None, n = None):
        return "m %s, n %s" % (m,n)
    def printVal(self):
        return "I'm in B"
class C(B):
    def __init__(self,z):
        super().__init__(z)

objC = C(3)
print(objC.printVal(1,2))