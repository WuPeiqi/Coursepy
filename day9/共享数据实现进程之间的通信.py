#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from multiprocessing import Manager,Process
import os

def work(d,l):
    #print(os.getpid())
    l.append(os.getpid())
    d[os.getpid()]=os.getpid()
if __name__ == '__main__':
    m=Manager()
    l=m.list(['init',])
    d=m.dict({'name':'egon'})

    p_l=[]
    for i in range(5):
        p=Process(target=work,args=(d,l))
        p.start()
        p_l.append(p)
    for p in p_l:
        p.join()
    print(d,'&',l)