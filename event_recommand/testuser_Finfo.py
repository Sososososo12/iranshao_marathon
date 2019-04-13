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

input_race_id=597
filename=r'./event_participant/{}usertest.xls'.format(str(input_race_id))
data = xlrd.open_workbook(filename=filename)
sheet1 = data.sheet_by_index(2)
user_id_set = sheet1.col_values(0)
user_id_len=len(user_id_set)
startnum = 1
stopnum = 501


for num in range(1,user_id_len):
    user_info = get_Pfollowing_event.getPFInfo(user_id_set[num])
                # 运行后返回的是个tuple，里面是多个返回的值（list）
                # 给每一个总list加上读取到的tuple中的对应list
    user_id.extend(user_info[0])
    event_id.extend(user_info[1])
    event_name.extend(user_info[2])
    print('已载入第' + str(num) + '个用户信息' + '\n')

data1 = pd.DataFrame({'p_id': user_id,
                      'id': event_id,
                      'name': event_name,
                    })
data1.to_excel(u'/yuan/{}_info_test.xls'.format(str(input_race_id)), index=False, encoding='"utf_8_sig')
print('id为'+str(input_race_id)+'的用户信息写入完成！')

# for inum in range(1, 20):
#     if stopnum>user_id_len:
#         stopnum=user_id_len
#         for num in range(startnum, stopnum):
#             # number = number + 1
#             user_info = get_Pfollowing_event.getPFInfo(user_id_set[num])
#             # 运行后返回的是个tuple，里面是多个返回的值（list）
#             # 给每一个总list加上读取到的tuple中的对应list
#             user_id.extend(user_info[0])
#             event_id.extend(user_info[1])
#             event_name.extend(user_info[2])
#             print('已载入第' + str(num) + '个用户信息' + '\n')
#
#         data1 = pd.DataFrame({'p_id': user_id,
#                               'id': event_id,
#                               'name': event_name,
#
#                               })
#         data1.to_excel(u'acc_info_test{}.xls'.format(str(stopnum)), index=False, encoding='"utf_8_sig')
#         print('截止'+str(stopnum)+'条用户的关注信息写入完成！')
#         break
#
#     for num in range(startnum, stopnum):
#         # number = number + 1
#         user_info = get_Pfollowing_event.getPFInfo(user_id_set[num])
#         # 运行后返回的是个tuple，里面是多个返回的值（list）
#         # 给每一个总list加上读取到的tuple中的对应list
#         user_id.extend(user_info[0])
#         event_id.extend(user_info[1])
#         event_name.extend(user_info[2])
#         print('已载入第' + str(num) + '个用户关注信息' + '\n')
#
#     data1 = pd.DataFrame({'p_id': user_id,
#                           'id': event_id,
#                           'name': event_name,
#
#                           })
#     data1.to_excel(u'/yuan/{}_info_test{}.xls'.format(str(input_race_id,stopnum)), index=False, encoding='"utf_8_sig')
#     print('截止'+str(stopnum-1)+'条用户信息写入完成！')
#
#     startnum = startnum + 500
#     stopnum = stopnum + 500
#     time.sleep(10)

