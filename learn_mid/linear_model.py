#!/usr/bin/env python3

from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

#x表示皮萨尺寸， Y表示皮萨价格
X = [[6],[8],[10],[14],[18]]
Y = [[7],[9],[13],[17.5],[18]]
print(u'数据集X：',X)
print(u'数据集Y：',Y)

#回归训练
clf = linear_model.LinearRegression()
clf.fit(X,Y)
res = clf.predict(np.array([12]).reshape(-1,1))[0]
print(u'预测一张12英寸皮萨价格：$%.2f' % res)

#预测结果
X2 = [[0],[10],[14],[25]]
Y2 = clf.predict(X2)

#绘制线性回归图形
plt.figure()
plt.title(u'diameter-cost curver')
plt.xlabel(u'diameter')
plt.ylabel(u'cost')
plt.axis([0,25,0,25])  #区间
plt.grid(True)  #显示网格
plt.plot(X,Y,'k.')
plt.plot(X2,Y2,'g-')
plt.show()
print (u'系数', clf.coef_)
print (u'截距', clf.intercept_)
print (u'评分函数', clf.score(X, Y))
''''' 
系数 [[ 0.9762931]] 
截距 [ 1.96551743] 
评分函数 0.910001596424 
'''