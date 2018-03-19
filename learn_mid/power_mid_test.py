#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,linear_model
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict

data = pd.read_csv('.\Folds5x2_pp.csv')
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

predicted = cross_val_predict(linreg,x,y,cv = 10)

y_pred = linreg.predict(x_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print('MSE:',metrics.mean_squared_error(y,predicted))
# 用scikit-learn计算RMSE
print('RMSE:',np.sqrt(metrics.mean_squared_error(y,predicted)))
fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()