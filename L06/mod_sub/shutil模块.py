#!/usr/bin/env python
# -*- coding:utf-8 -*-

#Author:xp
#blog_url: http://blog.csdn.net/wuxingpu5/article/details/71209731

import shutil

#shutil.copyfileobj(open('mod_xml.py','r'),open('mod_xml.2.py','w'))

#shutil.copyfileobj(src,dst) #仅拷贝权限

#shutil.copy()  #拷贝文件加上权限

#shutil.copytree('folder1','folder2',ignore=shutil.ignore_patterns('*.pyc','tem*')) #拷贝目录 忽略指定文件

#shutil.copytree('f1','f2',symlinks=True) #拷贝软链接

#shutil.move('folder1','folder2')#重命名

#shutil.make_archive('databak','gztar',root_dir='/data')   #gzip格式打包   进行压缩   默认不要加文件后缀

#解压
import tarfile
#
# # 打包
# >>> t=tarfile.open('/tmp/egon.tar','w')
# >>> t.add('/test1/a.py',arcname='a.bak')
# >>> t.add('/test1/b.py',arcname='b.bak')
# >>> t.close()
#
#
# # 解压
# >>> t=tarfile.open('/tmp/egon.tar','r')
# >>> t.extractall('/egon')
# >>> t.close()


