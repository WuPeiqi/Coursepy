#!/usr/bin/python
# -*- coding utf8 -*- 

#class Foo:
#    def

class List(list):
    def __init__(self,item,permission=False):
        self.__init__=super().__init__(item)
        self.permission=permission
    def __del__(self):
        if not :
            raise TypeError('类型错误')
        else:
            del List

l1=List([1,2,3])
del l1