#!/usr/bin/python
# -*- coding utf8 -*- 

class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight / (self.height**2)
p=People('xp',65,1.7)
p.height=1.73
#print(p.bmi)

from math import pi
class Roundness:
    def __init__(self,radius):
        self.radius=radius
    @property
    def perimeter(self):
        return self.radius*2*pi
r1=Roundness(1)
print(r1.perimeter)


