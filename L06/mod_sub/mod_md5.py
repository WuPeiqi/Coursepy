#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import  hashlib
md5=hashlib.md5()

md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#数据过长 分次运算 结果一样
md5=hashlib.md5()
md5.update('how to use md5 in '.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

