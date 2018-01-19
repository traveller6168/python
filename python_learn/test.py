#!/usr/bin/env python3
import os
from glob import glob #用到了这个模块
def search_file(pattern, search_path=os.environ['PATH'], pathsep=os.pathsep):
    for path in search_path.split(os.pathsep):
        for match in glob(os.path.join(path, pattern)):
            yield match
if __name__ == '__main__':
    import sys
    if len(sys.argv)<2  or sys.argv[1].startswith('-'):#sys.argv[0]是当前路径,1开始是后面的参数
        print( 'Use: %s <pattern>' % sys.argv[0])
        sys.exit(1)
    if len(sys.argv)>2:
        matchs = list(search_file(sys.argv[1],sys.argv[2]))
    else:
        matchs = list(search_file(sys.argv[1]))
    print( '%d match' % len(matchs))
    for match in matchs:
        print( match)