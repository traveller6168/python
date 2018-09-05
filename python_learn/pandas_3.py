#!/usr/bin/python

import numpy as np
import pandas as pd

obj = pd.Series([4,7,-5,3])
print(obj.values)
print(obj.index)

obj2 = pd.Series([4,7,-5,3], index = ['d','b','a','c'])
print(obj2)
print(obj2['a'])
print(obj2[obj2 >0])
print(obj2*2)
print(np.exp(obj2))
print(obj2)

print('b' in obj2)

sdata = {'Obio':35000, 'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = pd.Series(sdata)
print(obj3)