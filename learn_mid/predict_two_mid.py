#!/usr/bin/env python3

import os
import random
import numpy as np
import matplotlib.pyplot as plt

#加载数据
def load_exdata(filename):
    data = []
    with open(filename,'r') as f:
        for line in f.readlines():
            line = line.split(',')
            current = [int(item) for item in line]
            data.append(current)
    return data

path = os.getcwd() + '/data/ex1data2.txt'
data = load_exdata(path)
data = np.array(data,np.int64)
print(data)

#特征缩放
def featureNormalize(x):
    x_norm = x;
    mu = np.zeros((1,x.shape[1]))
    sigma = np.zeros((1,x.shape[1]))
    for i in range(x.shape[1]):
        mu[0,i] = np.mean(x[:,i]) #均值
        sigma[0,i] = np.std(x[:,i]) #标准差
    print(mu)
    print(sigma)
    x_norm = (x - mu) / sigma
    return x_norm,mu,sigma

#计算损失
def computeCost(x,y,theta):
    m = y.shape[0]
    c = x.dot(theta) - y
    J2 = (c.T.dot(c)) / (2*m)
    return J2

#梯度下降
def gradientDescent(x,y,theta,alpha,num_iters):
    m = y.shape[0]
    J_history = np.zeros((num_iters,1))
    for iter in range(num_iters):
        theta = theta - (alpha/m) * (x.T.dot(x.dot(theta) - y))
        J_history[iter] = computeCost(x,y,theta)
    return J_history,theta



iterations = 10000 #迭代次数
alpha = 0.01 #学习率
x = data[:,(0,1)].reshape((-1,2))
y = data[:,2].reshape((-1,1))
m=y.shape[0]
x,mu,sigma = featureNormalize(x)
x = np.hstack([x,np.ones((x.shape[0],1))])

theta = np.zeros((3,1))

j = computeCost(x,y,theta)
J_history,theta = gradientDescent(x,y,theta,alpha,iterations)

def predict(data):
    testx = np.array(data)
    testx = ((testx - mu) / sigma)
    testx = np.hstack([testx,np.zeros((testx.shape[0],1))])
    price = testx.dot(theta)
    print('price is %d' % (price))

predict([1650,3])
