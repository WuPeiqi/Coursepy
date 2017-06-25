#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

class People:
    def __init__(self,name):
        self.__name=name

    #@property
    def name(self):
        return self.__name

p=People('xp')

print(p.name())
#---------------------------------------
class People:
    def __init__(self,name):
        self.__name=name

    @property
    def name(self):
        return self.__name

p=People('xp')

print(p.name)

#-----------------------------------------
class People:
    def __init__(self,name,permmission=False):
        self.permmission=permmission
        self.__name=name

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError('类型错误')
        self.__name=value
    @name.deleter
    def name(self):
        if not self.permmission:
            raise PermissionError('禁止操作')
        del self.__name


p=People('xp')
p.permmission=True
print(p.name)
p.name='hsingpu'
del p.name

#封装 提供关键字模拟c++的set get

#print(p.name)

#--------------------------------------------
'''非装饰器写法'''

class People:
    def __init__(self,name,permmission=False):
        self.permmission=permmission
        self.__name=name


    def get_name(self):
        return self.__name

    def set_name(self,value):
        if not isinstance(value,str):
            raise TypeError('类型错误')
        self.__name=value

    def del_name(self):
        if not self.permmission:
            raise PermissionError('禁止操作')
        del self.__name
    name=property(get_name,set_name,del_name)
p2=People('xingpu')
#print(p.get_name)
#print(p.get_name())
p2.permmission=True
print(p2.get_name)
p2.get_name
p2.del_name
p2.get_name
