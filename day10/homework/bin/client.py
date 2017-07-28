#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from socket import *

cod='utf-8'
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8080))

while True:
    msg=input('>>').strip()
    if not msg:continue
    c.send(msg.encode(cod))
    res=c.recv(1024)
    print(res.decode(cod))
