#!/usr/bin/python
# -*- coding utf8 -*- 

from threading import Timer

def hello(name):
    print('%s say hello, world' %name)

t=Timer(3,hello,args=('egon',))
t.start()

