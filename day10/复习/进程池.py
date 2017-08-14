#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:xp
# blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731


from multiprocessing import Pool
import time, os


def work(n):
    print('%s work' % os.getpid())
    time.sleep(0.5)
    return n ** 2


if __name__ == '__main__':
    p = Pool()
    res_l = []
    for i in range(10):
        # res=p.apply(work,args=(i,))
        obj = p.apply_async(work, args=(i,))  # 不执行,异步提交任务
        res_l.append(obj)
    p.close()
    p.join()
    for obj in res_l:
        print(obj.get())


        # print(res)
#可以使用回调函数 解决耗时问题