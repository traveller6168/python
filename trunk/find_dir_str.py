#!/usr/bin/python3
# encoding=gbk
import os


def dirlist(path,var_find_str, allfile, file_result):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        # print(filepath)
        if os.path.isdir(filepath):
            dirlist(filepath,var_find_str, allfile, file_result)
        else:
            allfile.append(filepath)
            # print(filepath,filename)
            # if '_02047_' in filename[0:2].upper():
            file_desc = open(filepath, 'r')
            file_desc_c = file_desc.read()
            if var_find_str.upper() in file_desc_c.upper():
                # print (filename,'文件中包含GBASEBAS库\n')
                file_result.append(filename)
            else:
                pass
            file_desc.close()
    # print(result_list)
    return allfile, file_result



while True:
    find_str = input("请输入要查找的字段：\n")
    # print (dirlist("/gpfs/yijing/download/", [],[]))
    if find_str == 'quit@':
        break
    else:
        return_content = dirlist("F:\资料\pydata-book-master\ch02",find_str, [], [])
        return_file = list(set(return_content[1]))
        print("结果文件\n", return_file)
