#!/usr/bin/python
# coding:utf-8

import logging.handlers
import logging
import os
import sys

#日志
class logger:
    log_path = '/home/admin/PycharmProjects/python/log'
    log_size = 1024*1024*8
    log_num = 3

    #日志文件名：由脚本得名称，结合日志保存路径得到日志文件得绝对路径
    log_name = os.path.join(log_path,sys.argv[0].split('/')[-1].split('.')[0])

    #初始化logger
    log = logging.getLogger()
    #日志格式，可以根据需要设置
    fmt = logging.Formatter('%(asctime)s | Script name is %(filename)s | %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S %p')

    #日志输出到文件，这里用到日志名称，大小，保存个数
    handle1 = logging.handlers.RotatingFileHandler(log_name,maxBytes=log_size,backupCount=log_num)
    handle1.setFormatter(fmt)
    #同时输出到屏幕，便于观察
    handle2 = logging.StreamHandler(stream=sys.stdout)
    handle2.setFormatter(fmt)
    log.addHandler(handle1)
    log.addHandler(handle2)

    #设置日志为INFO，只有INFO级别以上才会打印
    log.setLevel(logging.INFO)

    #日志接口，用户只需调用此接口即可,这里只定位了INFO, WARNING, ERROR三个级别的日志，可根据需要定义更多接口
    @classmethod
    def info(cls,msg):
        cls.log.info(msg)
        return

    @classmethod
    def warning(cls,msg):
        cls.log.warning(msg)
        return

    @classmethod
    def error(cls,msg):
        cls.log.error(msg)
        return


