#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from multiprocessing import Process,Queue
from multiprocessing import JoinableQueue
import time
import random

# def consumer(q,name):
#     while True:
#         time.sleep(random.randint(1,3))
#         res=q.get()
#         print('消费者%s拿到了%s'%(name,res))
#
# def producer(seq,q,name):
#     for item in seq:
#         time.sleep(random.randint(1,3))
#         q.put(item)
#         print('\033[42m生产者%s生产了%s\033[0m' %(name,item))
# if __name__ == '__main__':
#     q=Queue()
#     c=Process(target=consumer,args=(q,'xp'),)
#     c.start()
#
#
#     seq=['包子%s'%i for i in range(10)]
#     producer(seq,q,'厨师1')
#     print('主进程')

# '''最后发一个空字符,解决死循环问题'''
# def consumer(q,name):
#     while True:
#         time.sleep(random.randint(1,3))
#         res=q.get()
#         if res is None:break
#         print('消费者%s拿到了%s'%(name,res))
#
# def producer(seq,q,name):
#     for item in seq:
#         time.sleep(random.randint(1,3))
#         q.put(item)
#         print('\033[42m生产者%s生产了%s\033[0m' %(name,item))
#     q.put(None)
# if __name__ == '__main__':
#     q=Queue()
#     c=Process(target=consumer,args=(q,'xp'),)
#     c.start()
#
#
#     seq=['包子%s'%i for i in range(10)]
#     #producer(seq,q,'厨师1')
#     p=Process(target=producer,args=((seq,q,'xingpu')))
#     p.start()
#     print('主进程')



'''
q.join()
join等待收到全部task_done回应
q.task_done()



主进程等待生产者结束 p.join
生产者等待消费者取完数据结束,一旦取完就不再阻塞
消费者c.daemon 主进程完毕即回收,消费者已无存在必要
'''
def consumer(q,name):
    while True:
        #time.sleep(random.randint(1,3))
        res=q.get()
        q.task_done()
        print('消费者%s拿到了%s'%(name,res))

def producer(seq,q,name):
    for item in seq:
        #time.sleep(random.randint(1,3))
        q.put(item)
        print('\033[42m生产者%s生产了%s\033[0m' %(name,item))
    q.join()
    print('===========>:')
if __name__ == '__main__':
    q=Queue()
    q=JoinableQueue()           #JoinableQueque可以确认是否取完
    c=Process(target=consumer,args=(q,'xp'),)
    c.daemon=True
    c.start()


    seq=['包子%s'%i for i in range(10)]
    #producer(seq,q,'厨师1')
    p=Process(target=producer,args=((seq,q,'xingpu')))
    p.start()
    p.join()
    #c.join()
    print('主进程')


