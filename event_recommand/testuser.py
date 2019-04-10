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

user_id=[]
event_id=[]
event_name=[]
participant_site_based='http://iranshao.com/people/{}/races'
participant_site_following='http://iranshao.com/people/{}/races?page={}&type=follow'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}

data = xlrd.open_workbook(filename=r'./based/583participant.xlsx')
sheet1 = data.sheet_by_index(2)
user_id_set = sheet1.col_values(0)

number=0
for num in range(1,501):
    number=number+1
    user_info = get_Pfollowing_event.getPFInfo(user_id_set[num])
    # 运行后返回的是个tuple，里面是多个返回的值（list）
    # 给每一个总list加上读取到的tuple中的对应list
    user_id.extend(user_info[0])
    event_id.extend(user_info[1])
    event_name.extend(user_info[2])
    print('已载入第'+str(number)+'个用户信息'+'\n')

data1 = pd.DataFrame({'p_id':user_id,
                      'id':event_id,
                      'name':event_name,

                      })
data1.to_excel(u'acc_info_test500.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')