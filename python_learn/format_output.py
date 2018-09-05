#!/usr/bin/python

import math
from python_learn.get_log_info import *

print('{name}websitte:{site}'.format(name='sosos',site='www.nn.com'))

print('{0:.3f}'.format(math.pi))

table = {'Google':1,'Runoob':2,'Taobao':3}
for name,number in table.items():
    print('{0:10}  ==> {1:10d}'.format(name,number))

print('Runoob: {0[Runoob]:d}; Google:{0[Google]:d};Taobao:{0[Taobao]:d}'.format(table))


logger.info('this is test')