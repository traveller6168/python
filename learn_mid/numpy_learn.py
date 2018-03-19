#!/usr/bin/env python3

import numpy as np

data1 = [6,7.5,8,0,1]
arr1 = np.array(data1)
print(arr1)

data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(data2)

print(arr2.ndim,arr2.shape,arr2.dtype)
print(np.zeros(10))
print(np.zeros((3,6)))
print(np.empty((2,3,3)))
print(np.arange(15))

arr = np.arange(10)
print(arr)
print(arr[5],'dd',arr[5:8])
arr[5:8] = 12
print(arr)

arr_slice = arr[5:8]
print(arr_slice)
arr_slice[1] = 12345
print(arr_slice)
arr_slice[:] = 64
print(arr_slice)
print(arr)

arr3d = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print("test")
print(arr3d)
print("uid")
print(arr3d[0])
print('PWE')
old_values = arr3d[0].copy()
print(old_values)
arr3d[0] = 42
print("dd")
print(arr3d)
arr3d[0] = old_values
print('QWWWW')
print(arr3d)

print("OO")
print(arr[1:6])
print("LLL")
print(arr2)