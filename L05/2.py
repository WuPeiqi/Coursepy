#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
#tool.oschina.net/regex
s='''
wo
'''
res=re.findall('\w',s)  #匹配字符串
print(res)


#匹配字母数字下划线
print(re.findall('\w','as213df_*|'))  #结果为一个列表
print(re.findall('\W','a_b 、\n'))
print(re.findall('\s','a_b 、 \t '))  #匹配空字符 \t \v \f \r 制表符 翻页 换行
print(re.findall('\S','a_bDDDDD 、 \t  '))
print(re.findall('\d','a_b ')) #数字
print(re.findall('\D','a_b ')) #非数字
print(re.findall('\n','a_b \n'))
print(re.findall('^a','a_b  bab'))#从头部开始查找
print(re.findall('.','a_b ')) #任意单个字符
print(re.findall(,'a_b '))



