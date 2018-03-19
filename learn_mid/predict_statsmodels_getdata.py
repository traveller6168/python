#!/usr/bin/env python3

import pandas as pd
import urllib
import shutil
import zipfile
import os


data_source = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip' # 网络数据地址
zipname = '/home/admin/PycharmProjects/python/learn_mid/data/Bike-Sharing-Dataset.zip'
data_path = '/home/admin/PycharmProjects/python/learn_mid/data'
urllib.request.urlretrieve(data_source,zipname)

zip_ref = zipfile.ZipFile(zipname,'r')
zip_ref.extractall(data_path)
zip_ref.close()

daily_path = data_path + '/day.csv'
daily_data = pd.read_csv(daily_path)
#print(daily_data.head())
daily_data['dteday'] = pd.to_datetime(daily_data['dteday'])
#print(daily_data.head())
drop_list = ['instant','season','yr','mnth','holiday','workingday', 'weathersit', 'atemp', 'hum']
daily_data.drop(drop_list,inplace = True,axis = 1)
print(daily_data.head())

import statsmodels.api as sm
from statsmodels.stats.outliers_influence import summary_table

x = sm.add_constant(daily_data['temp'])
y = daily_data['cnt']
regr = sm.OLS(y,x)
res = regr.fit()

st,data,ss2 = summary_table(res, alpha=0.05)
fitted_values = data[:,2]
print(fitted_values)