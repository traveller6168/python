#!/usr/bin/env python3

#数据可视化导入
import urllib
from urllib import request
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
import re
import os

#显示文件下载进度
def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块大小
    c:远程文件大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


#爬取网页内容
def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    return html

#获取文件名
def getFileName(html,file_dir):
    reg = r'<a .*?>(.*(csv|log|txt))</a>'
    file = re.compile(reg)
    html = html.decode('utf-8')
    filelist = re.findall(file,html)
    x = 0
    for filename in filelist:
        file_path = '/run/media/admin/0008-276D/data/'+file_dir+'/'+filename[0]
        fileurl = 'http://aima.cs.berkeley.edu/data/'+filename[0]
        print(file_path)
        request.urlretrieve(fileurl, file_path,Schedule)
        x += 1


html = getHtml("http://aima.cs.berkeley.edu/data/")
print(getFileName(html,'berkeley'))