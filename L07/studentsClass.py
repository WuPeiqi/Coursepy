#!/usr/bin/python
# -*- coding utf8 -*- 
#类的继承  类的派生
class students:
    count=0
    def __init__(self,name,ege,sex,score):
        self.name=name
        self.ege=ege
        self.sex=sex
        self.score=score
        students.count += 1
        print('count is: ')
    def talk(self):
        print('====>',name,score)

stu1=students('xp','18','F','100')
