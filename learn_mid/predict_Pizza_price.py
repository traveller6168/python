#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model

path = os.getcwd() + '\data\predict_Pizza_data.csv'


def get_data(file_name):
    Pizza_size = []
    Pizza_price = []
    data = pd.read_csv(path)
    print(data)
    for x,y in zip(data['size'],data['price']):
        Pizza_size.append([x])
        Pizza_price.append([float(y)])
    return Pizza_size,Pizza_price

#print(get_data(path))

def predict_Pizza_price(x,y,Pizza_size):
    regr = linear_model.LinearRegression()
    regr.fit(x,y)
    predict_value = regr.predict(Pizza_size)
    print('尺寸%5s  披萨的价格为 %f'% (Pizza_size,predict_value))

x, y = get_data(path)

for i in range(20,30):
    predict_Pizza_price(x,y,i)