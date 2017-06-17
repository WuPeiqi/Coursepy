#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731


#父类中  __定义的方法可以在父类中调用,不可以继承
class Foo1:
    def foo(self):
        print('from parent foo')
        self.__test()
    def __test(self):
        print('from foo.test')

class Bar(Foo1):
    def test(self):
        #Foo1.test()
        #super(Bar,self).test() #python2的用法  在Python3中这2个参数可以省略
        print('Bar')
b=Bar()
b.test()

#模块级别的隐藏  单下划线