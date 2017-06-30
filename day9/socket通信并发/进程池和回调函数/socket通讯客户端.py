#!/usr/bin/python
# -*- coding utf8 -*- 

from multiprocessing import Process
from socket import *
client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))
while True:
    msg=input('msg: ').strip()
    if not msg:continue
    client.send(msg.encode('utf-8'))
    msg2=client.recv(1024)
    print(msg2.decode('utf-8'))