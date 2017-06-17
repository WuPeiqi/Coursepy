#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731


import settings
import hashlib
import time


class MySQL:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.id=self.create_id()  #调用非绑定的方法 生成ID
        print('connecting...')
    @staticmethod       #创建唯一id  不依赖于类 不依赖于对象
    def create_id():
        # m=hashlib.md5(str(time.time()).encode('utf-8'))
        m = hashlib.md5(str(time.clock()).encode('utf-8'))
        return m.hexdigest()
    @classmethod
    def from_conf(cls):
        return cls(settings.Host,settings.Port)   #MySQL(127.0.0.1 3306)
    def select(self):
        print('select function',self)

conn=MySQL('192.168.1.1',3306)

conn2=MySQL.from_conf()
conn3=MySQL.from_conf()
print(conn2.id)
print(conn3.id)
