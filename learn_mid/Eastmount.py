#!/usr/bin/env python3
'''''
' 这篇代码主要讲述获取MySQL中数据，再进行简单的统计
' 统计采用SQL语句进行 By:Eastmount CSDN
'''

import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import pylab
import pymysql
from pylab import *
from pandas import *


# 根据SQL语句输出24小时的柱状图
try:
    conn = pymysql.connect(host='localhost', user='myuser',
                           passwd='w213486582', port=3306, db='mydb', charset='utf8')
    cur = conn.cursor()  # 数据库游标
    sql = "select HOUR(FBTime) as hh, count(*) as cnt from csdn_blog group by hh;"
    cur.execute(sql)
    result = cur.fetchall()  #获取结果复合纸给result
    hour1 = [n[0] for n in result]
    print(hour1)
    num1 = [n[1] for n in result]
    print(num1)

    N = 23
    ind = np.arange(N)
    width = 0.35
    plt.bar(ind, num1, width, color = 'r', label = 'sum num')
    #设置底部名称
    plt.xticks(ind + width/2, hour1, rotation = 40)
    for i in range(23):
        plt.text(i, num1[i], str(num1[i]), ha = 'center', va = 'bottom', rotation = 45)
    plt.title('Number-24Hour')
    plt.xlabel('hours')
    plt.ylabel('The number of blog')
    plt.legend()
    plt.savefig('08csdn.png',dpi = 400)
    plt.show()

#异常处理
except pymysql.Error as err:
    cur.rollback()
    print("Mysql Error:%s" % (err))
finally:
    cur.close()
    conn.commit()
    conn.close()

#每年每月博客对比
try:
    conn = pymysql.connect(host='localhost', user='myuser',
                           passwd='w213486582', port=3306, db='mydb', charset='utf8')
    cur = conn.cursor()  # 数据库游标
    sql = "select DATE_FORMAT(FBTime,'%Y%m'), count(*) from csdn_blog group by DATE_FORMAT(FBTime,'%Y%m');"
    cur.execute(sql)
    result = cur.fetchall()        #获取结果复合纸给result
    date1 = [n[0] for n in result]
    print (date1 )
    num1 = [n[1] for n in result]
    print (num1 )
    print (type(date1))
    plt.scatter(date1,num1,25,color='white',marker='o',
                edgecolors='#0D8ECF',linewidth=3,alpha=0.8)
    plt.title('Number-12Month')
    plt.xlabel('Time')
    plt.ylabel('The number of blog')
    plt.savefig('02csdn.png',dpi=400)
    plt.show()

#异常处理
except pymysql.Error as err:
    cur.rollback()
    print("Mysql Error:%s" % (err))
finally:
    cur.close()
    conn.commit()
    conn.close()

#通过DataFrame每年每月博客对比
try:
    conn = pymysql.connect(host='localhost', user='myuser',
                           passwd='w213486582', port=3306, db='mydb', charset='utf8')
    cur = conn.cursor()  # 数据库游标
    sql = "select DATE_FORMAT(FBTime,'%Y'), Count(*) from csdn_blog group by DATE_FORMAT(FBTime,'%Y');"
    cur.execute(sql)
    result = cur.fetchall()        #获取结果复合纸给result
    day1 = [n[0] for n in result]
    print (len(day1))
    num1 = [n[1] for n in result]
    print (len(num1),type(num1) )
    matplotlib.style.use('ggplot')
    df=DataFrame(num1, index=day1,columns=['Nums'])
    plt.show(df.plot(kind='bar'))
    plt.savefig('05csdn.png',dpi=400)

#异常处理
except pymysql.Error as err:
    cur.rollback()
    print("Mysql Error:%s" % (err))
finally:
    cur.close()
    conn.commit()
    conn.close()


#时间序列图
try:
    conn = pymysql.connect(host='localhost', user='myuser',
                           passwd='w213486582', port=3306, db='mydb', charset='utf8')
    cur = conn.cursor()  # 数据库游标
    sql = "select DATE_FORMAT(FBTime,'%Y-%m-%d'), Count(*) from csdn_blog group by DATE_FORMAT(FBTime,'%Y-%m-%d');"
    cur.execute(sql)
    result = cur.fetchall()        #获取结果复合纸给result
    day1 = [n[0] for n in result]
    print (len(day1))
    num1 = [n[1] for n in result]
    print (len(num1),type(num1))
    matplotlib.style.use('ggplot')
    #获取第一天
    start = min(day1)
    print (start)
    #np.random.randn(len(num1)) 生成正确图形 正态分布随机数
    ts = pd.Series(np.random.randn(len(num1)),
                   index=pd.date_range(start, periods=len(num1)))
    ts = ts.cumsum()
    ts.plot()
    plt.title('Number-365Day')
    plt.xlabel('Time')
    plt.ylabel('The number of blog')
    plt.savefig('04csdn.png',dpi=400)
    plt.show()

#异常处理
except pymysql.Error as err:
    cur.rollback()
    print("Mysql Error:%s" % (err))
finally:
    cur.close()
    conn.commit()
    conn.close()