#!/usr/bin/ python3
import pandas as pd
names1880 = pd.read_csv('/names/yob1880.txt',names = ['name','sex','births'])
print(names1880)
print("按性别统计：\n",names1880.groupby('sex').births.sum())

years = range(1880,2011)
pieces = []
columns = ['name','sex','births']
for year in years:
    path = '/names/yob%d.txt' % year
    frame = pd.read_csv(path,names = columns)
    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces,ignore_index = True)
total_births = names.pivot_table('births',rows = 'year',cols = 'sex',aggfunc = sum)
total_births.tail()

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births /births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)
print(names)


