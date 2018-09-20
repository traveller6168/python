import os

def mylog(logname,logpath):
    import logging
    # 创建一个日志记录器
    log = logging.getLogger("test_logger")
    log.setLevel(logging.INFO)
    # 创建一个日志处理器
    ## 这里需要正确填写路径和文件名，拼成一个字符串，最终生成一个log文件
    logHandler = logging.FileHandler(filename = logpath+"RiskControlDebugging_"+logname+".log")
    ## 设置日志级别
    logHandler.setLevel(logging.INFO)
    # 创建一个日志格式器
    formats = logging.Formatter('%(asctime)s %(levelname)s: %(message)s',
                datefmt='[%Y/%m/%d %I:%M:%S]')

    # 将日志格式器添加到日志处理器中
    logHandler.setFormatter(formats)
    # 将日志处理器添加到日志记录器中
    log.addHandler(logHandler)
    return log


logname = 'test';logpath = '/home/admin/PycharmProjects/python/log' +os.sep
logger=mylog(logname,logpath)
import sys
try:
    print(1/0)
except:
    logger.exception(sys.exc_info())
    logger.info("Error in dbconfig_file")

f=open('RiskControlDebugging_test.log','r')
print(f.read())