#!/usr/bin/env python3

a = lambda x,y=2:x+y
print(a(3))
print(a(3,5))
print(a(0))
print(a(0,9))
print(a('we',' are differrence!'))

b = lambda *z:z
print(b(23,'zyx'))
print(b(42))

c = lambda **x:x
print(c(x = '1',y = 33,g = '$#@'))

d = lambda *x:x
print(d(23,4))