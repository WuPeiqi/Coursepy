#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from socket import *
from threading import Thread

# s=socket(AF_INET,SOCK_STREAM)
# s.bind(('127.0.0.1',8080))
# s.listen(5)

# while True:
#     conn,addr=s.accept()
#
#     while True:
#         res=conn.recv(1024)
#         print('client %s%s msg %s'%(addr[0],addr[1],res))
#         conn.send(res.upper())

def server(ip,port):

    s=socket(AF_INET,SOCK_STREAM)
    s.bind((ip,port))
    s.listen(5)


    while True:
        conn, addr = s.accept()
        print('client: ',conn,addr)
        t=Thread(target=talk,args=(conn,addr))
        t.start()

def talk(conn,addr):
    try:
        while True:
            res = conn.recv(1024)
            if not res:break
            print('client %s%s msg %s' % (addr[0], addr[1], res))
            conn.send(res.upper())
    except  Exception:
        pass
    finally:
        conn.close()

if __name__ == '__main__':
    server('127.0.0.1',8080)