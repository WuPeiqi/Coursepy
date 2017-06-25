#!/usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *

tcp_client=socket(AF_INET,SOCK_STREAM)
tcp_client.connect(('127.0.0.1',8080))

tcp_client.send('hello'.encode('utf-8'))
tcp_client.send('hello'.encode('utf-8'))
tcp_client.send('hello'.encode('utf-8'))
