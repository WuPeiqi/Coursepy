#!/usr/bin/env python
# -*- coding:utf-8 -*-

__all__=['money','s2']#控制导入*的内容
#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

print('from spam')
money=1000
def s1():
    print('1111',money)
def s2():
    print('''222222 from spam s2 func''')
    s1()
def change():
    global money
    money=0


print('当前文件的路径',__file__)
#spam.py当做脚本执行__name__等于__main__
#被当做模块导入  等于模块名
#可以用于判断状态 示例:
print('当前文件的名字',__name__)

if __name__=='__main__':
    print('当做脚本执行')
    change()
    print(money)