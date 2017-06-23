#!/usr/bin/env python
# -*- coding:utf-8 -*-
''''''
'''
此处接收分段 先接收大小 然后分段接收数据

'''
import socket,struct,json
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #等同于服务端
phone.connect(('127.0.0.1',8080))     #拨通电话 注意此处是一个元组的形式
while True:
    cmd=input('>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))  #转为二进制发出去
    print('ready to recv message')

    '''先收报头的长度'''
    head_struct = phone.recv(4)
    head_len = struct.unpack('i',head_struct)[0]
    head_bytes = phone.recv(head_len)
    head_json = head_bytes.decode('utf-8')
    head_dic = json.loads(head_json)
    '''根据报头里的详细信息,取真实的数据'''
    total_size = head_dic['total_size']


    recv_size=0
    data=b''
    while recv_size < total_size:
        recv_data=phone.recv(1024)
        data+=recv_data
        recv_size+=len(recv_data)

    print(data.decode('gbk'))
phone.close()