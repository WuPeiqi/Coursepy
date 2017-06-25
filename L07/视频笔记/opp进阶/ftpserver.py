#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import ftpclient
f1=ftpclient.FtpClient('192.168.1.1')

#f1.get()  直接调用报错  对端还没有定义此代码  对端定义后才能正常直接调用
#此处利用反射进行判断
if hasattr(f1,'get'):
    func=getattr(f1,'get')
    func()



print('其他的代码')

