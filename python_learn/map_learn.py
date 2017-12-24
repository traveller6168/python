#!/usr/bin/env python3
from random import randint as ri
def odd(n):
    return n+2

def muti(n):
    return n**2

def map_learn(func,seq):
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq

list_val = [ri(1,99) for i in range(9)]
print("原始列表：",list_val)
print("自定义map函数测试：",map_learn(odd,list_val))
print("map函数测试：",list(map((lambda x:x+2),list_val)))

muti_val = range(6)
print("原始列表：",muti_val)
print("自定义map函数测试：",map_learn(muti,muti_val))
print("map函数测试：",list(map((lambda x:x**2),muti_val)))

print("多序列map函数测试：")
print(list(map(lambda x,y:x+y,[1,3,5],[2,4,6])))
print(list(map(lambda x,y:(x+y,x-y),[1,3,5],[2,4,6])))
#print(type(map(None,[1,3,5],[2,4,6]) )  )
print(list(map(int,(1,2,3,4))))
print(list(map(int,'1234')))
print(list(map(int,{1:2,2:3,3:4})))
print(tuple(map(tuple,'agdf')))
print(list('1234'))
print(list((1,2,3,4)))

