#!/usr/bin/python
# -*- coding utf8 -*- 
import os
print(os.cpu_count())
from multiprocessing import Process
import time
import random
# def piao(name):
#     print('%s is piaoing'%name)
#     time.sleep(random.randint(1,3))
#     print('%s is piao end'%name)
#
# if __name__ == '__main__':
#     #开启进程
#     #Process(target=piao,args=(),kwargs=())
#     p1=Process(target=piao,args=('egon',),) #元组
#     p1.start()#开子进程
#     print('父进程')
#     '''
# 开进程耗时较长,走的系统调用.程序不等,优先打印出父进程,执行结果:
#     父进程
# egon is piaoing
# egon is piao end
#     '''
def piao(name):
    print('%s is piaoing'%name)
    time.sleep(random.randint(1,3))
    print('%s is piao end'%name)

if __name__ == '__main__':
    #开启进程
    #Process(target=piao,args=(),kwargs=())
    p1=Process(target=piao,args=('egon',),name='P1') #元组
    p1.start()#开子进程
    time.sleep(1)
    print('父进程')
    '''
    执行结果:
egon is piaoing
父进程
egon is piao end
    '''