#!/usr/bin/python3

'''
An example if rading and writing Unicode string:Writes
a Unicode string to a file in utr-8 and reads it back in.
'''

CODE = 'utf-8'
FIlE = 'unicode.txt'

hello_out = u"Hello World\n"
bytes_out = hello_out.encode(CODE)
f = open(FIlE,'w')
f.write(hello_out)
f.close()

f = open(FIlE,'rb')
bytes_in = f.read()
f.close()
#print(bytes_in)
hello_in = bytes_in.decode(encoding=CODE)
print(hello_in)