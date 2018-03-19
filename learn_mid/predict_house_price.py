#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model

path = os.getcwd() + '\data\predict_house_data.csv'


def get_data(file_name):
    data = pd.read_csv(path)
    X_parameter = []
    Y_parameter = []
    for single_square_feet,single_price_value in zip(data['square_feet'],data['price']):
        X_parameter.append([float(single_square_feet)])
        Y_parameter.append([float(single_price_value)])
    return X_parameter,Y_parameter



def linear_model_main(X_parameters,Y_parameters,predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters,Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

X, Y = get_data(path)
#print(X)
#print('-------------')
#print(Y)
predictvalue = 700
result = linear_model_main(X, Y, predictvalue)

print ("Intercept value " , result['intercept'])
print ("coefficient" , result['coefficient'])
print ("Predicted value: ",result['predicted_value'])

def show_linear_line(X_parameters,Y_parameters):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters,Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color = 'blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color = 'red',linewidth = 4)
    plt.xticks(())
    plt.yticks(())
    plt.show()

show_linear_line(X,Y)
