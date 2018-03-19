#!/usr/bin/env python3

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression

path = os.getcwd() + '\data\Folds5x2_pp.csv'
data = pd.read_csv(path)
#print(data.tail())
#print(data.shape)

x = data[['AT','V','AP','RH']]
#print(x.head())

y = data[['PE']]
#print(y.head())

x_train,x_test,y_train,y_test = train_test_split(x,y,random_state = 1)
#print(x_train.shape)
#print(y_train.shape)
#print(x_test.shape)
#print(y_test.shape)

linreg = LinearRegression()
linreg.fit(x_train,y_train)
print(linreg.intercept_)
print(linreg.coef_)

y_pred = linreg.predict(x_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print('MSE:',metrics.mean_squared_error(y_test,y_pred))
# 用scikit-learn计算RMSE
print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

fig,ax = plt.subplots()
ax.scatter(y_test,y_pred)
ax.plot([y_test.min(),y_test.max()],[y_test.min(),y_test.max()],'k--',lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()