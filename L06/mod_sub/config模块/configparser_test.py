#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import configparser
config=configparser.ConfigParser()
config.read('a.ini')

print(config.sections())
print(config.options('section1'))
print(config.items('section1'))
'''
执行结果
['section1', 'section2']
['k1', 'v1', 'user', 'is_admin', 'salary']
[('k1', 'k1'), ('v1', 'v1'), ('user', 'xp'), ('is_admin', 'True'), ('salary', '31')]
'''

#获取值 整型 浮点 布尔(0,1,True,False)等
res=config.get('section1','db')
print(res,type(res))
res=config.getint('section1','SALARY')
print(res)

'''
config.remove_section('section1')
config.remove_option('section1','k1')

判断是否存在
config.has_option('section1','k1')
config.remove_option('section1',k1)
'''
print(config.has_option('section1','k1'))
print(config.remove_option('section1','k1'))

#写入
config.write(open('a.cfg','w'))

#添加一个标题
config.add_section('xp')
config.set('xp','name','winxp')
config.set('xp','age','xp') #必须是字符串

#