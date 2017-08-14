#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:xp
# blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from multiprocessing import Manager, Process, Lock


def work(d, mutex):
    with mutex:
        d['count'] -= 1
    # mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    m = Manager()
    d = m.dict({'count': 100})
    p_l = []
    for i in range(100):
        p = Process(target=work, args=(d,mutex))
        p_l.append(p)
        p.start()

    for p in p_l:
        p.join()
    print('主线程:', d)
