#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model
from sklearn.cross_validation import train_test_split

path = os.getcwd() + '\data\predict_house_data.csv'
data = pd.read_csv(path)
X = data[['square_feet']]
Y = data[['price']]
#print(X)
#print(Y)

x_train,x_test,y_train,y_test = train_test_split(X, Y,random_state= 1)
linereg = linear_model.LinearRegression()
linereg.fit(x_train,y_train)
print(linereg.intercept_)
print(linereg.coef_)

y_pred = linereg.predict(x_test)
print('预测值：',x_test,y_pred)

from sklearn import metrics
# 用scikit-learn计算MSE
print('MSE:',metrics.mean_squared_error(y_test,y_pred))
# 用scikit-learn计算RMSE
print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))