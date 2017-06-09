#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }
std3={'name':'xp','score':111}
def print_score(std):
    print('%s %s'%(std['name'],std['score']))
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s %s'%(self.name,self.score))

bart = Student('Bart simpsom',59)
bart.print_score()
