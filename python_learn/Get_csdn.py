#!/usr/bin/env python3
# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import re
import time
import os
import sys
import codecs
import pymysql

# 打开Firefox浏览器 设定等待加载时间
driver = webdriver.Firefox()
wait = ui.WebDriverWait(driver, 10)


# 获取每个博主的博客页面低端总页码
def getPage():
    print('getPage')
    number = 0
    texts = driver.find_element_by_xpath("//div[@id='papelist']").text
    print('页码', texts)
    #m = re.findall(r'(\w*[0-9]+)\w*', texts)  # 正则表达式寻找数字
    m = re.findall(r'\d+', texts)
    print('页数：' + str(m[1]))
    print(m[1])
    return int(m[1])


# 主函数
def main():
    # 获取txt文件总行数
    count = len(open("C:/Users/zhaowh/PycharmProjects/python/Blog_URL.txt", 'rU').readlines())
    print(count)
    n = 0
    urlfile = open("C:/Users/zhaowh/PycharmProjects/python/Blog_URL.txt", 'r')
    print("URI is : ",)
    # 循环获取每个博主的文章摘信息
    while n < count:  # 这里爬取2个人博客信息，正常情况count个博主信息
        url = urlfile.readline()
        url = url.strip("\n")
        print(url)
        driver.get(url)
        # 获取总页码
        allPage = getPage()
        print(u'页码总数为:', allPage)
        time.sleep(2)

        # 数据库操作结合
        try:
            conn = pymysql.connect(host='localhost', user='myuser',
                                   passwd='w213486582', port=3306, db='mydb',charset='utf8')
            cur = conn.cursor()  # 数据库游标

            # 报错:UnicodeEncodeError: 'latin-1' codec can't encode character
            #conn.set_character_set('utf8')
            #cur.execute('SET NAMES utf8;')
            #cur.execute('SET CHARACTER SET utf8;')
            #cur.execute('SET character_set_connection=utf8;')
            cur.execute('SET NAMES utf8;')
            cur.execute('SET CHARACTER SET utf8;')
            cur.execute('SET character_set_connection=utf8;')
            # 具体内容处理
            m = 1  # 第1页
            while m <= allPage:
                ur = url + "/article/list/" + str(m)
                print(ur)
                driver.get(ur)

                # 标题
                article_title = driver.find_elements_by_xpath("//div[@class='article_title']")
                for title in article_title:
                    # print url
                    con = title.text
                    con = con.strip("\n")
                    # print con + '\n'

                # 摘要
                article_description = driver.find_elements_by_xpath("//div[@class='article_description']")
                for description in article_description:
                    con = description.text
                    con = con.strip("\n")
                    # print con + '\n'

                # 信息
                article_manage = driver.find_elements_by_xpath("//div[@class='article_manage']")
                for manage in article_manage:
                    con = manage.text
                    con = con.strip("\n")
                    # print con + '\n'

                num = 0
                print(u'长度', len(article_title))
                while num < len(article_title):
                    Artitle =article_title[num].text
                    Description = article_description[num].text
                    Manage = article_manage[num].text
                    print("标题：",Artitle)
                    print("描述：",Description)
                    print("信息：",Manage)
                    # 获取作者
                    Author = url.split('/')[-1]
                    # 获取阅读数和评论数
                    mode = re.compile(r'\d+\.?\d*')
                    YDNum = mode.findall(Manage)[-2]
                    PLNum = mode.findall(Manage)[-1]
                    print("阅读量：",YDNum)
                    print("评论数：",PLNum)
                    # 获取发布时间
                    end = Manage.find(u' 阅读')
                    FBTime = Manage[:end]
                    # 插入数据 8个值
                    sql = """insert into csdn_blog (URL,Author,Artitle,Description,Manage,FBTime,YDNum,PLNum) values('%s','%s','%s','%s','%s','%s',%s,%s)""" % (url, Author.replace("'",''), Artitle.replace("'",''), Description.replace("'",''), Manage.replace("'",''), FBTime, YDNum, PLNum)
                    print(sql)
                    print("测试！")
                    cur.execute(sql)

                    num = num + 1
                else:
                    print(u'数据库插入成功')
                m = m + 1

                # 异常处理
        except pymysql.Error as err:
            cur.rollback()
            print("Mysql Error:%s" % (err))
        finally:
            cur.close()
            conn.commit()
            conn.close()

        n = n + 1

    else:
        urlfile.close()
        print('Load Over')


main()