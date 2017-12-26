#!/usr/bin/python3
# encoding=utf-8
import os


def dirlist(path,var_find_str, allfile, file_result):
    #print("Search strint is:", var_find_str)
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        #print(filepath)
        if os.path.isdir(filepath):
            dirlist(filepath,var_find_str, allfile, file_result)
        else:
            allfile.append(filepath)
            print("Searching File:",filepath, end = '')
            #if 'XML' in filename.upper():
            file_desc = open(filepath, 'rb')
            file_desc_c = file_desc.read()
            #print(str(file_desc_c))
            if var_find_str.upper() in str(file_desc_c).upper():
                file_result.append(filename)
                print("  \033[4;31m exist string: %s\033[0m " %  var_find_str)
            else:
                print("  \033[0;36m isn't exist string: %s\033[0m "%  var_find_str)
                pass
            file_desc.close()
    return allfile, file_result



while True:
    find_str = input("Please input the string you search:\n")
    if find_str == 'quit':
        break
    else:
        return_content = dirlist("/home/admin/PycharmProjects/python",find_str, [], [])
        return_file = list(set(return_content[1]))
        print("The result is :\n")
        for var in return_file:
            print(var)
