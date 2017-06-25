#!/usr/bin/env python
# -*- coding:utf-8 -*-


print('from glancepackage')
x=1
from glance.api import policy
from glance.api import versions
from glance.cmd import manage
from glance.db import models

from glance.api.policy import get
from glance.api.policy import create_resource
from glance.api.cmd import main
from glance.api.db import register_models