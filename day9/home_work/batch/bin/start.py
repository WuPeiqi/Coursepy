#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import paramiko
import configparser

conffile='a.ini'

config=configparser.ConfigParser()
config.read(conffile)
print(config.sections()) #标题
print(config.options('global')) #key
print(config.items('group'))#key value
print(config.get('h1','ip'))  #标题下 键对应的值

def info_init(hostname):
    ip=''
    port=''
    user=''
    passwd=''
    return ip,port,user,passwd

def ssh_conn(ip,port,user,passwd,command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port,user,passwd)
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
