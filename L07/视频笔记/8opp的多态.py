#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731
class Animal:
    pass
class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print('eating')
    def talk(self):
        print('%ssay hello'%self.name)

class Dog:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print('eating')
    def talk(self):
        print('%s汪汪汪'%self.name)

class Pig:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print('eating')
    def talk(self):
        print('%s 哼哼' % self.name)
class Cat(Animal):
    def talk(self):
        print('喵喵喵')
peo1=People('Alex',18,'male')
pig1=Pig('wupeiqi',22,'female')
dog1=Dog('yx',22,'male')
cat1=Cat()

'''
同一种事物的多种形态即为多态
多态的使用:调用相同的函数名,返回不同的值.
'''
def func(obj):
    obj.talk()
# peo1.talk()
# pig1.talk()
# dog1.talk()
func(peo1)
func(pig1)
func(dog1)
func(cat1)