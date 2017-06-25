#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''socket2 进阶'''

'''
接上节内容  处理粘包问题
'''


'''
    此处接上节内容 , 扩展支持往服务端发送命令. 并返回执行结果. 模拟xshell的执行方式
'''


'''
1.使用while True 实现客户端服务端循环通信
2.异常捕获处理客户端异常关闭导致的崩溃 , 针对windows系统下
3.再次添加while True 实现循环建立连接
4.客户端无消息断开连接  , 针对linux系统下
5.此处有出现断开占用问题(egon blog)  可以修改内核参数或者在绑定地址之前判断
'''
import socket
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
            conn.send(struct.pack('i',len(cmd_res)))
            conn.send(cmd_res)
        except ConnectionResetError:    #exception 万能捕获异常
            break
    conn.close()    #关闭连接
phone.close()   #关闭手机

