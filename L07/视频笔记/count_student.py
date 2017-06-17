#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731
count=1000
class Foo:
    count=0
    def __init__(self,name):
        self.name=name
        #count + =1 全局
        #self.count=0 对象自己的
        Foo.count+=1

        global count
        count+=1
obj1=Foo('x')
obj2=Foo('xx')

print(Foo.count)
print(obj1.count)
print(obj2.count)
print(count)