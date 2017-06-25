#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

'''
模块: 一个模块就是包含了py定义和声明的文件  文件名就是模块名加上py后缀
为什么要使用模块:


导入模块做的事情
1.产生新的名称空间
2.以新建的名称空间为全局名称空间.执行文件的代码
3.拿到一个模块名 指向spam.py
'''
import spam
money=1999
print(spam.money)  #获取的是spam的money值
print(spam.s1)
spam.s1()

#别名  也可以,号导入多个
import os,time
import spam as x
print(x.money)

#不加前缀直接使用 from  *** import ***
'''
1.产生新的名称空间
2.以新建的名称空间为全局名称空间.执行文件的代码
3.直接拿到spam.py产生的名称空间中的名字

优点:方便直接调用  不用加前缀
缺点:容易跟当前的名称空间冲突
'''

from spam import money,s1
print(money)
s1()

#本地定义会覆盖  del money也无法调用到原来导入的money
money=10
print(money)
time.sleep(20)




