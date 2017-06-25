#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

# class E:
#     def test(self):
#         print('from E')
# class D:
#     def test(self):
#         print('from D')
# class A(E):
#     def test(self):
#         print('from a')
# class B(D):
#     pass
#     # def test(self):
#     #     print('from b')
# class C:
#     def test(self):
#         print('from c')
# class F(A,B,C):
#     pass
#     # def test(self):
#     #     print('from D')
# f=F()
#f.test()
#
'''
继承结构
A   B
C   D   E
F

'''
#继承分支 先从左边开始



class A:
    def test(self):
        print('from a')
class B(A):
    #pass
     def test(self):
         print('from b')
class C(A):
    pass
    #def test(self):
      #  print('from c')
class F(B,C):
    pass
    # def test(self):
    #     print('from D')
f=F()
f.test()

'''
   
        A
      -   -
    <-       ->
 B              C
     -     -
       >F<
F继承B和C  B继承A C继承A
此时F没有则找B, B没有则不找源头,从另一个分支开始,此处找C

新式类:都是此继承关系 广度优先,默认不先找根节点
经典类:在Python2中经典类深度优先(即默认不继承object)

'''

print(F.mro()) #Python3打印出继承关系  C3算法的继承效果



