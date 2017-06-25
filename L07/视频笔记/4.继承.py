#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

''''''
'''
继承是一种创建新类的方式,新建的类可以继承一个或多个父类

父类  又称基类 超类
子类  又名派生类
'''

class ParentClass1:
    pass
class ParentClass2:
    pass
class SubClass1(ParentClass1):
    pass
class SubClass2(ParentClass1,ParentClass2):
    pass
#查看继承的父类
print(SubClass1.__bases__)
print(SubClass2.__bases__)

'''Python2 和Python3  类的区别
2中类分为新式类和经典类
3中都是经典类 默认已经继承了object
'''

#新式类
class Foo(object):
    pass
#经典类  不继承任何内容
class Bar:
    pass
print(Bar.__bases__)



'''寻找继承关系'''
