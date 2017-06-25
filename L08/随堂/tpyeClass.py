#!/usr/bin/python
# -*- coding utf8 -*- 

class_body='''
class Foo:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self,name):
        print('is talking'%self.name)
'''
#obj=Foo('xp',18)
#print(obj)  #<__main__.Foo object at 0x000001CC9F3BD550>
class_name='Foo'
class_bases=(object,)
class_dict={}
Foo=type(class_body,class_bases,class_dict)
obj=Foo('xp',18)
print(obj)s