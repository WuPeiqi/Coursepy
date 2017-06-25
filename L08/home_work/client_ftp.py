#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import socket,struct,json,os
import sys
import time
import hashlib
#import server_ftp
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
            inp=input('>>:').strip()
            if not inp:continue
            l=inp.split()
            cmd=l[0]    #截取上传下载命令
            if hasattr(self,cmd):               #???????这里为什么要传入问号
                func=getattr(self,cmd)
                func(l)
                #print(func)
                #print(l)
            #
            #
            # self.send(cmd.encode(self.coding))
            # head_struct=self.recv(4)
            # head_len=struct.unpack('i',head_struct)[0]
            # head_bytes=self.recv(head_len)
            # head_json=head_bytes.decode('utf-8')
            # head_dic=json.loads(head_json)
    def put(self,args):
        cmd=args[0]
        filename=args[1]
        if not os.path.isfile(filename):
            print('文件%s不存在'%filename)
            return                      #不加return继续运行会报错
        else:
            filesize=os.path.getsize(filename)
        head_dic={'cmd':cmd,'filename':os.path.basename(filename),'filesize':filename} #basename获取文件名
        head_json=json.dumps(head_dic)
        head_bytes=bytes(head_json,encoding=self.coding)

        head_struct=struct.pack('i',len(head_bytes))
        self.socket.send(head_struct)
        self.socket.send(head_bytes)
        send_size=0
        with open(filename,'rb') as f:
            for line in f:
                self.socket.send(line)
                send_size+=len(line)
                #print('进度%s'%(send_size/filesize),"\r")
                #already_send=(send_size/filesize)
                sys.stdout.write('#'+'>'+"\b\r")
                time.sleep(0.05)   #文件过小 设置时间可以看到进度条效果
                #print(send_size)
            else:                                       #for循环结束后执行?!
                print('upload success')                 #


    def user_login(self):
        #self.client_connect()
        name=input('用户名: ')
        passwd=input('密码: ')   #此处应该用getpass.getpass
        md5=hashlib.md5()
        md5.update(passwd.encode(self.coding))
        passwd=md5.hexdigest()
        user_info={'name':name,'passwd':passwd}
        print(user_info)
        user_info=str(user_info).encode(self.coding)
        i=struct.pack('i',len(user_info))
        self.socket.send(i)
        self.socket.send(user_info)
    def auth_res(self):
        cli_ser=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        cli_ser.bind(('127.0.0.1',808))
        cli_ser.listen(5)
        cli_conn,cli_addr=cli_ser.accept()
        res=cli_conn.recv(4)
        #res=struct.unpack('i',res)[0]
        print(res)
        res=bool(res.decode(self.coding))
        if res==True:
            print('登陆成功')
            self.run()
        else:
            print('无法成功登陆到服务器')
        cli_conn.close()
        cli_ser.close()
client=MyClient(('127.0.0.1',8080))
client.user_login()
client.auth_res()
#client.run()