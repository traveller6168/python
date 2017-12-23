from matplotlib import pyplot as plt
import numpy as np

a = np.array([[30,40,70],[80,20,10],[50,90,60]])
print('我们的数组是：')
print(a)
print('\n')
print('调用percentile()函数：')
print(np.percentile(a,50,axis= 1))