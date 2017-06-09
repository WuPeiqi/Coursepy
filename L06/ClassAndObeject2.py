#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#定义类产生类的名称空间  定力对象产生对象的名称空间

class Chinese:
    print('==>')
    country='China'
    city='hb'
    def __init__(self,name,age,sex):
        self.city='bj'
        self.Name=name
        self.Age=age
        self.Sex=sex
    def talk(self):
        print('%s is talking' % self.Name)

print(Chinese.__init__)
print(Chinese.__dict__)  #类级别定义的变量等
#{'__module__': '__main__', 'country': 'China', '__init__': <function Chinese.__init__ at 0x02ED4348>, 'talk': <function Chinese.talk at 0x02ED4300>, '__dict__': <attribute '__dict__' of 'Chinese' objects>, '__weakref__': <attribute '__weakref__' of 'Chinese' objects>, '__doc__': None}


p1=Chinese('xp','18','male')  #触发init方法
print(p1.__dict__)
print(p1.Age)
print(p1.country)
print(p1.city)#优先对象内部

p1.talk()#输出结果  xp is talking



p2=Chinese('w','1','F')
print(p1.country,id(p1.country))
print(p2.country,id(p2.country))

print(Chinese.talk)
print(p1.talk)
print(p2.talk)
'''
执行结果  可以看到各个实例化的对象调用的都是自己的方法,绑定的类的函数(绑定方法 传入自己作为参数)
China 59581088
China 59581088
<function Chinese.talk at 0x038D4300>
<bound method Chinese.talk of <__main__.Chinese object at 0x037CA470>>
<bound method Chinese.talk of <__main__.Chinese object at 0x038D2870>>
'''




