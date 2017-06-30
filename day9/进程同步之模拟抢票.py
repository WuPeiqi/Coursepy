#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from multiprocessing import Process,Lock
import time
import random
import json

'''
模拟抢票 会有很多人抢票成功 但是配置文件里只有一张票
配置文件内容 {"count": 1}
'''
# def work(dbfile,name,lock):
#     with open(dbfile,encoding='utf-8') as f:
#         dic=json.loads(f.read())
#
#     if dic['count'] > 0:
#         dic['count'] -= 1
#         time.sleep(random.randint(1,3))#模拟网络延迟
#         with open(dbfile,'w',encoding='utf-8') as f:
#             f.write(json.dumps(dic))
#         print('\033[43m %s 抢票成功 \033[0m' %name)
#     else:
#         print('\033[45m %s抢票失败 \033[0m' % name)
#
# if __name__ == '__main__':
#     lock=Lock()
#     p_l=[]
#     for i in range(100):
#         p1=Process(target=work,args=('a.txt',i,lock))
#         p1.start()
#         p_l.append(p1)
#     for i in p_l:
#         i.join()
#     print('主进程')


'''
使用lock
对指定代码块加锁 防止冲突

'''
def work(dbfile,name,lock):
    lock.acquire()
    with open(dbfile,encoding='utf-8') as f:
        dic=json.loads(f.read())

    if dic['count'] > 0:
        dic['count'] -= 1
        time.sleep(random.randint(1,3))#模拟网络延迟
        with open(dbfile,'w',encoding='utf-8') as f:
            f.write(json.dumps(dic))
        print('\033[43m %s 抢票成功 \033[0m' %name)
    else:
        print('\033[45m %s抢票失败 \033[0m' % name)
    lock.release()
if __name__ == '__main__':
    lock=Lock()
    p_l=[]
    for i in range(100):
        p1=Process(target=work,args=('a.txt',i,lock))
        p1.start()
        p_l.append(p1)
    for i in p_l:
        i.join()
    print('主进程')



'''
上下文管理的方式加锁
使用with lock:
'''
def work(dbfile,name,lock):
    with lock:
        with open(dbfile,encoding='utf-8') as f:
            dic=json.loads(f.read())

        if dic['count'] > 0:
            dic['count'] -= 1
            time.sleep(random.randint(1,3))#模拟网络延迟
            with open(dbfile,'w',encoding='utf-8') as f:
                f.write(json.dumps(dic))
            print('\033[43m %s 抢票成功 \033[0m' %name)
        else:
            print('\033[45m %s抢票失败 \033[0m' % name)

if __name__ == '__main__':
    lock=Lock()
    p_l=[]
    for i in range(100):
        p1=Process(target=work,args=('a.txt',i,lock))
        p1.start()
        p_l.append(p1)
    for i in p_l:
        i.join()
    print('主进程')
