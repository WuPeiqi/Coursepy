#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#property
''''''
'''
封装的示例: 
'''
class Foo:
    @property
    def test(self):
        print('from foo')
    #test=property(test)
f=Foo()
f.test   #调用属性

#BMI体质指数  计算公式:...
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    def bmi(self):
        return self.weight/(self.height*2)
p=People('xp',65,1.80)
#print(p.bmi())
#--------------------------------------
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight/(self.height*2)
p=People('xp',65,1.80)
print(p.bmi)

'''示例 计算圆形的周长'''

import math
class Circle:
    def __init__(self,radius): #圆的半径
        self.radius=radius
    @property
    def perimeter(self):
        return 2*math.pi*self.radius
c=Circle(10)
print(c.perimeter)