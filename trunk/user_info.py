#!/usr/bin/env python3

try:
  user_file = open('/run/media/admin/0008-276D/data/ml-1m/users.dat','r')
  for user_info in user_file:
      print(user_info,user_info.split('::'))
except IOError:
  print('Open file error')

with open('/run/media/admin/0008-276D/data/ml-1m/movies.dat','br') as f:
    for eachLine in f:
        print(eachLine)