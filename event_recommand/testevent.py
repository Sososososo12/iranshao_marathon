import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re
from event_recommand import get_eventinfo

race_id=[]
race_name=[]
race_location=[]
race_score=[]
race_summary=[]
race_followed=[]
race_participant=[]
race_comment=[]
race_diaries=[]
number=0

data = xlrd.open_workbook(filename=r'./race_info_test.xls')
sheet1 = data.sheet_by_index(0)
race_id_set = sheet1.col_values(1)

for idnumber in range(1001,1501):
    racecpinfo_tuple=get_eventinfo.getRaceInfo(int(race_id_set[idnumber]))
    number=number+1
    race_id.append(racecpinfo_tuple[0])
    race_name.append(racecpinfo_tuple[1])
    race_location.append(racecpinfo_tuple[2])
    race_score.append(racecpinfo_tuple[3])
    race_summary.append(racecpinfo_tuple[4])
    race_followed.append(racecpinfo_tuple[5])
    race_participant.append(racecpinfo_tuple[6])
    race_comment.append(racecpinfo_tuple[7])
    race_diaries.append(racecpinfo_tuple[8])
    print('第'+str(number)+'条赛事详细信息已获取完成！'+'\n')
    time.sleep(3)

data1 = pd.DataFrame({'race_id':race_id,
                      'race_name':race_name,
                      'race_location':race_location,
                      'race_score':race_score,
                      'race_summary':race_summary,
                      'race_followed':race_followed,
                      'race_participant':race_participant,
                      'race_comment':race_comment,
                      'race_diaries':race_diaries


                      })
data1.to_excel(u'race_cpinfo_test1500.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')