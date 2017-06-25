#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#导入全部
from spam import *
#s2()
#s1()
from spam import *

'''
import只执行一次   优先从内容 --->内置--->sys.path中找
'''


'''不在同一路径  可以sys.path.insert追加路径信息'''
import sys,os
print(sys.path)
s1=os.system('cd')
sys.path.insert(0,r'D:\code\py\py3\Coursepy\L05\a')
print(sys.path)
import sp1



