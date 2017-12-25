#!/usr/bin/env python3

def counter(start_at = 0):
    count = [start_at]
    print(count)
    def incr():
        count[0] += 1
        return count[0]
    print(count)
    return incr

count = counter(5)
print(count())