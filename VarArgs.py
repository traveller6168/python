#!/usr/bin/env python3
def tupleVarArgs(arg1,arg2='defaultB',*theRest):
    'display regular args and non-keyword variable args'
    print('formal arg 1:',arg1)
    print('formal arg 2:',arg2)
    for eachXtrArg in theRest:
        print('another arg:',eachXtrArg)

tupleVarArgs('abc')
tupleVarArgs(23,4,56)
tupleVarArgs('abc',123,'xyz',456.789)