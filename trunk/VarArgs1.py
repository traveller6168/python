#!/usr/bin/env python3

def dictVarArgs(arg1,arg2='defaultB',*nkw,**theRest):
    'display 2 regular args and keyword variable args'
    print('formal arg1:',arg1)
    print('formal arg2:',arg2)
    for eachNkw in nkw:
        print('additional non-keyword arg:',eachNkw)
    for eachXtrArg in theRest.keys():
        print('Xtra arg %s:% s' % (eachXtrArg,str(theRest[eachXtrArg])))

dictVarArgs(1220, 740.0, c='grail')

dictVarArgs(arg2='tales',c=123,d='poe',arg1='mystery')

print('new test:')

dictVarArgs('ttt','222',*('111','221','kl'),c=2213,d='poe')
