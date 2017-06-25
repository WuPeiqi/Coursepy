#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

class Student:
    tag='1111111111 money'
    def __init__(self,ID,name,age):
        self.id=ID
        self.name=name
        self.age=age
    def walk(self):
        print('%s is walking'% self.name)
s1=Student(1,'egon',19)
s2=Student(2,'xp',1000)

print(s1.id)
s1.walk()