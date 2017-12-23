#!/usr/bin/env python3

def testit(func,*nkwargs,**kwargs):
    try:
        retval = func(*nkwargs,**kwargs)
        result = (True,retval)
    except (Exception):
        result = (False)
    return result

def test():
    funcs = (int,float)
    vals = (1234,12.34,'1234','12.34')

    for eachFunc in funcs:
        print('_'*20)
        for eachVal in vals:
            retval = testit(eachFunc,eachVal)
            if retval[0]:
                print('%S(%S) = FAILED:' % (eachFunc.__name__,'eachVal'),retval[1])

if __name__ == 'main__':
    test()