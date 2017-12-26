#!/usr/bin/python3
# encoding=utf-8
import os


def dirlist(path, allfile,file_result):
    filelist = os.listdir(path)
    result_list = []
    for filename in filelist:
        filepath = os.path.join(path, filename)
        #print(filepath)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile,file_result)
        else:
             allfile.append(filepath)
             file_result.append(filename)
             #print(filepath,filename)
             if 'YO' in filename[0:2].upper():
                  file_desc = open(filepath,'r')
                  file_desc_c = file_desc.read()
                  if 'LISA' in file_desc_c.upper():
                        print (filename,'文件中包含GBASEBAS库\n')
                        result_list.append(filename)
                  else:
                        pass
                  file_desc.close()
    print(result_list)
    return allfile,file_result

print (dirlist("F:\资料\pydata-book-master", [],[]))
return_content = dirlist("F:\资料\pydata-book-master", [],[])
return_file = list(set(return_content[1]))
print("结果文件\n",return_file)