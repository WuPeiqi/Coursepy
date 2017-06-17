#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

class People:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def tell_info(self):
        print('人的名字是:%s,人的性别是:%s,人的年龄是: '%(
            self.__name,
            self.__age,
            #self.__sex,
        ))

    def set_info(self,x,y):
        if not isinstance(x,str):
            raise TypeError('名字必须是字符串')
        if not isinstance(y,int):
            raise TypeError('年龄必须是数值型')
        self.__name=x
        self.__age=y

p=People('alex',1000)
p.tell_info()
p.set_info('ax',900)
p.tell_info()