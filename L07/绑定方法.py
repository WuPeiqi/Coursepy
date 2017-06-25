#!/usr/bin/python
# -*- coding utf8 -*- 
#绑定到类
# class Foo:
#     @classmethod
#     def test(cls):
#         print(cls)
# f=Foo()
# Foo.test()
# f.test()
#非绑定方法
# class Foo:
#     @staticmethod
#     def test(x,y):
#         print('test',x,y)
# Foo.test(1,3)
# f= Foo()
# f.test(1,222)
#绑定到对象
class Foo:
    def test(self):
        print('test',self)
    def test2(self):
        print('test2',self)
    def test3():
        print('test3')
f=Foo()
f.test()
f.test2()
#f.test3()