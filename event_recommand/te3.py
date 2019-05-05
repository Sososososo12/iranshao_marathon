import xlrd
import xlwt
import os
import pandas as pd
import time
from event_recommand import get_user_partinrace
from event_recommand import email_attention

# userlenfilename = r'./event_participant/{}usertest2.xls'.format(str(583))
# user_Fdata = xlrd.open_workbook(filename=userlenfilename)
# sheet1 = user_Fdata.sheet_by_index(0)
# user_id_set = sheet1.col_values(1)
#
# print(user_id_set)
# print(len(user_id_set))
# user_id_set_dup=list(set(user_id_set))
# print(user_id_set_dup)
# print(len(user_id_set_dup))

# num=1000
# filename='./based/test{}.xlsx'.format(str(num))
# if os.path.exists(filename):
#     print(1)
# else:
#     print(0)


dataname = r'./user_done_participant/alluser_filtered.xlsx'
data = xlrd.open_workbook(filename=dataname)
sheet1 = data.sheet_by_index(1)
user_id_set = sheet1.col_values(0)
user_id_len = len(user_id_set)

p_id = []
p_time = []
r_id = []
r_name = []
d_time = []
distance = []
p_speed = []
comment = []
# print('正在创建' + str(startnum) + '至' + str(stopnum) + '的用户赛事参与信息！')
for user_index in range(41480, 41500):
    user_id_test = user_id_set[user_index]
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
    print('已载入第' + str(user_index + 1) + '个用户信息' + 'user_id为：' + user_id_set[user_index] + '\n')
    time.sleep(1)
# id=[1,2,3,4]
# name=['a','b','c','d']
# data=pd.DataFrame({
#     'id':id,
#     'name':name
# })
filename = './user_done_participant/user_partake_info_test{}.xls'.format(str(41500))
if os.path.exists(filename):
    print('已存在文件名：' + 'test{}'.format(str(41500)))
else:
    data = pd.DataFrame({'p_id': p_id,
                         'p_time': p_time,
                         'r_id': r_id,
                         'r_name': r_name,
                         'd_time': d_time,
                         'distance': distance,
                         'p_speed': p_speed,
                         'comment': comment
                         })
    data.to_excel(u'./user_done_participant/user_partake_info_test{}.xls'.format(str(41500)), index=False,
                  encoding='"utf_8_sig')

    print('已创建文件名：' + 'user_partake_info_test{}.xls'.format(str(41500)))
    email_remind = email_attention.mail(41500)
time.sleep(10)

print('已全部创建完成！')
