#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import socket

'''
socket编程1
Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。

所以，我们无需深入理解tcp/udp协议，socket已经为我们封装好了，我们只需要遵循socket的规定去编程，写出的程序自然就是遵循tcp/udp标准的。


也有人将socket说成ip+port，ip是用来标识互联网中的一台主机的位置，而port是用来标识这台机器上的一个应用程序，ip地址是配置到网卡上的，而port是应用程序开启的，ip与port的绑定就标识了互联网中独一无二的一个应用程序

而程序的pid是同一台机器上不同进程或者线程的标识


下面是一个简单的sock网络编程示例
为了便于理解,我们将sock通信按打电话的方式来写

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

