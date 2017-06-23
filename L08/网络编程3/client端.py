#!/usr/bin/env python
# -*- coding:utf-8 -*-
''''''
'''
1.使用while True 实现客户端服务端循环通信
2.if not msg:continue  判断是否有消息 防止空消息问题

'''
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #等同于服务端
phone.connect(('127.0.0.1',8080))     #拨通电话 注意此处是一个元组的形式
while True:
    cmd=input('>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))  #转为二进制发出去
    print('ready to recv message')
    cmd_msg=phone.recv(1024)        #接收消息
    print(cmd_msg.decode('gbk'))
phone.close()