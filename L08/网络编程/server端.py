#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import socket

'''
模拟打电话的沟通方式
'''

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #理解为买电话.基于ipv4 基于流式协议tcp   SOCK_DGRAM udp协议
phone.bind(('127.0.0.1',8080))   #插卡
phone.listen(5) #开机  此处参数是指backlog 半连接池 下一篇博客解释
print('staring...')
conn,addr=phone.accept()#等待电话接通     conn建好的连接  addr客户端地址
print(conn,'client addr',addr)

client_msg=conn.recv(1024)    #开始接收消息  此处先使用1024 每次接收的大小
print('client msg : %s' % client_msg)
conn.send(client_msg.upper())  #将收到的消息回发回去
conn.close()    #关闭连接
phone.close()   #关闭手机

