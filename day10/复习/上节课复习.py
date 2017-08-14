#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from multiprocessing import Process

class Work(Process):
    def run(self):
        print('%s say hello '%self.name)

if __name__ == '__main__':
    p=Work()
    p.start()
    # p.terminate()
    # p.is_alive()
    print('主线程')

#
# def work(name):
#     print('%s say hello'%name)
#
#
# if __name__ == '__main__':
#     p=Process(target=work,args=('egon1',))
#     p.daemon=True   #主的挂 子的也挂  守护进程不能再开子进程
#     p.start()
#     p.join()  #等待主
#     print('主线程')
#

