#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

class Animal:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print('eating')
    def talk(self):
        print('%s正在叫' %self.name)



class People(Animal):
    def __init__(self,name,age,sex,education):
        Animal.__init__(self,name,age,sex)      #继承的派生:在子类定义新的属性 覆盖父类的属性
        self.education=education
    def eat(self):
        print('eating')
    def talk(self):                             #函数的继承
        Animal.talk(self)
        print('%ssay hello'%self.name)

class Dog(Animal):
    pass


class Pig(Animal):
    pass

peo1=People('Alex',18,'male','小学')
pig1=Pig('wupeiqi',22,'female')
dog1=Dog('yx',22,'male')

peo1.talk()
#pig1.talk()
dog1.talk()
pig1.talk()
