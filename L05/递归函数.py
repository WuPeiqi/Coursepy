#!/usr/bin/python
# -*- coding utf8 -*- 

#递归调用：在函数调用过程中，直接或间接地调用了函数本身，这就是函数的递归调用


#
# def f1():
#     print('from f1')
#     f1()
#
# f1()



# def f1():
#     print('f1')
#     f2()
#
# def f2():
#     f1()
#
# f1()


#可以查看递归造成的死循环次数 也可进行修改

# import sys
# print(sys.getrecursionlimit())
# print(sys.setrecursionlimit())
#递归示例 年龄推导
def age(n):
    if n == 1:
        return 18
    return age(n-1) +2
print(age(5))



