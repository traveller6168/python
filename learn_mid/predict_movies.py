#!/usr/bin/env python3

import csv
import sys
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets,linear_model

file_name = os.getcwd() + '\data\predict_movies_data.csv'
def get_data(file_name):
    data = pd.read_csv(file_name)
    #print(data)
    flash_x_parameter = []
    flash_y_parameter = []
    arrow_x_parameter = []
    arrow_y_parameter = []
    for x1,y1,x2,y2 in zip(data['flash_episode_number'],data['flash_us_viewers'],data['arrow_episode_number'],data['arrow_us_viewers']):
        flash_x_parameter.append([x1])
        flash_y_parameter.append([y1])
        arrow_x_parameter.append([x2])
        arrow_y_parameter.append([y2])
    return flash_x_parameter,flash_y_parameter,flash_x_parameter,arrow_y_parameter

#print(get_data(file_name))

def more_viewers(x1,y1,x2,y2):
    regr1 = linear_model.LinearRegression()
    regr1.fit(x1,y1)
    predicted_value1 = regr1.predict(9)
    print("flash_us_viewers:",predicted_value1)
    regr2 = linear_model.LinearRegression()
    regr2.fit(x2,y2)
    predicted_value2 = regr2.predict(9)
    print('arrow_us_viewers:',predicted_value2)
    if predicted_value1 > predicted_value2:
       print ("The Flash Tv Show will have more viewers for next week")
    else:
       print ("Arrow Tv Show will have more viewers for next week")

x1, y1, x2, y2 = get_data(file_name)
print(x1,': ',y1)
print(x2,': ',y2)
more_viewers(x1, y1, x2, y2)