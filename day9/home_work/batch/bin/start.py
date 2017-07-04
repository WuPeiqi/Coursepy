#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import paramiko
import configparser
from multiprocessing import Pool,Process

conffile='a.ini'

config=configparser.ConfigParser()
config.read(conffile)
#print(config.sections()) #标题
#print(config.options('global')) #key
#print(config.items('group'))#key value
#print(config.get('h1','ip'))  #标题下 键对应的值

def info_init(hostname):
    ip=config.get(hostname,'ip')
    port=config.get(hostname,'port')
    user=config.get(hostname,'user')
    passwd=config.get(hostname,'passwd')
    print('%s host_info'%(hostname),ip,port,user,passwd)
    return ip,port,user,passwd

def ssh_conn(login,command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(login[0],int(login[1]),login[2],login[3])
    stdin,stdout,stderr = ssh.exec_command(command)
    print(stdout.read().decode('utf-8'))
    ssh.close()

class ftp_conn():
    def __init__(self):
        pass
    def ftp_put(self):
        t=paramiko.Transport(('172.21.120.247',41022,))
        t.connect(username='dev',password='imsa1qaz@WSX')
        sftp=paramiko.SFTPClient.from_transport(t)
        #sftp.put('')
        sftp.close()
    def ftp_get(self):
        pass
if __name__ == '__main__':
    #info_init('h1')        测试可以正常读取到主机名对应的信息,下面使用回调函数
    # pool=Pool()
    # p
    # res=info_init('h1')
    # print(type(res))
    # print(res[1])
    hostname=input('请输入主机名')
    command=input('请输入执行的命令')
    ssh_conn(info_init(hostname),command)