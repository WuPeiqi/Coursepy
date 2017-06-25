#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

'''
目录结构
glance_test
    api 
        __init__
        policy.py
        versions.py
    cmd
        __init__
    db
        __init__
        models.py
    __init__
glance_test.py

'''


#绝对导入  from导入给外部使用   内部执行报错
#内部执行使用main函数
#from glance_test.api import versions

if __name__=='__main__':
    import versions



#相对导入

else:
    from ..db import models
