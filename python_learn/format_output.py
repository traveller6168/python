#!/usr/bin/python

import math
from python_learn.logger import *

print('{name}websitte:{site}'.format(name='sosos',site='www.nn.com'))

print('{0:.3f}'.format(math.pi))

table = {'Google':1,'Runoob':2,'Taobao':3}
for name,number in table.items():
    print('{0:10}  ==> {1:10d}'.format(name,number))

print('Runoob: {0[Runoob]:d}; Google:{0[Google]:d};Taobao:{0[Taobao]:d}'.format(table))


test = logger()
try:
    y = 5/0
    print (y)
except:
   #print(sys.exc_info())
   test.set_logger('log_test','program run error')
   #test.set_logger('log_test','ddddd')