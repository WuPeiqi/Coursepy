#!/usr/bin/python
# -*- coding utf8 -*- 

from multiprocessing import Process,Pool
from socket import *
import os

server=socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)
def talk(conn,addr):
    print(os.getpid())
    while True:#通讯循环
        try:
            msg=conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break

if __name__ == '__main__':
    pool=Pool()
    res_l=[]
    while True:#链接循环

        conn,addr=server.accept()
        print(addr)
        #pool.apply(talk,args=((conn,addr)))    #同步
        res=pool.apply_async(talk, args=((conn, addr)))
        res_l.append(res)

        # p=Process(target=talk,args=((conn,addr)))
        #p.start()