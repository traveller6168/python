#!/usr/bin/env python3

from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()
'''''
print(iris.data)
print(iris.target)
print(len(iris.target))
print(iris.data.shape)
'''

''''' 
重点：分割数据集 构造训练集/测试集，120/30 
     70%训练  0-40  50-90  100-140 
     30%预测  40-50 90-100 140-150 
'''
#训练集
train_data = np.concatenate((iris.data[0:40, :], iris.data[50:90, :], iris.data[100:140, :]), axis = 0)
#训练集样本类别
train_target = np.concatenate((iris.target[0:40], iris.target[50:90], iris.target[100:140]), axis = 0)
#测试集
test_data = np.concatenate((iris.data[40:50, :], iris.data[90:100, :], iris.data[140:150, :]), axis = 0)
#测试集样本类别
test_target = np.concatenate((iris.target[40:50], iris.target[90:100], iris.target[140:150]), axis = 0)

#导入决策树DTC包
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(train_data,train_target)
print(clf)

#predicted = clf.predict(iris.data)



#预测结果
predict_target = clf.predict(test_data)
print(predict_target)
#预测结果与真实结果比对
print("预测结果与真实结果比对")
print(sum(predict_target == test_target))


#输出准确率 召回率 F值
from sklearn import metrics
print("输出准确率 召回率 F值")
print(metrics.classification_report(test_target,predict_target))
print(metrics.confusion_matrix(test_target,predict_target))


#获取花卉测试数据集两列数据集
#X = iris.data
X = test_data
L1 = [x[0] for x in X]
L2 = [x[1] for x in X]


import matplotlib.pyplot as plt
plt.scatter(L1,L2, c = predict_target , marker = 'x')
plt.title("DecisionTreeClassifier")
plt.show()