#!/usr/bin/python
# -*- coding utf8 -*- 

try:
    int('xx')
except ValueError as e:
    print(e)
except NameError:
    print('NameError')

#万能异常
except Exception as e:
    print(e)
else:
    print('木有异常')
finally:
    print('有无异常都会执行,finally通常用于回收资源')
'''

'''
