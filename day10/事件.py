#!/usr/bin/python
# -*- coding utf8 -*- 
from threading import Event,Thread
import threading
import time
def conn_mysql():
    print('%s waiting...' %threading.current_thread().getName())
    e.wait()
    print('%s start to connect mysql....' %threading.current_thread().getName())
    time.sleep(2)

def check_mysql():
    print('%s checking ...'%threading.current_thread().getName())
    time.sleep(4)
    e.set()
if __name__ == '__main__':
    e=Event()
    c1=Thread(target=conn_mysql)
    c2 = Thread(target=conn_mysql)
    c3 = Thread(target=conn_mysql)
    c4=Thread(target=check_mysql)
    c1.start()
    c2.start()
    c3.start()
    c4.start()