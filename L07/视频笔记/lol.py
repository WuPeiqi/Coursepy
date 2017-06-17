#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

#值的传递示例:
'''
示例游戏角色直接的攻击传递 . 盖伦和瑞文 定义各自的血量 攻击力 生命值等等
'''

#角色名
class Garen:
    camp='Demacia'#阵营

    def __init__(self, nikename, life_value=200, aggressivity=100):  # 昵称,生命值,攻击力
        self.nikename=nikename
        self.life_value=life_value
        self.aggressivity=aggressivity

    def attack(self,enemy):#攻击对象
        enemy.life_value-=self.aggressivity   #对方减血..对方生命值减去自己的攻击力


class Riven:
    camp = 'Noxus'  # 阵营

    def __init__(self, nikename, life_value=11, aggressivity=11):  # 昵称,生命值,攻击力
        self.nikename = nikename
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attack(self, enemy):  # 攻击对象
        enemy.life_value -= self.aggressivity  # 对方减血..对方生命值减去自己的攻击力

G1=Garen('ob')
R1=Riven('xp')

print(R1.life_value)
G1.attack(R1)
print(R1.life_value)