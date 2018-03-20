#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model

data = datasets.load_diabetes()
x = data.data
print(len(x),x.shape)
#print(x[:4])

x_one = x[:,np.newaxis,2]
print(x_one[:4])

y = data.target
print(y[:4])

x_train = x_one[:-42]
x_test = x_one[-42:]
y_train = y[:-42]
y_test = y[-42:]

clf = linear_model.LinearRegression()
clf.fit(x_train,y_train)
pre = clf.predict(x_test)

print(type(pre),type(y_test),pre.shape,y_test.shape)
print("预测结果： %5s " % (pre))
print("实际结果：%5s" % (y_test))

cost = np.mean(y_test-pre)**2
print('平方和计算：',cost)
print('系数：',clf.coef_)
print('截距：',clf.intercept_)
print('方差：',clf.score(x_test,y_test))


plt.title('diabetes')
plt.xlabel("x")
plt.xlabel("y")
plt.plot(x_test,y_test,'k.')
plt.plot(x_test,pre,'g-')
for idx,m in enumerate(x_test):
    plt.plot([m,m],[y_test[idx],pre[idx]],'r-')

plt.show()