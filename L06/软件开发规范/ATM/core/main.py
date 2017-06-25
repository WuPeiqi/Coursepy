#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import os,sys
print(sys.path)
from conf import settings

def run():
    print('from main run')
    print('setings info: ',settings.x)