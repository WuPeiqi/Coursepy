#!/usr/bin/python
# -*- coding utf8 -*- 

from threading import Thread

msg_l=[]
format_l=[]

def talk():
    while True:
        msg=input('>>>: ').strip()
        if not msg:continue
        msg_l.append(msg)

def format():
    while True:
        if msg_l:
            res=msg_l.pop()
            res=res.upper()
            format_l.append(res)

def save():
    while True:
        if format_l:
            res=format_l.pop()
            with open('a.txt','a',encoding='utf-8') as f:
                f.write('%s\n' %res)

if __name__ == '__main__':
    t1=Thread(target=talk())
    t2 = Thread(target=format())
    t3 = Thread(target=save())
    t1.start()
    t2.start()
    t3.start()