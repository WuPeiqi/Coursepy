#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

from multiprocessing import Pool,Process
import time
import random
import os

# def work(n):
#     return n**2
# if __name__ == '__main__':
#     pool=Pool()
#     res_l=[]
#     for i in range(6):
#         p=pool.apply_async(work,args=(i,))
#         res_l.append(p)
#     print(res_l)
#
#     for res in res_l:
#         print(res.get())  #拿到真正的执行结果

'''实际示例'''
# def get_page(url):
#     print('正在爬取网页: %s' %url)
#     time.sleep(random.randint(1,3))
#     return 'xxxxxxxxxxxxx'
#
# def parse_page(page_content):
#     print('正在解析网页: %s' %page_content)
#     time.sleep(1)
#     page_content=os.getpid()
#     return page_content
#
# urls=[
#     'baidu.com',
#     'sina.com',
#     'sinasdfa.com',
#     'adsfsina.com',
#     '123312sina.com',
# ]
#
# for url in urls:
#     page_content=get_page(url)
#     res=parse_page(page_content)
#     print(res)
# if __name__ == '__main__':
#    pool=Pool()
#    res_l=[]
#    for url in urls:
#        res=pool.apply_async(get_page,callback=parse_page)
#        res_l.append(res)


'''并发实际示例'''
def get_page(url):
    print('正在爬取网页: %s' %url)
    time.sleep(random.randint(1,3))
    return {'url':url}

def parse_page(page_content):

    time.sleep(1)
    page_content['url']=os.getpid()
    print('正在解析网页结果为: %s' % page_content)
    return page_content



# for url in urls:
#     page_content=get_page(url)
#     res=parse_page(page_content)
#     print(res)
if __name__ == '__main__':
    urls = [
        'baidu.com',
        'sina.com',
        'sinasdfa.com',
        'adsfsina.com',
        '123312sina.com',
    ]
    pool=Pool()
    res_l=[]
    for url in urls:
        #pool.apply_async(get_page(url, ), callback=parse_page)
        res=pool.apply_async(get_page(url,),callback=parse_page)
        res_l.append(res)
        for res in res_l:
            res.get()