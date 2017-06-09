#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731
#
# 获取当前时间
from datetime import datetime
now =datetime.now() #获取当前时间
print(now)
print(type(now))
'''
2017-06-08 13:52:49.095945
<class 'datetime.datetime'>
'''

#
# 获取指定时间

dt = datetime(2017,6,8,13,54)
print(dt)

dt=dt.timestamp() #转换为timstamp  时间戳
print(dt)

#时间戳转换为datetime
t=1496901240.0
print('timestamp to datetime: %s' % datetime.fromtimestamp(t))


#格林威治时间转换
print('---------------------------------------------------')
'''
此时相互转换的时间是转换到本地时间  即当前操作系统所在位置的时间 
也就是东八区时间
转换到格林威治标准时间的方法是utcfromtimestamp
示例:
'''
t=1496901240.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))
'''
结算结果为
---------------------------------------------------
2017-06-08 13:54:00
2017-06-08 05:54:00
本地时间为utc +8:00 格林威治标准时间为UTC + 0:00

'''

#字符串转换为时间

cday=datetime.strptime('2017-06-08 14:06:22', '%Y-%m-%d %H:%M:%S')
print(cday,type(cday))
#字符串转换的是默认没有时区信息的

#时间转换为字符串
now=datetime.now()
print(now.strftime('%a,%b %d %H:%M'))  #Thu,Jun 08 14:09

#时间的加减
from datetime import timedelta
now=datetime.now()
now=now+timedelta(hours=10)
print(now)
now=now - timedelta(days=1)
now + timedelta(hours=1,days=2)

from datetime import datetime, timedelta,timezone
tz_utc_8=timezone(timedelta(hours=8)) #创建时区UTC=8:00
now=datetime.now()
print(now)
dt = now.replace(tzinfo=tz_utc_8)
print(dt)
#对比可以查看dt包含+8:00

print('---------------------------------------------------')
#utcnow() 可以获取当前UTC时间,再转换为任意时区的时间

#示例  获取当前utc时间  转换为utc_0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

#转换为北京时间
bj_dt=utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

#astimezone转换为东京时间
tokyo_dt=utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

#astimezone直接北京时间转换为东京时间
tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

'''
任何带时区的datetime都可以转换到对应的时区,  带有tzinfo(时区) 默认tzinfo为空

1要存储dateime最好转换为timstamp  时间戳格式  时间戳与时区无关
'''



