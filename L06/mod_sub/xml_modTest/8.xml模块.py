#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import xml.etree.ElementTree as ET
tree=ET.parse('a.xml')
root=tree.getroot()
# for i in root.iter('year'):
#     print(i.tag,i.text,i.attrib)   #标签名  标签内容 标签名中内容
#
#
# #只搜索主节点下  第一个无结果
# print(root.find('year'))
# print(root.find('country').attrib)
# print(root.findall('country')) #查找所有
#
# for country in root:
#     #print(country)
#     print(country.attrib['name'])
#     for item in country:
#         #print(item)
#         print(item.tag,item.text,item.attrib)
#
# for year in root.iter('year'):  #取到所有的year
#     print(year.tag)
#

# #修改标签
# for year in root.iter('year'):
#     year.text=str(int(year.text)+1)
#     year.set('update','yes')
# tree.write('a.xml')
#
#
# #删除标签
# for country in root:
#     print(country)
#     #print('-===>',country.find('year'))
#     year=country.find('year')
#     if int(year.text) > 2010:
#         country.remove(year)
# tree.write('b.xml')

#添加标签
for country in root:
    print(country)
    #print('-===>',country.find('year'))
    year=country.find('year')
    if int(year.text) > 2010:
        year2=ET.Element('year2')
        year2.text=str(int(year.text)+1)
        year2.set('update','yes')
        country.append(year2)
tree.write('e.xml')

#自己创建xml文件