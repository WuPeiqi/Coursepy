#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#yield语句形式
#yield表达式形式
#协程函数
'''
示例: 饭店吃饭的过程
'''
# def eater(name):
#     print('%s ready to eat' % name)
#     while True:
#         food=yield
#         print('%s start to eat %s' % (name,food))
#
# g=eater('xp')
# g.__next__()
# g.__next__()
# g.__next__()

#上面next取不到值
#========================================================================
# def deco(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args,**kwargs)
#         next(res)
#         return res
#     return wrapper
#
# @deco  #为了解决第一次无法传值
# def eater(name):
#     print('%s ready to eat' % name)
#     while True:
#         food=yield
#         print('%s start to eat %s' % (name,food))


# g=eater('xp')
# g.send('土豆')
# g.__next__()
# g.__next__()
# g.__next__()
# #可以使用send发送值
# g.send('爆米花')
#第一次必须send(None)  表达式生成器必须先传个空值 进行初始化

#================================================================
def deco(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        next(res)
        return res
    return wrapper

@deco  #为了解决第一次无法传值
def eater(name):
    print('%s ready to eat' % name)
    food_list=[]
    while True:
        food = yield food_list    #返回值
        food_list.append(food)
        print('%s start to eat %s' % (name,food))

g=eater('xp')
g.send('土豆')
g.send('爆米花')
print(g.send('冬瓜片子'))

#x=yield
#g.send('1111'),先把1111传给yield，由yield赋值给x
# 然后再往下执行，直到再次碰到yield，然后把yield后的返回值返回