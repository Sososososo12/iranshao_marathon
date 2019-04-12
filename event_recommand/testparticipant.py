import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
from event_recommand import get_participant


data = xlrd.open_workbook(filename=r'./based/race_info_based.xls')
sheet1 = data.sheet_by_index(0)
race_id_set = sheet1.col_values(1)

for index in range(2,21):
    p_id = []
    p_name = []
    p_stats = []
    p_result = []
    p_resultinfo = []
    p_comment = []

    race_id =int(race_id_set[index])
    print('正在提取id为'+str(race_id)+' 的赛事信息！')
    allparticipant_num = get_participant.getParticipant_num(race_id)

    for pagenumber in range(1, allparticipant_num + 1):
        participant_tuple = get_participant.getParticipant_info(race_id,pagenumber)
        p_id.extend(participant_tuple[0])
        p_name.extend(participant_tuple[1])
        p_stats.extend(participant_tuple[2])
        p_result.extend(participant_tuple[3])
        p_resultinfo.extend(participant_tuple[4])
        p_comment.extend(participant_tuple[5])

        print('已完成载入关注人第 ' + str(pagenumber) + ' 页!')
        time.sleep(3)

    data1 = pd.DataFrame({'id': p_id,
                          'name': p_name,
                          'stats(participating num)': p_stats,
                          'result': p_result,
                          'result_info': p_resultinfo,
                          'comment': p_comment,
                          })
    data1.to_excel(u'{}usertest.xls'.format(race_id), index=False, encoding='"utf_8_sig')
    print('id为'+str(race_id)+' 的赛事信息写入完成！')



