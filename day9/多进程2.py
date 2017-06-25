#!/usr/bin/python
# -*- coding utf8 -*-
import os
#print(os.cpu_count())
from multiprocessing import Process
import time
import random

class Piao(Process):
    def __init__(self,name):
        super().__init__()
        self.name=name
    def run(self):
        print('x')
        print('%s is piaoing' % self.name)
        time.sleep(3)
        print('%s is piao end' % self.name)
if __name__ == '__main__':
    p1=Piao('egon')
    p1.start()
    #p1.join() #等待执行完
    print('父进程')
