#!/usr/bin/python
# -*- coding utf8 -*- 

from gevent import monkey;monkey.patch_all()
import requests
import gevent
import time

def get_page(url):
    print('Get page:%s'%url)
    response=requests.get(url)
    if response.status_code==200:
        print(response.text)

start_time=time.time()
g1=gevent.spawn(get_page,'https://www.python.org')
g2=gevent.spawn(get_page,'https://www.yahoo.com')
g3=gevent.spawn(get_page,'https://www.github.com')
gevent.joinall(
    [
        g1,
        g2,
        g3,
    ]
)
stop_time=time.time()
print('run time is : %s'%(stop_time-start_time))