#!/usr/bin/python
# -*- coding utf8 -*- 
'''队列,先进先出'''
# import queue
#
# q=queue.Queue(3)
# q.put('a')
# q.put('b')
# q.put('c')
#
# print(q.get())
# print(q.get())
# print(q.get())

import queue
# q=queue.LifoQueue() #堆栈  后进先出
# q.put('a')
# q.put('b')
# q.put('c')
#
# print(q.get())
# print(q.get())
# print(q.get())

q=queue.PriorityQueue() #优先级
q.put((10,'a'))
q.put((1,'b'))
q.put((2,'c'))

print(q.get())
print(q.get())
print(q.get())





