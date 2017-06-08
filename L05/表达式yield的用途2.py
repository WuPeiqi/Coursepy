#!/usr/bin/env python
# -*- coding:utf-8 -*-

#此为最终结果  已经可以查找到有关键字的文件
'''
grep -rl 'python' /root
'''
import os

def init(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@init #生成器调用装饰器
def search(target):
    '''取出所有文件路径'''
    #更改为生成器
    while True:
        search_path = yield
        g=os.walk(search_path)
        for par_dir,_,files in g:
            for file in files:
                file_abs_path=r'%s\%s'%(par_dir,file)
              #  print('file_abs_path is ==>: ',file_abs_path)
                target.send(file_abs_path)
#g=search()

#d=r'D:\code\py\py3\Coursepy'
#g.send(d)

@init
def opener(target):
    while True:
        file_abs_path=yield
      #  print('opener==>: ',file_abs_path)
        with open(file_abs_path,encoding='utf-8') as f:
            target.send((file_abs_path,f))
        #    pass
#o=opener()
#o.__next__
#o.send('/2.py')
#g=search(opener())   # 将opener函数传送给search   直接在search函数里直接打开
#g.send(d)   测试发送文件打开

@init
def cat(target):
    '''遍历文件内容'''
    while True:
        file_abs_path,f=yield
        for line in f:
            #print(line)
           # print('file_abs_path & line : ',file_abs_path,line)
            tag=target.send((file_abs_path,line))
            #print(tag)
            if tag:
                break
@init
def grep(target,pattern):
    tag=False
    while True:

        file_abs_path,line=yield tag
        tag = False
        if pattern in line:
            tag = True
            target.send(file_abs_path)
@init
def printer():
    while True:
        file_abs_path=yield
        print(file_abs_path)

#将文件路径发送给函数
xx=r'D:\code\py\py3\Coursepy\L05\a\b\b'
x=r'D:\code\py\py3\Coursepy\L05\a'
gg=search(opener(cat(grep(printer(),'python'))))
#print(gg)
gg.send(x)