#!/usr/bin/python
# -*- coding utf8 -*- 

from multiprocessing import Process
from socket import *

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)
def talk(conn,addr):
    while True:#通讯循环
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break

if __name__ == '__main__':

    while True:#链接循环
        conn,addr=server.accept()
        p=Process(target=talk,args=((conn,addr)))
        p.start()