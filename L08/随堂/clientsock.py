#!/usr/bin/python
# -*- coding utf8 -*- 

import socket
phone=socket.socket(socket.AF_INET,srocket.SOCK_STREAM)
phone.connect(('127.0.0.1',8081))
while True:
    msg=input('>>:').strip()
    if not msg:continue#防止用户空消息
    phone.send(msg.encode('utf-8'))
    back_msg=phone.recv(1024)
    print(back_msg.decode('utf-8'))
phone.close()