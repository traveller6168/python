#!/usr/bin/python3

'readTextFile.py  --  read and display text file'
#get filename
fname = input('Enter filename:')
print(fname)

# attempt to open file for reading C:/Users/zhaowh/PycharmProjects/untitled/自动化运维.sql
try:
    fobj = open(fname,'r')
except:
    print ("*** file open error:")
else:
    # display contents to the screen
    for eachLine in fobj:
        print(eachLine)
    fobj.close()