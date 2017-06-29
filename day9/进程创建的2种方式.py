#!/usr/bin/python
# -*- coding utf8 -*- 
'''Python中进程的创建'''
'''
Python中进程创建有2种方式
1.定义一个函数,实例化进程,向其中传参数(执行的函数名,函数参数,进程名).
2.定义类继承进程类,实例化进程,start调用run方法
'''
from multiprocessing import Process
import time
import random
def piao(name):
    print('%s is piaoing' %name)
    time.sleep(3)
    print('%s is piao end' %name)
if __name__ == '__main__':
    p1=Process(target=piao,args=('egon',),name='<p1>')
    p1.start()
    print('pi name is %s',p1.name)
    time.sleep(1)
    print('父进程')

# class Piao(Process):
#     def __init__(self,name):
#         super().__init__()
#         self.name=name
#     def run(self):
#         print('%s is piaoing' %self.name)
#         time.sleep(3)
#         print('%s is piao end'%self.name)
# if __name__ == '__main__':
#     '''创建进程 调用run方法'''
#     p1=Piao('egon')
#     p1.start()
#     print('父进程')