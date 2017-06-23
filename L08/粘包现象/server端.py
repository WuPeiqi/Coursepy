#!/usr/bin/env python
# -*- coding:utf-8 -*-


''''''
'''
粘包有2种现在
1.是在客户端粘包
2.
'''
from socket import *

tcp_server=socket(AF_INET,SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
tcp_server.bind(('127.0.0.1',8080))
tcp_server.listen(5)

conn,addr=tcp_server.accept()

res=conn.recv(1000)
#res=conn.recv(1)
#res=conn.recv(1)
#res=conn.recv(1)
print(res)