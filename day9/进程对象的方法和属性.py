#!/usr/bin/python
# -*- coding utf8 -*- 

from multiprocessing import Process
import time
import random
def piao(name):
    print('%s is piao '%name)
    time.sleep(random.randint(1,3))
    print('%s is piao'%name)
if __name__ == '__main__':
    p1=Process(target=piao,args=('egon',),name='<p1>')
    p2 = Process(target=piao, args=('xp',), name='<p1>')
    p1.daemon=True
    p1.start()

    p1.terminate()#杀死进程
    time.sleep(1)
    print(p1.is_alive())
    p1.join()
    print('主进程')
    #print(p1.name)     #进程名
    #print(p1.pid)      #进程pid
