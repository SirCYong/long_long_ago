# -*- coding: utf-8  -*-
"""
Author:Cy

"""
import xlrd

fileName = '/Users/cy/Downloads/test1107.xlsx'
data = xlrd.open_workbook(fileName)
table = data.sheets()[0]
nrows = table.nrows
print(nrows)

# f = open(fileName, 'r')
# path = ""
# lines = f.readlines()
# print (lines)
# n = 0
# with open(fileName) as f:
#     for x in f:
#         n += 1
#     print n
