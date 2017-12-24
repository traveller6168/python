#!/usr/bin/env python3
from random import randint
from random import randint as ri
def fillter(bool_func,seq):
    filtered_seq = []
    for eachItem in seq:
        if bool_func(eachItem):
            filtered_seq.append(eachItem)
    return filtered_seq

def odd(n):
    return n % 2

allNums = []
for eachNum in range(9):
    allNums.append(randint(1,99))


print ("filter 函数测试：",list(filter(odd,allNums)))
print ("其他函数测试:",fillter(odd,allNums))
print ("filter～lambda 函数测试：",list(filter(lambda n:n%2,allNums)))
print("其他写法测试：",[n for n in allNums if n % 2])
print("简化写法测试：",[n for n in [ri(1,99) for i in range(9)] if n % 2])
print("写法测试：",[n for n in [ri(1,200) for i in range(10)] if n % 3])