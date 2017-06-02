#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#内置函数 map reduce filter

def func():
    print('func')

#匿名函数
f=lambda x,y:x+y
#print(f(1,2))

'''
max , min ,zip
'''
#假设以下为人名和工资
dic_1={
    'na':2000,
    'w':3333,
    'd':2,
    'boss':323232,
}
print(max(dic_1))#结果和值不一样,默认比较key的字母排序
print(max(dic_1.values())) #无法得到钱最多的人的值
res=zip(dic_1.values(),dic_1.keys())
#res是个迭代器
#print(list(res)) #迭代器一次性
#print(max(res))

#max进行for循环 根据for循环的值做为key
# def func(k):
#     return dic_1[k]
# print(max(dic_1,key=func))

print(max(dic_1,key=lambda k:dic_1[k]))
print(min(dic_1,key=lambda k:dic_1[k]))

print(sorted(dic_1))                        #默认排序从小到大
print(sorted(dic_1,key=lambda x:dic_1[x]))  #排序从大到小
print(sorted(dic_1,key=lambda x:dic_1[x]),reversed())  #反转