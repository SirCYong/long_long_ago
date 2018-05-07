# coding:utf-8

"""
  Author:  CaoYong
  Purpose: web端下载文件
  Created: 2016年11月24日09:49:43
  downloadWebFile
  写入需要下载的文件名称
  fileName = '51752900000018019.xlsx'
  设置指定的地址
  downloadPath = '/Users/cy/Downloads/'
  设置下载链接的路径
  downloadURL = "http://192.168.6.93/pic/51752900000018019.xlsx"


  Author:  CaoYong
  Purpose: excel行数统计
  Created:2016年11月24日16:17:39
  写入需要统计excel的文件名称
  fileName = '51752900000018019.xlsx'
  设置指定的地址
  downloadPath = '/Users/cy/Downloads/'

"""
import urllib2
import xlrd


def downloadWebFile(URL, path, name):
    a = urllib2.urlopen(URL)
    data = a.read()
    with open(path + name, "wb") as code:
        code.write(data)
    pass


def statisticsExcelNumberOfRows(path, name):
    data = xlrd.open_workbook(path + name)
    table = data.sheets()[0]   # 获得第一个对象 【0】是索引
    a = table.nrows
    print(a)
    pass


# if __name__ == '__main__':
#     downloadWebFile(URL=downloadURL, path=downloadPath, name=fileName)
