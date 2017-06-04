#!/usr/bin/python
# -*- coding utf8 -*- 

import re
print(re.sub('^(\w+)(\s)(\w+)(\s)(\w+)',r'\5\2\3\4\1','alex make love'))
print(re.sub('^(\w+)(\W+)(\w+)(\W+)(\w+)',r'\5\2\3\4\1','alex " \ + = make ---/== love'))