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

        print('connecting...')

    # @staticmethod
    # def from_conf():
    #     return MySQL(settings.Host,settings.Port)   #MySQL(127.0.0.1 3306)

    '''用classmethod定义 子类调用即是调用子类的方法.因为是传入第一个参数为子类.是由子类实例化的效果'''
    @classmethod
    def from_conf(cls):
        return cls(settings.Host,settings.Port)   #MySQL(127.0.0.1 3306)
    def __str__(self):
        return '父类'

class Mariadb(MySQL):
    pass
    def __str__(self):
        #return '子类'        #最后一步更改子类的返回值 获取到有用信息
        return "host:%s port:%s"%(self.host,self.port)

conn2=MySQL.from_conf()
#print(conn2.host)
conn3=Mariadb.from_conf()
print(conn3)