#!/usr/bin/python3

import os
for tmpdir in ('/home/admin/PycharmProjects/test/tmp',r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
    else:
        print ('no temp directory available')
        tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print('*** current tmporary directory')
    print(cwd)
    print('*** new working directory:')
    print(os.listdir(cwd))
    print('*** createing test file...')
    fobj = open('test','w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()
    print('*** update directory listing:')
    print(os.listdir(cwd))
    print("*** renaming 'test' to 'filetest.txt'")
    os.renames('test','filetest.txt')
    print('*** updated directory listing:')
    print(os.listdir(cwd))
    path = os.path.join(cwd,os.listdir(cwd)[0])
    print('*** full file pathname')
    print(path)
    print('***(pathname,basename) == ')
    print(os.path.split(path))
    print('*** (filename,extension) == ')
    print(os.path.splitext(os.path.basename(path)))

    print('*** displaying file contents: ')
    fobj = open(path)
    for eachLine in fobj:
        print(eachLine)
    fobj.close()

    print('*** deleting test file')
    os.remove(path)
    print('*** updated diredctory listing: ')
    print(os.listdir(cwd))
    os.chdir(os.pardir)
    print('*** deleting test directory')
    os.rmdir('example')
    print('*** DONE')
