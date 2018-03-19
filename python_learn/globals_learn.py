#!/usr/bin/env python3

def foo():
    print('\ncalling foo()...')
    aString = 'bar'
    anInt = 42
    print("foo()'s globals:",globals().keys())
    print("foo()'s locals:",locals().keys())

print("__main__'s glocals:",globals().keys())
print("__main__'s locals:",locals().keys())
foo()