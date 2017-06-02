#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#模拟grep

import os
#windows下路径是两个斜杠 需要加r  raw string 原生字符串
#g=os.walk(r'D:\code\py\py3\Coursepy\L05\a')

# # for i in g:
# #     print(i)
# def search(search_path):
#     g=os.walk(search_path)
#     for par_idr,_,files in g:  #循环取出路径与文件
#         for file in files:
#             file_abs_path=r'%s%s' %(par_idr,file)
#             print(file_abs_path)
# search(r'D:\code\py\py3\Coursepy\L05\a')
#====================================================
#再次更改为yield模式 实现可以不停的send
import os

def init(func):
    def wrapper(*args,**kwargs):
        res =func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@init
def search(target):
    while True:
        search_path=yield
        g=os.walk(search_path)
        for par_idr,_,files in g:  #循环取出路径与文件
            for file in files:
                file_abs_path=r'%s%s' %(par_idr,file)
                #print(file_abs_path)
                target.send(file_abs_path)
x=r'D:\code\py\py3\Coursepy\L05\a'
#g=search()
#g.send(x)

@init
def opener():
    while True:
        file_abs_path=yield
        with open(file_abs_path,encoding='utf-8') as f:
#            target.send(file_abs_path,f)
             pass
g=search(opener())
g.send(r'D:\code\py\py3\Coursepy\L05\a')