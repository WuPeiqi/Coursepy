#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731
''''''

#判断是子类
# class Foo:
#     pass
# class Bar(Foo):
#     pass
# print(issubclass(Bar,Foo))


'''
 .的方式调用属性  或者用字符串的方式去字典里取

'''
class People:
    country='China'
    def __init__(self,name,age):
        self.name=name
        self.age=age

print(People.country)   #People.__ditc__['country']  真实的调用过程

p=People('egon',18)
print(p.name) #p.__dict__['name']

hasattr(p,'name')  #字符串取
print(hasattr(People,'country'))  #判断是否有

p.x=1
print(p.__dict__)  #执行结果{'name': 'egon', 'age': 18, 'x': 1}
print(p.x)

setattr(p,'y',300) #设置值

#获取值
print(getattr(p,'z','not exist'))
print(getattr(p,'y','not exist'))

#或者判断后取值
if hasattr(p,'x'):
    res=getattr(p,'x')
    print(res)

#删除
print(People.country)
delattr(People,'country')

#获取文件名
import sys
m=sys.modules[__name__]
print(m)

if hasattr(m,'People'):
    res=getattr(m,'People')
    print(res)
    obj=res('hsingpu',189)
    print(obj.name)

'''
反射 通过字符串取取值

hasattr判断
setattr
getattr
delattr

'''

