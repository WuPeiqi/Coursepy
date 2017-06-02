#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import re

def welcome_use():
    '''wlecome to use & input regular for content'''
    print('welcom to use')
    re_in=input('Please input your content will be computed: ')
    print('input info: %s'%re_in)
    return re_in

def plus_subtr(*args,**kwargs):
    '''plus & subtract'''
    pass

def multi_divis(arg1):
    '''multiplication & division '''
    print('arg1 is: %s'%arg1)
    mul=re.findall(r'\d+\*\d+',arg1)
    num_every=re.findall(r'\d+',arg1)
    print('mul is: %s ,%s' % mul, num_every)

def brack_opera():
    '''brack operation'''
    #res_bo=bool(re.compile(r'\(',expression))
    res_bo=bool(re.findall(r'\(+',expression))
    print(res_bo)
    if res_bo:
        print('include (')
        result_temp=multi_divis(expression)
        #result_real=multi_divis(result_temp)
    else:
        print('not include')
        result_temp = multi_divis(expression)
        # result_real=multi_divis(result_temp)
    #print(result_real)
    #return result_real

if __name__ == '__main__':
    expression =  welcome_use()
    print('type is',type(expression))
    brack_opera()
