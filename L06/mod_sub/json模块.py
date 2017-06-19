#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731
''''''
'''序列化
进行格式的统一
'''

dic={
    'name':'alex',
    'age':1000,
    'height':'150cm'
}

print(dic)

with open('a.txt','w') as f:
    f.write(str(dic))
with open('a.txt','r') as f:
    res=eval(f.read())
    print(res['name'],type(res))

x="[null,true,false,1]"
#evla(x) 报错  有Python不包含的类型

import json
res1=json.loads(x)
print(res1,type(res1))

res2=json.dumps(dic)
print('res2 result is:  ',res2,type(res2))
with open('a.json','w') as f:
    f.write(res2)

'''
序列化的过程 dic -- > json.dumps(dic)---f.write(res2)
反序列化 方向相反
'''

with open('a.json','r') as f:
    res3=f.read()
    dic=json.loads(res3)
    #dic=json.loads(f.read())
    print(dic,type(dic),dic['name'])

'''json的简单操作'''
res4=json.dump(dic,open('b2.json','w'))

res5=json.load(open('b2.json','r'))