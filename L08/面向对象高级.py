#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731
#
''''''
'''
面向对象高级
__str__ 初始化时使用 必须有返回值
__del__ 析构函数  用途:比如关闭数据库连接时使用

按字典的方式操作对象
__getitem__
__setitem__
__delitem__
'''
# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         #必须有返回值
#         return '<name:%s age:%s>' %(self.name,self.age)
#
# obj=Foo('xp',19)
# print(obj)
#

'''
析构函数
删除对象时执行
'''

# class Foo:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __del__(self):
#         print('del--->')
# obj=Foo('xp',19)
# del obj
# print('==============')
#

class Foo:
    def __init__(self,name):
        self.name=name
    def __getitem__(self,item):
        return self.__dict__[item]
        #print('getitem')
    def __setitem__(self,key,value):
        self.__dict__[key]=value
        #print('setitem',key,value)
        #self[key]=value
    def __delitem__(self,key):
        self.__dict__.pop(key)
        #print('del obj[key]时,我执行')
obj=Foo('xp')
'''原来的操作方法'''
#obj.name='hsingpu'
#print(obj.name)

'''新的操作对象属性方法'''
obj['name']='xingpu'  #触发setitem
print(obj['name'])
print(obj.name)
del obj['name']
print('--------------')
print(obj.__dict__)


#示例 字典内容的修改  此种方法有多余逻辑判断 程序慢 所以使用之前的三个方法  __setitem__ __getitem__ __delitem__
def func(obj,key,value):
    if isinstance(obj,dict):
        obj[key]=value
    else:
        setattr(obj,key,value)
dic={'name':'hsing','age':18}

func(dic,'name','hsingpu')
print(dic)

#字典形式调用
obj=Foo('wu')
print(obj.__dict__)
func(obj,'name','123')
print(obj.__dict__)