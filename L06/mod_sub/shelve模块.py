#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import shelve
f=shelve.open(r'a.txt')
f['people1']={'name':'eg','age':18}
print(f['people1'])
print(f['people1']['name'])
f.close()
'''
运行结果  会生成三个文件
{'name': 'eg', 'age': 18}
eg

'''