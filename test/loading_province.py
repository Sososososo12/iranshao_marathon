import requests
from lxml import etree
import pandas as pd
import time
import xlrd

provincefile=xlrd.open_workbook(r'D:\py project\iranshao_marathon\url of provinces.xls')
# print(provincefile.sheet_names())

sheet=provincefile.sheet_by_index(0)
cols1=sheet.col_values(0)
cols3=sheet.col_values(2)
# print(type(cols))
cols1.remove(cols1[0])
cols3.remove(cols3[0])
# print(len(cols))
provinces=cols3
names=cols1

# print(names[2])
# print(provinces[2])