#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

path = os.getcwd() + os.sep + 'data' + os.sep + 'data1.txt'
print(path)
data = pd.read_csv(path,header = None,names = ['Exam_1', 'Exam_2', 'Admitted'])
print(data.head())

positive = data[data['Admitted'] == 1]
negative = data[data['Admitted'] == 0]
fig,ax = plt.subplots(figsize = (10,5))
ax.scatter(positive['Exam_1'],positive['Exam_2'], s=20, c = 'b', marker = 'o', label = 'Admitted')
ax.scatter(negative['Exam_1'],negative['Exam_2'], s=20, c = 'r', marker = 'x', label = 'Not Admitted')
ax.legend()
ax.set_xlabel('Exam_1 Score')
ax.set_xlabel('Exam_2 Score')
plt.show()

def sigmoid(z):
    return 1 / (1 +np.exp(-z))

nums = np.arange(-10, 10 ,step=1)
fiz,ax = plt.subplots(figsize = (10,4))
ax.plot(nums,sigmoid(nums),'r')
plt.show()

def model(X,theta):
    return sigmoid(np.dot(X,theta.T))

data.insert (0,'ones',1)
orig_data = data.as_matrix()
cols = orig_data.shape[1]
X = orig_data[:,0:cols - 1]
y = orig_data[:,cols-1:cols]

theta = np.zeros([1,3])
print(X[:5])
print(y[:5])
print(theta)
print(X.shape,y.shape,theta.shape)

def cost(X,y,theta):
    left = np.multiply(y,np.log(model(X,theta)))
    right = np.multiply(1-y,np.log(1-model(X,theta)))
    return -np.sum(left + right) / (len(X))

print(cost(X,y,theta))


#未完，待续