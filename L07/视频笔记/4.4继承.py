#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

class Parent:
    def foo(self):
        print('from Parent.foo')
        self.bar()
    def bar(self):
        print('From parent.bar')

class Sub(Parent):
    def __init__(self):
        pass
        #self.bar=123 报错可以看出优先调用了自己的
    def bar(self):
        print('From Sub.bar')
s=Sub()
s.foo()
'''
执行结果
from Parent.foo
From Sub.bar
'''

#是否是示例 结果都为True
print(isinstance(s,Sub))
print(isinstance(s,Parent))

#继承反映的是一种什么是什么的关系
#--------------------------------------------------------------
#组合可以解决代码冗余问题  但是组合反映的是什么有什么的关系

class Date:
    def __init__(self,year,mon,day):
        self.year=year
        self.mon=mon
        self.day=day
    def tell(self):
        print('%s-%s-%s'%(self.year,self.mon,self.day))

class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

class Teacher(People):
    def __init__(self,name,age,sex,salary,year,mon,day):
        People.__init__(self,name,age,sex)
        self.salary=salary
        self.birth=Date(year,mon,day)           #类的组合  老师有生日
class Student(People):
    def __init__(self,name,age,sex,year,mon,day):
        People.__init__(self,name,age,sex)
        self.birth=Date(year,age,sex)

t=Teacher('eg',18,'male',3000,1954,12,21)
t.birth.tell()