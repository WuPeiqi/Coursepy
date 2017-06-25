#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import socket
import struct
import json
import subprocess
import os
import time

class MYTCPServer:
    address_family=socket.AF_INET  #ipv4
    socket_type = socket.SOCK_STREAM #tcp协议
    allow_reuse_address=False   ###?    ip复用
    max_packet_size=8192    #?????  此变量为使用
    coding='utf-8'
    allow_queue_size=5  ####?   监听地址池 尚未细讲解
    server_dir='file_upload'####?
    def __init__(self,server_address,bind_and_active=True):
        self.server_address=server_address
        self.socket=socket.socket(self.address_family,self.socket_type)
        if bind_and_active:
            try:
                self.server_bind()
                self.server_active()
            except:
                self.server_close()
                raise
    def server_bind(self):
        #pass
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.socket.bind(self.server_address)
        #print(self.server_address,type(self.server_address))
        #self.server_address=self.socket.getsockname()
        #print(self.server_address,type(self.server_address))
    def server_active(self):
        #elf.socket.listen(self.req)
        self.socket.listen(self.allow_queue_size)
        #pass

    def server_close(self):
        self.socket.close()

    #def server_listen(self):

        #pass

    def get_request(self):
        return self.socket.accept()
    def close_request(self,request):
        request.close()

    def run1(self):
        #pass
        while True:
            self.conn,self.addr=self.get_request()
            while True:
                try:
                    head_struct=self.conn.recv(4)
                    if not head_struct:break
                    head_len=struct.unpack('i',head_struct)[0]
                    print(head_len)
                    head_bytes=self.conn.recv(head_len)
                    head_json=head_bytes.decode(self.coding)
                    head_dic=json.loads(head_json)
                    cmd=head_dic['cmd']
                    #if not cmd:

                    if hasattr(self,cmd):
                        func=getattr(self,cmd)
                        print(func,head_dic)
                        func(head_dic)
                    else:
                        print('未完成')
                except Exception:
                    break

    def put(self,args):
        recv_size=0
        file_path=os.path.normpath(os.path.join(self.server_dir,args['filename']))  #normpath转换标准写法
        file_size=args['filesize']
        print('file_path is:  %s'%file_path)
        with open(file_path,'wb') as f:
            while recv_size < file_size:
                recv_data=self.conn.recv(1024)
                f.write(recv_data)
                recv_size+=len(recv_data)

    def get(self,args):
        pass
    def user_auth(self):
        self.conn,self.addr=self.get_request()
        user_struct=self.conn.recv(4)
        #if not user_struct:break
        auth_dic_len=struct.unpack('i',user_struct)[0]
        head_bytes=self.conn.recv(auth_dic_len)
        user_passwd=head_bytes.decode(self.coding)
        print(user_passwd)
        user_passwd=eval(user_passwd)
        print(user_passwd,type(user_passwd))
        if user_passwd['name']=='dev' and user_passwd['passwd']=='e77989ed21758e78331b20e477fc5582':
            ser2cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            ser2cli.connect(('127.0.0.1',808))
            #bo=struct.pack('i',1)
            bo=bytes('True'.encode(self.coding))
            print(ser2cli)
            time.sleep(0.5)
            print(bo)
            ser2cli.send(bo)
            print('账号密码验证正确')
            #$self.run1()
            return True
        else:
            print('客户端信息未验证通过哦')
mytcps1=MYTCPServer(('127.0.0.1',8080))
if mytcps1.user_auth():
    mytcps1.run1()

    #mytcps1.run1()