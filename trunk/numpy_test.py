#!/usr/bin/python3

import numpy as np
a = np.array([1,2,3])
print(type(a))
print(a.shape)
print(a[0],a[1],a[2])
a[0]=5
print(a)

print("test array B")
b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)
print(b[0,0],b[0,1],b[1,0])

print("test other:")
a = np.zeros((2,2))
print(a)
a = np.zeros(2)
print(a)

print("dddd:")
b = np.ones((1,2))
print(b)
b = np.ones(9)
print(b)

print("gggg:")
c = np.full((2,3),5)
print(c)

print("dddwww:")
d = np.eye(5,5,6)
print(d)

a = np.array([[1,2,3],[4,5,6]])
a.shape = (3,2)
print(a)

print("gggggg:")
a = np.arange(24)
print(a)
a.ndim
b = a.reshape(2,4,3)
print(b)