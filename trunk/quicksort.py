#!/usr/bin/python3

def quicksort(arr):
    if len(arr) <= 1:
        return  arr
    pivot = arr[int(len(arr) / 2)]
    print ("length:",len(arr)/2,"pivot:", pivot)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1,2,7]))
