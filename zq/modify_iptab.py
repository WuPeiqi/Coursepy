#!/user/local/bin/python3.4
#-*- coding:utf-8 -*-

import os

cnf='-A INPUT -p tcp -m state --state NEW -m tcp --dport 8884 -j ACCEPT'

file_name='/Users/admin/Documents/sysconfig/iptables'
file_tmp='/Users/admin/Documents/sysconfig/iptables.swapc'

cnf=cnf + '\n'

def modify_iptab():
    with open(file_name,encoding='utf-8',mode='r') as iptcfg,open(file_tmp,encoding='utf-8',mode='w') as iptabtmp:
        for line in iptcfg:
            if line.startswith(':OUTPUT'):
                iptabtmp.writelines(line)
                iptabtmp.writelines(cnf)
            else:
                iptabtmp.writelines(line)
    os.remove(file_name)
    os.rename(file_tmp,file_name)
modify_iptab()
