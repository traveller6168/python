#!/usr/bin/env python3

import os
if __name__ == '__mian__':
    print('current Process (%s) start ... ' %(os.getpid()))
    pid = os.fork()
    if pid < 0:
        print('error in fork')
    elif pid == 0:
        print('I am child process(%s) and my parent process is (%s)' % (os.getpid(),os.getppid()))
    else:
        print('I(%s) created a child process(%s).',(os.getpid(),pid))