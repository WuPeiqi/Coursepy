#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import re

res1=re.search('e','python is so easy').group()

s = 'python is so good'
res1=re.split(r'\s+',s)
print(res1)