#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#多进程共享一套文件系统

# from multiprocessing import Process
# import time,random
#
# def work(filename,msg):
#     with open(filename,'a',encoding='utf-8') as f:
#         f.write(msg)
#
# if __name__ == '__main__':
#
#     for i in range(5):
#         p=Process(target=work,args=('a.txt','进程名%s'%(str(i))))
#         p.start()
# '''写入效果为随机的 可以看出是并发效果 '''

from multiprocessing import Process,Queue
q=Queue(3)
q.put({'a':1})
q.put('b')
q.put(3)
#q.put('d',False)   相同 报错提示已满  full
#q.put_nowait('d')
#q.put('d',timeout=2)    #超时时间

#q.put(4)  内部没有空间或者取空之后会一直等待
print(q.get())
print(q.get())
print(q.get())
# print(q.get(block=False))  #不等待,直接报错
# print(q.get_nowait())
# print(q.get(timeout=2))

q.put('d',False)

#判断空还是满 或者大小
print(q.full())
print(q.empty())
print(q.qsize())

