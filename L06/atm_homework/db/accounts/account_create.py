#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import json

acc_dic={
    'id':6225,
    'passwd':6225,
    'limit':20000,
    'usable_lim':20000,
    'register':'20170609',
    'expire':'2020-10-01',
    'pay_date':22,
    'status':0
}

print(json.dumps(acc_dic))