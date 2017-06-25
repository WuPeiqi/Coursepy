#!/usr/bin/python
# -*- coding utf8 -*- 

class Animal:
    def talk(self):
        print('正在叫')
class People(Animal):
    def talk(self):
        print('say hi')
class Pig(Animal):
    def talk(self):
        print('哼')
class Dog(Animal):
    def talk(self):
        print('汪')

peo1=People()
dog1=Dog()
pig1=Pig()

def func(obj):
    obj.talk()
func(peo1)
func(dog1)
func(pig1)