#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

l=[1,2,10,30,40,33,22,99,31]
l.sort()
print(l)
def search(find_num,seq):
    if len(seq) == 0:
        print('seq not exists')
        return
    mid_index=len(seq)//2
    mid_num=seq[mid_index]
    print(seq, mid_num)
    if find_num >  mid_num:
        seq=seq[mid_index+1:]
        search(find_num, seq)
    elif find_num < mid_num:
        seq=seq[:mid_index]
        search(find_num, seq)
    else:
        print('find it')
search(44,l)