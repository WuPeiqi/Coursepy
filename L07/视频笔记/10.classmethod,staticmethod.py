#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731



''''''
'''默认绑定到对象



1.绑定方法:(绑定给谁,谁来调用就自动将它本身当作第一个参数传入)
    绑定到类 classmethod
    (其实对象仍可以调用,但是仍将类当作第一个参数传入)
    绑定到对象: 默认
    自动将对象当作第一个参数传入
2.非绑定方法:用staticmethod
    不与类和对象绑定.类和对象都可以调用.没有自动传值

'''



class Foo:
    def test1(self):
        print('test1',self)
    def test2(self):
        print('test2',self)
    def test3():
        print('test3')
f=Foo()
f.test1()
f.test2()
#f.test3()报错  需要0个参数 但是给了1个
class Foo:
    @classmethod
    def test(cls):
        print(cls)
f=Foo()
Foo.test()#类直接调用

print('--------分隔符-------------')

class Foo:
    @staticmethod
    def test(x,y):
        print('test1,',x,y)
f=Foo()

#类和对象都可以调用
f.test(3,4)
Foo.test(1,2)

#=====================================
print('----------分割线----------------')

import settings
class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        print('connecting...')
    @classmethod
    def from_conf(cls):
        return cls(settings.Host,settings.Port)   #MySQL(127.0.0.1 3306)
    def select(self):
        print('select function',self)
conn=MySQL('192.168.1.1',3306)
#conn.select()

#调用类绑定的方法
conn2=MySQL.from_conf()
#print(conn2.select())
