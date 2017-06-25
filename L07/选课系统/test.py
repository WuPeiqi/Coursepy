#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import uuid
import hashlib
import time

class School:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name
s1=School('北京')
print(s1)

def create_uuid():
    return str(uuid.uuid1())


def create_md5():
    m=hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()

if __name__ == '__main__':
    print(create_uuid())
    print(create_uuid())
    print(create_md5())
    print(create_md5())