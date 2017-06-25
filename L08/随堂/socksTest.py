#!/usr/bin/python
# -*- coding utf8 -*- 

import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.bind(('127.0.0.1',8081))
phone.listen(5) #backlog
while True:
    print('starting ...')
    conn,addr=phone.accept()
    print('client addr',conn,addr)
    while True:
        client_msg=conn.recv(1024)
        if not client_msg:break
        print('client msg:%s'%client_msg)
        conn.send(client_msg.upper())
    conn.close()
phone.close()