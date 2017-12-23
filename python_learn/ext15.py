#!/usr/bin/env python3
from sys import argv
script,filename = argv
txt = open(filename,'r')
file_content = txt.readlines()
print('文件名为：',filename)
for eachLine in file_content:
    print('@@##',eachLine)
txt.close()
print('逐行读取测试完成！')

print('请输入文件名称:\n')
file_again = input('> ')
txt_again = open(file_again)
print(txt_again.read())
