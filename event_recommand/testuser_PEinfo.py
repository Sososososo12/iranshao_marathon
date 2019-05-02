import os
import urllib3.request
from lxml import etree
import re
import requests
import time
import xlrd
import pandas as pd
from event_recommand import get_user_partinrace


filename = r'./user_done_participant/alluser_filtered.xlsx'
data = xlrd.open_workbook(filename=filename)
sheet1 = data.sheet_by_index(1)
user_id_set = sheet1.col_values(0)
user_id_len = len(user_id_set)

p_id=[]
p_time=[]
r_id=[]
r_name=[]
d_time=[]
distance=[]
p_speed=[]
comment=[]
for user_index in range(15000,20000):
    user_id_test=user_id_set[user_index]
    allinfo = get_user_partinrace.getUInfo(user_id_test)
    allinfolen = [len(allinfo[0]),
                  len(allinfo[1]),
                  len(allinfo[2]),
                  len(allinfo[3]),
                  len(allinfo[4]),
                  len(allinfo[5]),
                  len(allinfo[6]),
                  len(allinfo[7]),
                  ]
    p_id.extend(allinfo[0])
    p_time.extend(allinfo[1])
    r_id.extend(allinfo[2])
    r_name.extend(allinfo[3])
    d_time.extend(allinfo[4])
    distance.extend(allinfo[5])
    p_speed.extend(allinfo[6])
    comment.extend(allinfo[7])
    print('已载入第' + str(user_index+1) + '个用户信息' + 'user_id为：' + user_id_set[user_index] + '\n')
    time.sleep(1)

data1 = pd.DataFrame({'p_id': p_id,
                      'p_time': p_time,
                      'r_id': r_id,
                      'r_name': r_name,
                      'd_time': d_time,
                      'distance': distance,
                      'p_speed': p_speed,
                      'comment': comment
                      })
data1.to_excel(u'./user_done_participant/user_partake_info_test20000.xls', index=False, encoding='"utf_8_sig')
print('测试信息写入完成！')
