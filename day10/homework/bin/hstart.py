#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from ftplib import FTP

def ftp_(ip,port):
    ftp=FTP()
    ftp.connect(ip,port)
