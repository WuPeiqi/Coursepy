#!/usr/bin/python
# -*- coding utf8 -*- 

#开启
from threading import Thread
import os
#
# def work(name):
#     print('%s say hello'%name)
# if __name__ == '__main__':
#     t=Thread(target=work,args=('egon',))
#     t.start()
#     print('主线程')
#     '''线程开销小  打印结果为
#     egon say hello，主线程
#     '''


class Work(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('%s say hello'%self.name,os.getpid())
if __name__ == '__main__':
    t=Work('EGON')
    t.start()
    print('主线程',os.getpid())
'''线程和主进程pid一致'''






