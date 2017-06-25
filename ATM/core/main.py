#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from core import logs

def run():
    print('from main run')
    logger=logs.get_logger()
    #logger.info('transfer 111')

if __name__ == '__main__':
    run()