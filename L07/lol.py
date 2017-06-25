#!/usr/bin/env python
# -*- coding utf8 -*- 

class lol:
    def __init__(self,name,country,skill):
        self.name=name
        self.country=country
        self.skill=skill

    def skills(self):
        pass

rw=lol('ruiwen','dema','A')
gl=lol('gailun','shalaizhe','S')
print(rw.skill)
print(gl.skill)


#类的传递