#!/usr/bin/env python3
from random import randint
def randGen(aList):
    while len(aList) > 0:
        yield aList.pop(randint(0,len(aList)-1))

for item in randGen(['rock','paper','scissors']):
    print(item)