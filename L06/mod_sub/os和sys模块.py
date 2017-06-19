#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import os
# print(os.getcwd())  #打印当前目录
# print(os.chdir('c:\\'))  #改变目录
# print(os.getcwd())
# print(os.listdir()) #列出目录下所有文件和内容
# print(os.curdir)  #当前目录符号
# print(os.pardir) #父目录符号
# print(os.makedirs())
# print(os.mkdir())
# print(os.removedirs()) #递归删除空目录
# print(os.rmdir()) #删除空目录
# print(os.remove())#删除文件
# print(os.rename())#重命名
# print(os.stat())#获取文件信息
'''
print(os.sep) 系统路径分隔符
os.linesep  行终止符  win为\t\n   linux为\n
os.pathsep  环境变量分隔符 win;  linux:
os.name 当前平台   win是'nt'
'''
# print(os.path.abspath('a/b')) #取绝对路径 以当前路径
# print(os.path.abspath('/a/b'))#以当前盘符取绝对路径
#
# print(os.path.split('e:/a/b.txt')) #切割目录和文件
# print(os.path.dirname('E:\\a')) #取上一级目录
#
# print(os.path.exists('d:\\code')) #判断路径存在
# print(os.path.isabs('E:\\')) #判断绝对路径
'''
os.isfile()
os.isdir()

获取访问时间修改时间
os.path.getatime()
os.path.getmtime()


os.getsize() 获取文件大小

'''
print(os.path.join('a','b','c'))   #路径拼接
print(os.path.join('a','b','E:\\c'))  #丢弃前边 从绝对路径开始拼接
'''
a\b\c
E:\c
'''
print(os.path.normcase('C:\\wINDOWS/xp'))  #转换为小写 单斜杠c:\windows\xp
print(os.path.normpath('c://windows\\System32\\../Temp/')) #转为..为上级目录 c:\windows\Temp

#添加到环境变量
res=os.path.abspath(__file__) #取当前文件的绝对路径
print(res)
res_p=os.path.dirname(res)
print(res_p)
res_p=os.path.dirname(res_p)
print(res_p)
import sys
sys.path.append(res_p)



print(__file__)
res=os.path.join(__file__, os.pardir,os.pardir) #追加2个..
print(res)
res=os.path.normpath(res)   #转换..为上级目录
print(res)



