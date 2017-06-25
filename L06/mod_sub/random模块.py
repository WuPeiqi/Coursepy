#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import  random
print(random.random())   #大于0 小于1
print(random.randint(1,3)) #大于等于1 小于等于3
print(random.randrange(1,3))    #小于等于1小于3之间


proxy_ip=[
    '10.10.8.2',
    '10.10.2.8',
    '10.59.2.56',
    '10.19.15.1',
]
print(random.choice(proxy_ip))

print(random.sample([1,'23',[4,5]],2))  #随机选择2个 组成列表
print(random.uniform(1,3))  #小于1小于3的小数

item=[1,3,4,5]
print(random.shuffle(item))   # 打乱次序 相当于洗牌
print(item)

def v_code(n=5):
    res=''
    for i in range(n):
        num=random.randint(0,9)
        #s=random.randint(65,90)  #asci码对应的字母
        s=chr(random.randint(65,90))
        add=random.choice([num,s])
        res+=str(add)
    return res
print(v_code(6))