#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

'''
三种时间
时间戳
本地时间
UTC标准时间
'''
import time
print(time.time())
print(time.localtime())
print(time.localtime().tm_year)
print(time.gmtime())

#格式化输出
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%Y-%m-%d %X'))

#时间转换
#时间戳转当前时间
print(time.localtime(13211123))
print(time.localtime(time.time()))
#结构化时间转时间戳
print(time.mktime(time.localtime()))

#本地转换成格式化时间
print(time.strftime('%Y',time.localtime()))

#字符串转结构化时间
print(time.strptime('2017-06-15 11:22:33','%Y-%m-%d %X'))


#linux style  Thu Jun 15 22:10:09 2017
print(time.asctime())
print(time.ctime(123123122))
print(time.asctime(time.localtime()))