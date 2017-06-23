#!/usr/bin/env python
# -*- coding:utf-8 -*-
''''''
'''
此处接收分段 先接收大小 然后分段接收数据

'''
import socket,struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #等同于服务端
phone.connect(('127.0.0.1',8080))     #拨通电话 注意此处是一个元组的形式
while True:
    cmd=input('>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))  #转为二进制发出去
    print('ready to recv message')
    head=phone.recv(4)
    total_size=struct.unpack('i',head)[0]

    #cmd_msg=phone.recv(total_size)


    recv_size=0
    data=b''
    while recv_size < total_size:
        recv_data=phone.recv(1024)  #进行分段接收 优化数据过大问题
        data+=recv_data
        recv_size+=len(recv_data)


    print(data.decode('gbk'))
phone.close()