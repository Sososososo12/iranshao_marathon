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
race_id_len=3295

for index in range(3295,4408):
    p_id = []
    p_name = []
    p_stats = []
    p_result = []
    p_resultinfo = []
    p_comment = []

    race_id =int(race_id_set[index])
    print('正在提取id为'+str(race_id)+' 的赛事信息！')
    participant_einfo=get_participant.getParticipant_num(race_id)
    allparticipant_num_page = participant_einfo[0]
    participant_exist=participant_einfo[1]

    # 需要判断2次，第一次是是否为0，第二次是否为单页
    if allparticipant_num_page!=0:
        for pagenumber in range(1, allparticipant_num_page + 1):
            participant_tuple = get_participant.getParticipant_info(race_id, pagenumber)
            p_id.extend(participant_tuple[0])
            p_name.extend(participant_tuple[1])
            p_stats.extend(participant_tuple[2])
            p_result.extend(participant_tuple[3])
            p_resultinfo.extend(participant_tuple[4])
            p_comment.extend(participant_tuple[5])

            print('已完成载入关注人第 ' + str(pagenumber) + ' 页!')
            time.sleep(3)
    else:
        if participant_exist!=0:
            participant_tuple = get_participant.getParticipant_info(race_id, 1)
            p_id.extend(participant_tuple[0])
            p_name.extend(participant_tuple[1])
            p_stats.extend(participant_tuple[2])
            p_result.extend(participant_tuple[3])
            p_resultinfo.extend(participant_tuple[4])
            p_comment.extend(participant_tuple[5])
            print('已完成载入关注人第1 页!')
            time.sleep(1)
        else:
            p_id.append(str(race_id))
            p_name.append('null')
            p_stats.append('null')
            p_result.append('null')
            p_resultinfo.append('null')
            p_comment.append('null')




    data1 = pd.DataFrame({'id': p_id,
                          'name': p_name,
                          'stats(participating num)': p_stats,
                          'result': p_result,
                          'result_info': p_resultinfo,
                          'comment': p_comment,
                          })
    data1.to_excel(u'./event_participant_new/{}usertest.xls'.format(race_id), index=False, encoding='"utf_8_sig')
    print('id为'+str(race_id)+' 的赛事信息写入完成！'+'\n')


