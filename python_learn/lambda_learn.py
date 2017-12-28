#!/usr/bin/env python3
x = 10
def foo():
    y = 5
    bar = lambda z:x+z
    print(bar(y))
    y = 8
    print(bar(y))

foo()

print("下一个练习：")

j,k = 1,2
def proc1():
    j,k = 3,4
    print("j == %d and k == %d" % (j,k))
    k = 5
def proc2():
    j = 6
    proc1()
    print("j == %d and k == %d" % (j,k))

k = 7
proc1()
print("j == %d and k == %d" % (j,k))

j = 8
proc2()
print("j == %d and k == %d" % (j,k))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return(n*factorial(n-1))
print(factorial(2))