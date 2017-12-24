#!/usr/bin/env python3
from functools import reduce

def reduce_me(bin_func,seq,init=None):
    Iseq = list(seq)  #convert to list
    if init is None:  #initializer?
        res = Iseq.pop(0)
    else:
        res = init
    for item in Iseq:
        res = bin_func(res,item)
    return res

def mySum(x,y):return x+y
allNums = range(5)
total = 0
for eachItem in allNums:
    total = mySum(total,eachItem)

print("allNums is:",allNums)
print("The Total is:",total)

print("reduce lambda 测试：",reduce((lambda x,y:x+y), range(5)) )

