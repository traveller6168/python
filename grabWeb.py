#!/usr/bin/env python3

import urllib

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
    else:
        return eachLine

def firstLast(webpage):
    f = open(webpage)
    lines= f.readlines()
    f.close()
    print(firstNonBlank(lines))
    lines.reverse()
    print(firstNonBlank(lines))

def download(url = 'http://www.baidu.com',process=firstLast):
    try:
        retval = urllib.urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:
        process(retval)

if __name__ == '__man__':
    download()