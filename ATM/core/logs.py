#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731


import logging

def get_logger():
    logger = logging.getLogger()

    fh = logging.FileHandler('test.log')  # 文件流
    ch = logging.StreamHandler()  # 屏幕流

    # 格式
    format = logging.Formatter("%(asctime)s--%(levelname)s--%(message)s")

    # 添加输出样式
    fh.setFormatter(format)
    ch.setFormatter(format)

    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.setLevel(logging.DEBUG)

    #logger.info("transfer 10000")
    return logger