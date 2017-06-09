#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731


# #类是变量和函数的结合体
# class Chinese:
#     print('==>')#定义时候会立即执行
#     country='China'
#     def __init__(self,name,age,sex):  #self实例化的对象作为第一个参数
#         self.Name=name
#         self.Age=age
#         self.Sex=sex
#     def talk(self):
#         print('talking' ,self)
#
# #类的使用方法  属性  和  实例化
#
# #属性
# print(Chinese.country)
#
# Chinese.talk('a')
# Chinese.x=1  #往类的名称空间里加一个变量
#
# #实例化  调用类其实就是调用类下面的init方法
# p=Chinese('xp','18','male')
# #p2=Chinese()
# print(p.Name)
# print(p.country)
# #p2.country
#
# #self 传入自己
# p.talk()
# #Chinese.talk() 报错

#-----------------------更新-------------------------------

#类是变量和函数的结合体
class Chinese:
    print('==>')#定义时候会立即执行
    country='China'
    def __init__(self,name,age,sex):  #self实例化的对象作为第一个参数
        self.Name=name
        self.Age=age
        self.Sex=sex
    def talk(self):
        print('%s is talking' % self.Name)

p=Chinese('xp','18','male')

p.talk()#输出结果  xp is talking

