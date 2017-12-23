#!/usr/bin/python3
import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('/run/media/admin/0008-276D/data/ml-1m/users.dat',sep = '::',header=None,names = unames)
#print(users)

inames = ['user_id','movie_id','rating','timestamp']
rating = pd.read_table('/run/media/admin/0008-276D/data/ml-1m/ratings.dat',sep = '::',header=None,names = inames)
#print(rating)

rnames = ['movie_id','title','genres']
movies = pd.read_table('/run/media/admin/0008-276D/data/ml-1m/movies.dat',sep = '::',header=None,names = rnames)
#print(movies)

print(users[:5])
print(rating[:5])
print(movies[:5])

data = pd.merge(pd.merge(rating,users),movies)

print(data[:5])
print('输出IX：')
print(data.ix[0:2])
print('聚合测试：')
mean_rating = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
print(mean_rating[:5])
print('分组测试')
ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])

print('输出大于249：')
active_title = ratings_by_title.index[ratings_by_title >= 250]

print(active_title)
print('细项：')
print(mean_rating.ix[active_title])

print('女性最喜欢的电影：')
top_female_rating = mean_rating.sort_index(by = 'F',ascending=False)
top_female_rating[:10]

print('男女分歧最大的电影：')
mean_rating['diff'] = mean_rating['M']-mean_rating['F']
sorted_by_diff = mean_rating.sort_index(by='diff')
print(sorted_by_diff[:15])