#!/usr/bin/python3

from sklearn import linear_model
from matplotlib import pyplot as plt

#本程序建立逻辑回归模型
#让逻辑回归模型自动学习如何判断两个数值的大小关系

#训练数据集，共8个样本
#每个样本包含两个特征[a,b]
#前4个样本表示a<b，后4个样本表示a>b

data = [[3,4],[3,6],[3,7],[4,7],
        [4,3],[6,3],[7,3],[7,4]]

#目标值，即a<b还是a>b
#0表示a<b，1表示a>b
target = [0,0,0,0,
          1,1,1,1]

#初始化逻辑回归模型
logreg = linear_model.LogisticRegression(C=1e5)
#训练逻辑回归模型
logreg.fit(data,target)
#测试判断样本[100,101]的目标值
#即判断100<101还是100>101
print(logreg.predict([[100,101]]))
print(logreg.predict([[101,100]]))

#在一个2D图上绘制点阵
#如果x<y，则将点绘制成红色
#如果x>y，则将点绘制成蓝绿色

for x in range(0,20):
    for y in range(0,20):
         # 输入[x,y]，利用逻辑回归模型预测目标值
         t = logreg.predict([[x,y]])
         if (t == 0):
             plt.plot(x,y,'ro')
         else:
             plt.plot(x,y,'co')
plt.show()