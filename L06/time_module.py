#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import time

print(time.time())  #1970标准时间   时间戳 机器使用
print(time.localtime())
print(time.localtime().tm_year)   #格式化的时间字符串
print(time.gmtime())#结构化时间  标准时间
print(time.strftime('%Y-%m-%d %H:%M:%S' ))
print(time.strftime('%Y-%m-%d %X' ))   #x代表上面的所有

print(time.localtime(1496892865))
print()