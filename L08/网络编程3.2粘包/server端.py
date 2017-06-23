#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''socket2 进阶'''

'''
接上节内容  处理粘包问题  此处更改了报头,使用了字典
'''

import socket,json
import subprocess,struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #理解为买电话.基于ipv4 基于流式协议tcp   SOCK_DGRAM udp协议
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  #注释5  重用IP地址
phone.bind(('127.0.0.1',8080))   #插卡
phone.listen(5) #开机  此处参数是指backlog 半连接池 下一篇博客解释
while True: #注释3
    conn,addr=phone.accept()#等待电话接通     conn建好的连接  addr客户端地址

    while True: #注释1
        try:    #注释2
            cmd=conn.recv(1024)    #开始接收消息  此处先使用1024 每次接收的大小
            if not cmd:break #注释4
            '''执行命令,获取正确输入和错误输入
            如果有错误输出则输出错误
            否则输出正确解决(此处正确结果为和系统相关的编码格式,此处为gbk)'''
            res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,)
            err=res.stderr.read()
            if err:
                cmd_res=err
            else:
                cmd_res=res.stdout.read()
            #conn.send(struct.pack('i',len(cmd_res)))
            '''改用字典方式'''
            head_dic={'filename':None,'hash':None,'total_size':len(cmd_res)}
            head_json=json.dumps(head_dic)
            head_bytes=head_json.encode('utf-8')
            '''先发送json的报头'''
            conn.send(struct.pack('i',len(head_bytes)))
            conn.send(head_bytes)
            conn.send(cmd_res)
        except ConnectionResetError:    #exception 万能捕获异常
            break
    conn.close()    #关闭连接
phone.close()   #关闭手机

