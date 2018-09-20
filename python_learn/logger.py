#!/usr/bin/python
# coding:utf-8

import logging.handlers
import logging
import os
import sys

#日志
class logger:
  def set_logger(self,job_name,msg):
    #初始化logger
    log = logging.getLogger()
    #日志格式，可以根据需要设置
    fmt = logging.Formatter('%(asctime)s | Script name is %(filename)s | %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S %p')

    #日志输出到文件，这里用到日志名称，大小，保存个数

    log_path = '/home/admin/PycharmProjects/python/log'
    log_size = 1024*1024*8
    log_num = 3

    #日志文件名：由脚本得名称，结合日志保存路径得到日志文件得绝对路径
    #log_name = os.path.join(log_path,sys.argv[0].split('/')[-1].split('.')[0])
    #job_name = 'dddd'
    log_name = os.path.join(log_path,job_name)

    handle1 = logging.FileHandler(log_name)
    handle1.setFormatter(fmt)
    #同时输出到屏幕，便于观察
    handle2 = logging.StreamHandler(stream=sys.stdout)
    handle2.setFormatter(fmt)
    log.addHandler(handle1)
    log.addHandler(handle2)

    #设置日志为INFO，只有INFO级别以上才会打印
    log.setLevel(logging.INFO)

    log.info(msg)
    log.exception(msg)