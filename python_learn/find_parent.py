#!usr/bin/python
#-*- coding: UTF-8 -*-

from multiprocessing import Pool
import queue
import time
import sys
import os


def get_parent_list(id):
    #print (id)
    pid = 9999999999999999
    xid = 9999999999999999
    global break_flag
    break_flag = False
    match_status = 0
    f = open("./findpar.csv")
    while True:
        lines = f.readlines(10)
        if not lines:
            break
        for line in lines:
            #print(line)
            x = line.replace('\n','').split(',')
            #print(x)
            if id == x[0]:
                xid = x[0]
                pid = x[1]
                match_status = x[2]
                #print("找到父级信息")
                #print(line)
                if match_status == '3' and pid == '-1':
                   break_flag = True
                   #print("找到根结点")
                   f.close()
                   #print (xid)
                else:
                   xid = get_parent_list(pid)
            else:
                pass
                #print("未找到父级信息，跳过")
            if break_flag == True:
                break
        if break_flag == True:
            break
    f.close()
    return xid

def get_parent_id():
    file = './test11.txt'
    if os.path.exists(file):
       os.remove(file)
    f = open("./findpar.csv")
    while True:
        lines = f.readlines(2)
        if not lines:
            break
        result_file = open(file, 'a')
        for line in lines:
            #print(line)
            x = line.replace('\n','').split(',')
            #print(x)
            if x[2] == '6':
                #print("查找初匹信息债券信息！")
                #print(line)
                pid = x[1]
                root_pid = get_parent_list(pid)
                print(x,root_pid)
                result_file.write(','.join(x) + ',' + str(root_pid) + "\n" )
                #print("节点 %s,根结点 %s") % (x[0],root_pid)
                #time.sleep(20)
                #sys.exit(0)
            else:
                pass
                #print("初匹信息，跳过")
        result_file.close()
    f.close()

get_parent_id()




