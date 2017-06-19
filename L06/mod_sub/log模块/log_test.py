#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import logging    #%name并不是文件名日志名等


#           时间格式       name    日志级别     模块名     日志信息
#           时间              上下午
#      日志的级别
logging.basicConfig(
    #filename='access.log',  #日志写入到文件
    format='%(asctime)s - %(name)s-%(levelname)s-%(module)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    level=10
    #level=logging.FATAL #设置级别   可以使用文字和数字
)

'''
CRITICAL=10
FATAL=CRITICAL
ERROR-40
WARNING=30
WARN=WARNING
INFO=20
DEBUG=20
NOTSET=0
'''

print(logging.DEBUG)
#loging.DEBUG 大写是设置
logging.debug('DEBUG')
logging.info('INFO')
logging.warn('war')
logging.error('err')
logging.critical('cr')
