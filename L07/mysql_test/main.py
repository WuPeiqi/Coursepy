#!/usr/bin/python
# -*- coding utf8 -*- 

import settings
class Mysql:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        print('connecting..')
    @classmethod
    def from_conf(cls):
        return cls(settings.HOST,settings.PORT)
    def select(self):
        print(self)
        print('select function')
conn=Mysql('192.168.1.3',3306)
conn2=Mysql.from_conf()