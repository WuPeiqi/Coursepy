#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#
class Interface:
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
    def read(self):
        print('进程的读取方法')
    # def write(self):
    #     pass

t=Txt()
p=Process()
d=Sata()
print(isinstance(t,Interface))
print(isinstance(p,Interface))
t.read()
p.read()
#一切皆文件的执行效果

#p.write() 执行会报错  没有定义覆盖掉父类已经定义的方法