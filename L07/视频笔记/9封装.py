#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

''''''
'''
封装:保护隐私/隔离复杂度
 
你的钱包多少钱(数据的封装
你的性取向(数据的封装
你撒尿的工具(方法的封装



__ 双下划线进行隐藏  只在定义阶段发生变形
子类定义的不会覆盖父类的
'''

class Foo:
    x=1
    __y=2
    def test(self):
        print('from test')
#print(Foo.x)
#print(Foo.__dict__)
#print(Foo._Foo__y)
class People:
    def __init__(self,name,age,sex):
        self.__name=name
        self.__age=age
        self.__sex=sex
    def tell_info(self):
        print('人的名字是:%s,人的行吧是:%s,人的年龄是%s'%(
            self.__name,
            self.__sex,
            self.__age
        ))

p=People('xp',18,'male')
print(People.__dict__)
p.tell_info()

#只在定义阶段 定义完成后不发生变形
p.__salary=3000
print(p.__dict__)
#执行结果{'_People__name': 'xp', '_People__age': 18, '_People__sex': 'male', '__salary': 3000}

People.__n=1111
print(People.__dict__) #运行结果包含, '__n': 111  同样未发生变形
print(People.__n)