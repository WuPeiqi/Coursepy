#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import pickle
import uuid

#定义基类 作为父类
class BaseModel:
    def save(self):
        pickle.dump(self,open('db/filename','wb')) #dump self代表对象本身,比如s1.save()   dump(s1,oepn())
    @classmethod
    def get_all_obj_list(cls):
        ret=[]
        for file_name in 'db/filename':
            obj=pickle.load(open('db/filename','rb'))
            ret.append(obj)
        return ret
    @classmethod
    def create_uuid(cls):
        return str(uuid.uuid1())
class School:
    #filename='db/school'
    def __init__(self,name,addr):
        self.uuid=BaseModel.create_uuid()
        self.name=name
        self.addr=addr
    def __str__(self):
        return self.name
    def save(self):
        pickle.dump(self,open('db/school/%s' %self.uuid,'wb')) #dump self代表对象本身,比如s1.save()   dump(s1,oepn())
    @classmethod
    def get_all_obj_list(cls):
        ret=[]
        for file_name in 'db/school/*':
            obj=pickle.load(open(file_name,'rb'))
            ret.append(obj)
        return ret
s1=School('oldboy','beijing')
s1.save()
s2=School('北大青鸟','shanghai')
s2.save()
for school_obj in School.get_all_obj_list():
    print('学校的名字 %s ',school_obj)
class Teacher:
    pass

class Course:
    pass

class classes:
    pass

class Student:
    pass