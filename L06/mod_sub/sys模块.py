#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import sys,time

print(sys.argv)  #获取命令执行的结果 可以获取到传入的参数  比如在命令行执行 pyton  /usr/share/test.py -h 192.148.1.1 -p 412
print(sys.argv[0])

'''模拟进度条,需要命令行执行'''

for i in range(50):
    sys.stdout.write('%s\r'%('#'*i))   #\r跳到行首
    sys.stdout.flush()
    time.sleep(0.1)
