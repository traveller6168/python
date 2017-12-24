#!/usr/bin/env python3

#数据可视化导入
import urllib
from urllib import request
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
import numpy as np
from pylab import plot,show,close
data = np.genfromtxt("/run/media/admin/0008-276D/data/berkeley/iris.csv",delimiter = ",",usecols= (0,1,2,3))
target = np.genfromtxt("/run/media/admin/0008-276D/data/berkeley/iris.csv",delimiter = ",",usecols=(4),dtype=str)
print("data:",data)
print("target:",target)
print("data.shape:",data.shape,type(data))
print("target.shape:",target.shape,type(target))

print(set(target))
plot(data[target == "setosa",0],data[target== "setosa",2],"bo")
plot(data[target == "versicolor",0],data[target== "versicolor",2],"ro")
plot(data[target == "virginica",0],data[target== "virginica",2],"go")
show()

from pylab import figure,subplot,hist,xlim
xmin = min(data[:,0])
amax = max(data[:,0])
