#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import pickle
dic={'name':'alex','age':123}
#print(pickle.dumps(dic))
#执行结果为bytes格式 b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x04\x00\x00\x00alexq\x02X\x03\x00\x00\x00ageq\x03K{u.

with open('a.pkl','wb') as f1:
    f1.write(pickle.dumps(dic))

with open('a.pkl','rb') as f:
    d=pickle.loads(f.read())
    #print(d)

'''快速处理方法'''
pickle.dump(dic,open('b.pkl','wb'))
res=pickle.load(open('b.pkl','rb'))
print(res)

def func():
    print('from func')

#支持Python格式的对象
pickle.dump(func,open('b.pkl','wb'))

#可以直接调用
pickle.load(open('b.pkl','rb'))()


