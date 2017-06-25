#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

# class Foo:
#     def test(self):
#         print('from foo.test')
# class Bar(Foo):
#     def test(self):
#         Foo.test(self)#调用父类 但是无法更改父类名字
#         print('Bar')
# b=Bar()

class Foo1:
    def test(self):
        print('from foo.test')
class Bar(Foo1):
    def test(self):
        super().test()
        #super(Bar,self).test() #python2的用法  在Python3中这2个参数可以省略
        print('Bar')
b=Bar()
b.test()