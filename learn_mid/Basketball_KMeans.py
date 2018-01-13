#!/usr/bin/env python3
"""
第一部分：导入包
从sklearn.cluster机器学习聚类包中导入KMeans聚类
"""
# coding=utf-8
from sklearn.cluster import Birch
from sklearn.cluster import KMeans

""" 
第二部分：数据集 
X表示二维矩阵数据，篮球运动员比赛数据 
总共20行，每行两列数据 
第一列表示球员每分钟助攻数：assists_per_minute 
第二列表示球员每分钟得分数：points_per_minute 
"""

import os
data = []
for line in open("F:/资料/data/basketball.txt",'r').readlines():
    line = line.rstrip()
    result = ' '.join(line.split())
    s = [float(x) for x in result.strip().split(' ')]
    print(s)
    data.append(s)
print('完整数据集')
print(data)
print(type(data))

L2 = [n[0] for n in data]
L5 = [n[4] for n in data]
T = dict(zip(L2,L5))
print(T)
X = list(map(lambda x,y:(x,y),T.keys(),T.values()))

print(X)
""" 
第三部分：KMeans聚类 
clf = KMeans(n_clusters=3) 表示类簇数为3，聚成3类数据，clf即赋值为KMeans 
y_pred = clf.fit_predict(X) 载入数据集X，并且将聚类的结果赋值给y_pred 
"""
clf = KMeans(n_clusters = 3)
y_pred = clf.fit_predict(X)

#输出完整Kmeans函数，包括很多省略参数
print(clf)
#输出聚类预测结果，20行数据，每个y_pred对应X一行或一个球员，聚成3类，类标为0、1、2
print(y_pred)

""" 
第四部分：可视化绘图 
Python导入Matplotlib包，专门用于绘图 
import matplotlib.pyplot as plt 此处as相当于重命名，plt用于显示图像 
"""

import numpy as np
import matplotlib.pyplot as plt

#获取第一列和第二列数据 使用for循环获取 n[0]表示X第一列
x = [n[0] for n in X]
print(x)
y = [n[1] for n in X]
print(y)

#绘制散点图 参数：x横轴 y纵轴 c=y_pred聚类预测结果 marker类型 o表示圆点 *表示星型 x表示点
#plt.scatter(x,y,c = y_pred, marker = 'o')

x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

i = 0
while i < len(X):
    if y_pred[i] == 0 :
        x1.append(X[i][0])
        y1.append(X[i][1])
    elif y_pred[i] == 1 :
        x2.append(X[i][0])
        y2.append(X[i][1])
    elif y_pred[i] == 2 :
        x3.append(X[i][0])
        y3.append(X[i][1])
    i = i +1

plot1, = plt.plot(x1,y1,'or', marker = 'x')
plot2, = plt.plot(x2,y2,'og', marker = 'o')
plot3, = plt.plot(x3,y3,'ob', marker = '*')


#绘制标题
plt.title("Kmeans-Basketball Data")

#绘制x轴和y轴坐标
plt.xlabel("assists_per_minute")
plt.ylabel("points_per_minute")

#设置右上角图例
plt.legend((plot1,plot2,plot3),("A","B","C"), fontsize = 10)

#显示图形
plt.show()