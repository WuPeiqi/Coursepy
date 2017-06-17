#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import abc

class Interface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass

    def write(self):
        raise TypeError('类型错误')

class Txt(Interface):
    def read(self):
        print('文本文件的读取方法')
    def write(self):
        print('文本文件的写方法')
class Sata(Interface):
    def read(self):
        print('硬盘读取的方法')
    def write(self):
        print('硬盘的写方法')
class Process(Interface):
    pass

t=Txt()
p=Process()
d=Sata()
print(isinstance(t,Interface))
print(isinstance(p,Interface))
t.read()
p.read()

#实例化报错  必须定义父类里面的方法
#twisted可以实现java的接口