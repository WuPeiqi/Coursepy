#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731



# import glance.api.policy
# glance.api.policy.get()



'''
glance的init文件添加
from glance.api import policy
from glance.api import versions
from glance.cmd import manage
from glance.db import models
'''

#import glance
#glance.api.policy.get()
#glance.models.register_models('sql')

'''
再次追加 可以直接调用
from glance.api import policy
from glance.api import versions
from glance.cmd import manage
from glance.db import models

from glance.api.policy import get
from glance.api.policy import create_resource
from glance.api.cmd import main
from glance.api.db import register_models
'''

glance.get()