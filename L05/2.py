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
print(re.findall('\w','as213df_*|'))  #结果为一个列表  #执行结果
print(re.findall('\W','a_b 、\n'))    #执行结果
print(re.findall('\s','a_b 、 \t '))  #匹配空字符 \t \v \f \r 制表符 翻页 换行   #执行结果
print(re.findall('\S','a_bDDDDD 、 \t  '))   #执行结果
print(re.findall('\d','a_b ')) #数字  #执行结果
print(re.findall('\D','a_b ')) #非数字 #执行结果
print(re.findall('\n','a_b \n'))    #执行结果
print(re.findall('^a','a_b  bab'))#从头部开始查找  #执行结果
print(re.findall('.','a_b ')) #任意单个字符   #执行结果
print(re.findall('a.b','a-b a--c ab'))   #执行结果['a-b']

'''
以上执行结果
['w', 'o']
['a', 's', '2', '1', '3', 'd', 'f', '_']
[' ', '、', '\n']
[' ', ' ', '\t', ' ']
['a', '_', 'b', 'D', 'D', 'D', 'D', 'D', '、']
[]
['a', '_', 'b', ' ']
['\n']
['a']
['a', '_', 'b', ' ']
['a-b']
'''
print('-----------------分割线-----------------------')
print(re.findall('a.b','a-b a--c a\nb',re.S))   #re.S 配置到换行符
print(re.findall('a[12]b','a1b a12b a2b a\nb',re.S))   #匹配ab中间包含1或者2   中括号 或者
print(re.findall('a[0-9]c','a2b acc a2c a3c'))  #横杠匹配范围
print(re.findall('a[0\-9]c','a2b acc a2c a3c a-c a0c'))  #转义 或者加到括号的末尾[09-]
print(re.findall('a[0-9a-zA-Z]c','a2b acc a2c a3c'))  #不支持a-Z   匹配全部大小写数字
print(re.findall('a[0-9*]c','a2b acc a2c a3c a*c'))  #匹配数字范围或星号
print(re.findall('a[^0-9]c','2a2b acc a2c a3c a*c'))  #^加到括号里面是取反的意思
'''
以上的结果
['a-b', 'a\nb']
['a1b', 'a2b']
['a2c', 'a3c']
['a-c', 'a0c']
['acc', 'a2c', 'a3c']
['a2c', 'a3c', 'a*c']
['acc', 'a*c']
'''
print('-----------------------分割线-----------------')
print(re.findall('ab*','abbbbbb  a  ab'))  #*出现零次或者无穷次
print(re.findall('ab+','abbbbbb  a  ab'))  #  + 匹配至少一次
print(re.findall('ab[1]+','abbbbbb  ab1  ab'))
print(re.findall('ab[123]+','ab111 ab2  ab3 abc1'))
print(re.findall('ab{3}','abbbbbb  a  ab'))  #{}指定左侧出现的次数
print(re.findall('ab{3,4}','abbbbbb  abbbc a  ab')) #指定匹配出现3到4次 匹配范围
print(re.findall('ab{3,}','abbbbbb  a  ab'))  #3到无穷次匹配
print(re.findall('ab{0,}','abbbbbb  a  ab'))  #等同于*号
print(re.findall('ab{,1}','abbbbbb  a  ab'))  #等同于加号
'''
['abbbbbb', 'a', 'ab']
['abbbbbb', 'ab']
['ab1']
['ab111', 'ab2', 'ab3']
['abbb']
['abbbb', 'abbb']
['abbbbbb']
['abbbbbb', 'a', 'ab']
['ab', 'a', 'ab']
'''
print('-----------------------分割线-----------------')
print(re.findall('ab?c','ac  abc abbc')) #零次或者一次
print(re.findall('a.*c','ac abc aec a1c aaa'))  #贪婪匹配  匹配出的列表只有一个值
print(re.findall('a.*?c','ac abc aec a1c aaa'))  #防止贪婪匹配 加问号
print(re.findall('abc(d|e)','abcd abd abce  ab')) # 得出d 或者e
print(re.findall('abc(?:d|e)','abcd abd abce  ab'))  #返回abcd abce
print(re.findall('a(?:bc)+','abcd abd abce  ab')) #()分组


