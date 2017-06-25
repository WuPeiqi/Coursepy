#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import hashlib

m=hashlib.md5()
m.update('hello world'.encode('utf-8'))
print(m.hexdigest())
#
# with open(r'E:\at.txt','r') as f:
#     f.read()

with open(r'D:\code\py\py3\Coursepy\L06\mod_sub\shutil模块.py','rb') as f:
    for line in f:
        m.update(line)
    md5_num=m.hexdigest()

print(md5_num)

#更多加密方法
m=hashlib.sha256()
m.update('hellwo'.encode('utf-8'))
print(m.hexdigest())

#可以进行抓包匹配


#hmac模块 合成生成加密信息  此方法又名加盐
import hmac
h=hmac.new('eg'.encode('utf8'))
h.update('hello'.encode('utf-8'))
print(h.hexdigest())