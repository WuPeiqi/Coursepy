#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):  #默认触发
        print('run __str__')
        return 'name:%s age:%s'%(self.name,self.age)
p=People('egon',189)
print(p)


