#!/usr/bin/python3

import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

path = os.getcwd() +os.sep + 'data' + os.sep + 'bankloan.csv'
data = pd.read_csv(path)
print(data.head())

x_temp = data.iloc[:,:8]
x = x_temp.as_matrix()
y = data.iloc[:,8].as_matrix()

rlr = RLR()
rlr.fit(x,y)
rlr.get_support()
print(rlr.get_support())
print('特征分数:')
print(rlr.scores_)
print(u'有效特征为： %s ' % ','.join(x_temp.columns[rlr.get_support()]))
x = data[x_temp.columns[rlr.get_support()]].as_matrix()
print(x)

lr = LR()
lr.fit(x,y)
print('逻辑回归训练结束！')
print('模型得正确率为： %s ' % lr.score(x,y))