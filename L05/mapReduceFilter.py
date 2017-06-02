#!/usr/bin/python
# -*- coding utf8 -*- 

'''
内置函数
map可以做追加映射
'''
l=['alex','wupeiqi','yuanhao']
res=map(lambda x:x+'_SB',l)
print(res)
print(list(res))

#map示例 乘方运算
nums=(2,4,9,10)
res1=map(lambda x:x**2,nums)
print(list(res1))

#reduce  传入2个值进行处理 返回结果和上一个值进行处理
from functools import  reduce
l=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,l))
print(reduce(lambda x,y:x+y,l,500)) #也可以再追加

#filter示例 对字符串进行过滤
l=['alex_SB','wupeiqi_SB','yuanhao_SB','egon']
res=filter(lambda x:x.endswith('SB'),l)
print(res)
print(list(res))


