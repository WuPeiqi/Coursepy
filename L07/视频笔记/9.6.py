#!/usr/bin/python
# -*- coding:utf-8 -*-

# class Foo:
#     x=1
#     def test(self):
#         print('from test')
#
# print(Foo.x)


# class Foo:
#     __x=1 #_Foo__x
#     def __test(self): #_Foo__test
#         print('from test')
# print(Foo.__dict__)
# print(Foo.__x)
# Foo.test(123)
# print(Foo._Foo__x)


# class People:
#     __country='China'
#     def __init__(self,name,age,sex):
#         self.__name=name #self._People__name=name
#         self.__age=age
#         self.__sex=sex
#
#     def tell_info(self):
#         print('人的名字是:%s ,人的性别是:%s,人的年龄是：%s' %(
#             self.__name, #p._People__name
#             self.__age,
#             self.__sex))
#
# p=People('alex',18,'male')
# print(p.__dict__)
# p.tell_info()
#
# print(p.__name)

# p.__salary=3000
# print(p.__dict__)
#
# print(People.__dict__)
#
# People.__n=11111111111111111111111111
# print(People.__dict__)
# print(People.__n)



# class Parent:
#     def foo(self):
#         print('from parent.foo')
#         self.__bar() #self._Parent__bar()
#
#     def __bar(self): #_Parent__bar
#         print('from parent.bar')
#
#
# class Sub(Parent):
#     # def __bar(self): #_Sub__bar
#     #     print('from SUb.bar')
#     pass
# s=Sub()
# s.foo()

# s._Parent__bar()



# class People:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#
#     def tell_info(self):
#         print('人的名字是:%s ,人的年龄是：%s' %(
#                     self.__name, #p._People__name
#                     self.__age))
#
#     def set_info(self,x,y):
#         if not isinstance(x,str):
#             raise TypeError('名字必须是字符串类型')
#         if not isinstance(y,int):
#             raise TypeError('年龄必须是整数类型')
#
#         self.__name=x
#         self.__age=y
#
#
# p=People('alex',1000)
# p.tell_info()
#
# p.set_info('alex_SB',123)
# p.tell_info()





# property

# class Foo:
#     @property
#     def test(self):
#         print('from fooo')
#     # test=property(test)
#
# f=Foo()
# # f.test()
# f.test



# class People:
#     def __init__(self,name,weight,height):
#         self.name=name
#         self.weight=weight
#         self.height=height
#
#     @property
#     def bmi(self):
#         return self.weight / (self.height ** 2)
#
# p=People('egon',75,1.80)
# p.height=1.82
# # print(p.bmi())
# print(p.bmi)







# class People:
#     def __init__(self,name,permmission=False):
#         self.__name=name
#         self.permmission=permmission
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError('名字必须是字符串类型')
#         self.__name=value
#
#     @name.deleter
#     def name(self):
#         if not self.permmission:
#             raise PermissionError('不允许的操作')
#         del self.__name
#
# p=People('egon')
#
# # print(p.name)
# #
# # p.name='egon666'
# # print(p.name)
# #
# # p.name=35357
# p.permmission=True
# del p.name




class People:
    def __init__(self,name,permmission=False):
        self.__name=name
        self.permmission=permmission

    def get_name(self):
        return self.__name

    def set_name(self,value):
        if not isinstance(value,str):
            raise TypeError('名字必须是字符串类型')
        self.__name=value

    def del_name(self):
        if not self.permmission:
            raise PermissionError('不允许的操作')
        del self.__name
    name=property(get_name,set_name,del_name)
p=People('egon')

# print(p.name)
#
# p.name='egon666'
# print(p.name)
#
# p.name=35357
p.permmission=True
del p.name
