#!/usr/bin/env python3

from operator import add,mul
from functools import partial

def sum(*args):
    s = 0
    for n in args:
        s = s + n
    return  s

add1 = partial(add,1)
mul100 = partial(mul,100)
sum_5_10 = partial(sum,5,10)

print(add1(100))
print(mul100(20))
print(sum_5_10())

