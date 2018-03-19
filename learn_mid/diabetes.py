#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sklearn import datasets
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()
print(diabetes.data)
print(diabetes.target)
print(u'总行数：',len(diabetes.data),len(diabetes.target))
print(u'特征数：',len(diabetes.data[0]))
print(u'数据类型：',diabetes.data.shape)
print(type(diabetes.data),type(diabetes.target))

diabetes_x = diabetes.data[:,np.newaxis]
diabetes_x_tmp = diabetes_x[:,:,2]
print(diabetes_x_tmp)

diabetes_x_train = diabetes_x_tmp[:-20]
diabetes_x_test = diabetes_x_tmp[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

print(u'划分行数：',len(diabetes_x_tmp),len(diabetes_x_train),len(diabetes_x_test))
print(diabetes_x_test)

#回归训练及预测
clf = linear_model.LinearRegression()
clf.fit(diabetes_x_train,diabetes_y_train)#注: 训练数据集

#系数 残差平法和 方差得分
print('Coefficients :\n',clf.coef_)
print("Residual sum of square: %.2f" % np.mean((clf.predict(diabetes_x_test) - diabetes_y_test) ** 2))
print("variance score: %.2f" % clf.score(diabetes_x_test,diabetes_y_test))

#绘图
plt.title(u'LinearRegression Diabetes')   #标题
plt.xlabel(u'Attributes')                 #x轴坐标
plt.ylabel(u'Measure of disease')         #y轴坐标
#点的准确位置
plt.scatter(diabetes_x_test,diabetes_y_test,color = 'black')
#预测结果 直线表示
plt.plot(diabetes_x_test,clf.predict(diabetes_x_test),color = 'blue',linewidth = 3)
plt.xticks(())
plt.yticks(())
plt.show()