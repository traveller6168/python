#!/usr/bin/ptrhon3
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV

from urllib import request
url = request.urlopen(r'http://aima.cs.berkeley.edu/data/iris.csv')
#/home/admin/PycharmProjects/test/ll
localFiel = open("iris.csv","wb+")
localFiel.write(url.read())
localFiel.close()

from numpy import genfromtxt,zeros
data = genfromtxt("iris.csv", delimiter=",", usecols=(0, 1, 2, 3))
target = genfromtxt("iris.csv", delimiter=",", usecols=(4), dtype=str)
print ("data:",data)
print("target:",target)
print("data.shape:",data.shape)
print("target.shape:",target.shape)

print(set(target))


# 使用 pylab 库（matplotlib的接口）的 plotting 方法可以建一个二维散点图让我们在两个维度上分析数据集的两个特征值
from pylab import plot, show, close
# 蓝色点代表山鸢尾、红色点代表变色鸢尾、绿色点代表维吉尼亚鸢尾
# 第一和第三维度是花萼的长度和花瓣的长度
plot(data[target == "setosa", 0],data[target == "setosa", 2], "bo")
plot(data[target == "versicolor", 0],data[target == "versicolor", 2], "ro")
plot(data[target == "virginica", 0],data[target == "virginica", 2], "go")
#show()
close()

# 另一种常用的查看数据的方法是分特性绘制直方图
# 下面的代码可以绘制数据中每一类型的第一个特性（花萼的长度）
from pylab import figure,subplot,hist,xlim,show
xmin = min(data[:,0])
xmax = max(data[:,0])
figure()
subplot(411)
hist(data[target == "setosa",0],color="b",alpha=.7)
xlim(xmin,xmax)
subplot(412)
hist(data[target == "versicolor",0],color="r",alpha=.7)
xlim(xmin,xmax)
subplot(413)
hist(data[target == "virginica",0],color="g",alpha=.7)
xlim(xmin,xmax)
subplot(414)
hist(data[:,0],color="y",alpha=.7)
xlim(xmin,xmax)
#show()
close()


# 分类
#     ------  高斯朴素贝叶斯分类 ------
# 把字符串数组转型成整型数据
t = zeros(len(target))
t[target == "setosa"] = 1
t[target == "versicolor"] = 2
t[target == "virginica"] = 3

# 模型实例化和训练分类器
from sklearn.naive_bayes import GaussianNB

classifier = GaussianNB()
classifier.fit(data, t)

# 分类器可以由 predict 方法完成，并且只要输出一个样例就可以很简单的检测
print (classifier.predict([data[0]]))
print (t[0])

# 评估分类器
# 通过从源数据集中随机抽取样本把数据分为训练集和测试集，然后使用训练集的数据来训练分类器，并使用测试集来测试分类器

#from sklearn import cross_validation


train, test, t_train, t_test = train_test_split(data, t, test_size=0.4, random_state=0)

# 训练分类器并输出精确度
classifier.fit(train, t_train)
print (classifier.score(test, t_test))

# 另一个估计分类器表现的工具叫做混淆矩阵。在此矩阵中每列代表一个预测类的实例，每行代表一个实际类的实例
from sklearn.metrics import confusion_matrix

print (confusion_matrix(classifier.predict(test), t_test))
""" 
如果我们牢记所有正确的猜测都在表格的对角线上，那么观测表格的错误就很容易了，即 
对角线以外的非零值 
"""

# 可以展示分类器性能的完整报告的方法也是很好用的
from sklearn.metrics import classification_report

print (classification_report(classifier.predict(test), t_test, target_names=["setosa", "versicolor", "virginica"]))


#     ------ 聚类 ------
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, init="random")
kmeans.fit(data)

c = kmeans.predict(data)

# 估计群集的结果，与使用完整性得分和同质性得分计算而得的标签作比较
from sklearn.metrics import completeness_score, homogeneity_score

print(completeness_score(t, c))
print(homogeneity_score(t, c))
""" 
当大部分数据点属于一个给定的类并且属于同一个群集，那么完整性得分就趋向于 1 
当所有群集都几乎只包含某个单一类的数据点时同质性得分就趋向于 1 
"""

# 把集群可视化并和带有真实标签的做可视化比较
figure()
subplot(211)
plot(data[t == 1, 0], data[t == 1, 2], "bo")
plot(data[t == 2, 0], data[t == 2, 2], "ro")
plot(data[t == 3, 0], data[t == 3, 2], "go")
subplot(212)
plot(data[c == 1, 0], data[c == 1, 2], "bo", alpha=.7)
plot(data[c == 2, 0], data[c == 2, 2], "ro", alpha=.7)
plot(data[c == 0, 0], data[c == 0, 2], "go", alpha=.7)
show()
close()


#     ------ 回归 ------
# 为了应用线性回归，我们需要建立一个由上所述的综合数据集
from numpy.random import rand

x = rand(40, 1)
y = x * x * x + rand(40, 1) / 5

from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(x, y)

# 我们可以通过把拟合线和实际数据点画在同一幅图上来评估结果
from numpy import linspace, matrix

xx = linspace(0, 1, 40)
plot(x, y, "o", xx, linreg.predict(matrix(xx).T), "--r")
show()
close()

# 我们还可以使用均方误差来量化模型和原始数据的拟合度
from sklearn.metrics import mean_squared_error

print(mean_squared_error(linreg.predict(x), y))
""" 
该指标度量了预期的拟合线和真实数据之间的距离平方，当拟合线很完美时该值为 0 
"""

#     ------ 相关 ------
""" 
我们通过研究相关性来理解成对的变量之间是否相关，相关性的强弱。此类分析帮助我们精确定位被依赖的重要变量。 
最好的相关方法是皮尔逊积矩相关系数，它是由两个变量的协方差除以他们的标准差的乘机计算而来 
"""

from numpy import corrcoef

corr = corrcoef(data.T)
print(corr)

from pylab import pcolor, colorbar, xticks, yticks, close
from numpy import arange

pcolor(corr)
colorbar()
xticks(arange(0.5, 4.5), ['sepal length', 'sepal width', 'petal length', 'petal width'], rotation=-20)
yticks(arange(0.5, 4.5), ['sepal length', 'sepal width', 'petal length', 'petal width'], rotation=-20)
show()
close()

#    ------ 降维 ------
# 最著名的降维技术之一就是主成分分析
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pcad = pca.fit_transform(data)

plot(pcad[target == "setosa", 0], pcad[target == "setosa", 1], "bo")
plot(pcad[target == "versicolor", 0], pcad[target == "versicolor", 1], "ro")
plot(pcad[target == "virginica", 0], pcad[target == "virginica", 1], "go")
show()
close()

# PCA 将空间数据方差最大化，我们可以通过方差比判断 PCs 包含的信息量
print(pca.explained_variance_ratio_)
# 输出：[ 0.92461621  0.05301557]
# 现在我们知道第一个 PC 占原始数据的 92% 的信息量而第二个占剩下的 5%，我们还可以输出在转化过程中
# 丢失的信息量
print(1 - sum(pca.explained_variance_))
# 此时我们可以是应用逆变换还原原始数据
data_inv = pca.inverse_transform(pcad)
# 可以证明的是，由于信息丢失逆变换不能给出准确的原始数据，我们可以估算逆变换的结果和原始数据的相似度
print(abs(sum(sum(data - data_inv))))

# 通过改变主成分的数值来计算我们能够覆盖多少信息量是很有趣的
for i in range(1, 5):
    pca = PCA(n_components=i)
    pca.fit(data)
    print(sum(pca.explained_variance_ratio_) * 100, "%")

# ------ 网络挖掘 ------
# 通常我们分析的数据是以网络结构存储的，我们可以使用点和边描述之间的关系
# 本章中我们将会介绍分析此类数据的基本步骤，称为图论，一个帮助我们创造、处理和研究网络的类库
# 尤其我们将会介绍如何使用特定方法建立有意义的数据可视化，以及如何建立一组关联稠密的点
# 使用图论可以让我们很容易的导入用于描述数据结构的最常用结构
import networkx as nx

G = nx.read_gml("lesmiserables.gml", relabel=True)
# networkx 必须要下载 1.9.1 版本才行
# 在上述代码我们导入了《悲惨世界》同时出现的单词组成的网络，可以通过https://gephi.org/datasets/lesmiserables.gml.zip免费
# 下载，数据以GML格式存储。我们还可以使用下面的命令导入并可视化网络：
nx.draw(G, node_size=0, edge_color="b", alpha=.2, font_size=7)

