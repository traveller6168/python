#!/usr/bin/env python3

# this one is like your script with argv
def print_two(*args):
    arg1,arg2 = args
    print("arg1:%r, arg2:%r" % (arg1,arg2))

#ok,thar *args is actually pointless,we can just do like this
def print_two_again(arg1,arg2):
    print("arg1:%r, arg2:%r" % (arg1,arg2))

#this just takes one argument
def print_one(arg1):
    print("arg1:%r" % (arg1))

#this one takes no arguments
def print_none():
    print("I got nothings.")

print("call print_two():")
print_two("Zed","Shaw")
print("call print_two_again():")
print_two_again("Zed","Shaw")
print("call print_one():")
print_one("Zed")
print("call print_none()")
print_none()