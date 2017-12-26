#!/usr/bin/python3
# encoding=utf-8
import os


def dirlist(path, allfile):
    filelist = os.listdir(path)
    result_list = []
    for filename in filelist:
        filepath = os.path.join(path, filename)
        #print(filepath)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
             allfile.append(filepath)
             #print(filepath,filename)
             if 'YO' in filename[0:2].upper():
                  file_desc = open(filepath,'r')
                  file_desc_c = file_desc.read()
                  if 'LISA' in file_desc_c.upper():
                        print (filename,'文件中包含GBASEBAS库\n')
                  else:
                        pass
                  file_desc.close()
    return allfile

print (dirlist("F:\资料\pydata-book-master", []))

