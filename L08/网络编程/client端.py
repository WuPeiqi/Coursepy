#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #等同于服务端
phone.connect(('127.0.0.1',8080))     #拨通电话 注意此处是一个元组的形式
phone.send('hello'.encode('utf-8'))  #转为二进制发出去
print('ready to recv message')
back_msg=phone.recv(1024)        #接收消息
print(back_msg)
phone.close()