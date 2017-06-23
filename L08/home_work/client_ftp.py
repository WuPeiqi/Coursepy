#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import socket,struct,json,os
class MyClient:
    address_family=socket.AF_INET
    socket_type=socket.SOCK_STREAM
    allow_reuse_address=False
    coding='utf-8'
    allow_queue_size = 5  ####?   监听地址池 尚未细讲解
    #server_dir = 'file_upload'  ####?
    def __init__(self,server_address,connect=True):
        self.server_address=server_address
        self.socket=socket.socket(self.address_family,
                                  self.socket_type)
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise   #raise和break是如何区别的
    def client_connect(self):
        self.socket.connect(self.server_address)
    def client_close(self):
        self.socket.close()
    def run(self):
        while True:
            cmd=input('>>:').strip()
            if not cmd:continue
            self.send(cmd.encode(self.coding))
            head_struct=self.recv(4)
            head_len=struct.unpack('i',head_struct)[0]
            head_bytes=self.recv(head_len)
            head_json=head_bytes.decode('utf-8')
            head_dic=json.loads(head_json)
