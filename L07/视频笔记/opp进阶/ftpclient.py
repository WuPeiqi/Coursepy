#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731


class FtpClient:
    def __init__(self,addr):
        print('正在连接服务器%s'%addr)
        self.addr=addr

    def get(self,arg):
        print('下载中%s'%arg)






    def run(self):
        while True:
            inp=input('==>').strip()
            inp=inp.split()
            if hasattr(self,inp[0]):
                func=getattr(self,inp[0])
                func(inp[1])

down1=FtpClient('192.168.1.1')
#down1.run()   执行测试  输入get a.txt即可



#补充说明 导入字符串格式的模块名方法
#1.__import_-
m=__import__('sys')
print(m.path)
#2.方法二 使用impotlib
import importlib
m=importlib.import_module('sys')
print(m)