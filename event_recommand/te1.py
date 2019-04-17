import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re
from event_recommand import get_Pfollowing_event

# a1=[]
# a2=[]
# a3=[]
# a=([1,2,3],['a','b','c'],['as','as','as'])
# # print(a)
# a1.extend(a[0])
# a2.extend(a[1])
# a3.extend(a[2])
# print(a1,a2,a3)

startnum = 2001
stopnum = 2501

# for inum in range(1, 20):
#     if stopnum>7984:
#         stopnum=7984
#         print(startnum, stopnum, inum)
#         break
#     print(startnum, stopnum,inum)
#
#     startnum = startnum + 500
#     stopnum = stopnum + 500


#
#
# data = xlrd.open_workbook(filename=r'./based/583participant.xlsx')
# sheet1 = data.sheet_by_index(2)
# user_id_set = sheet1.col_values(0)
# print(user_id_set[7983])

# a=[1,2]
# list=[]
# for i in range(1,len(a)):
#     list.append(a[i])
# print(list)
#
# a=[[1,2,4],['a','d','asd']]
# print(a[1][2])

# a=(1,2)
# x=4
# y=3
# a=(x,y)
# print(a)