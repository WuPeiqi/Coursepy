#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

class Chinese:
    country='China'
    def __init__(self,name,age):
        print('========>')
        self.name=name
        self.age=age
    def talk(self):
        print('say chinese',self)
'''类的用途  实例化  属性引用'''
p1=Chinese('xp',18)  #实例化触发__init__方法
print(Chinese.country)  #类的数据属性
print(Chinese.__init__) #类的函数属性


print(Chinese.__dict__) #类的名称空间 或者类的属性字典
print(Chinese.__dict__['country'])
print(p1.name)
print(p1.age)


'''
类有数据属性  函数属性
对象只存数据属性   {'name': 'xp', 'age': 18}'''
print(p1.__dict__)

'''
类型与类是统一的
'''
print(type(p1))

p1=Chinese('xp',18)
p2=Chinese('egon',1000)
print(p1.country)
print(p2.country)

#以下值一样
print(id(p1.country))
print(id(p2.country))
print(id(Chinese.country))

#绑定到对象身上  绑定到谁身上就给谁用的  谁来调用就会把自己当做第一个参数传入
print(Chinese.talk)
print(p1.talk)
print(p2.talk)
p1.talk()

