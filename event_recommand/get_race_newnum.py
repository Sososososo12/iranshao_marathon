import os
import urllib3.request
from lxml import etree
import re
import requests
import time
import xlrd
import pandas as pd

race_site_based = 'http://iranshao.com/races/{}'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}


def getRaceinfo(race_oid):
    race_nid = ''
    race_nname = ''

    race_ourl = race_site_based.format(str(race_oid))
    html_old = requests.get(race_ourl, allow_redirects=False)
    html_status = html_old.status_code
    if html_status == 200:
        race_nid = str(race_oid)
        race_nname = 'similar with old'
    elif html_status == 301:
        html_headers = html_old.headers
        race_nid = html_headers['Location'].replace('http://iranshao.com/races/', '')
        race_url = race_site_based.format(str(race_nid))
        html = requests.get(race_url).content.decode('utf-8')
        selector = etree.HTML(html)
        race_website_state = selector.xpath('//div[@class="racememu hidden-xs"]/div/h1')
        if race_website_state != []:
            race_name_state = selector.xpath('//div[@class="racememu hidden-xs"]/div/h1/a/text()')
            if race_name_state != []:
                race_nname = race_name_state[0].replace('\n', '').replace(' ', '')
            else:
                n = 'null'
            # event_location_state = selector.xpath('//div[@class="race-his"]/p/text()')
            # if event_location_state != []:
            #     event_location = event_location_state[0].replace('\n', '').replace(' ', '')
            # else:
            #     event_location = 'null'
            # event_score = selector.xpath('//section[@class="race-scores"]/div/span/@data-score')[0]
            # event_summary_state = selector.xpath('//div[@class="race-info"]/p/text()')
            # if event_summary_state != []:
            #     event_summary = event_summary_state[0]
            # else:
            #     event_summary = 'null'
            # event_followed = selector.xpath('//div[@class="race-menbers"]/p/span/em/text()')[0]
            # event_participant = selector.xpath('//div[@class="race-menbers"]/p/span/em/text()')[1]
            # event_comment_state = selector.xpath('//div[@id="racecomments"]/div/h2/span/a/span/text()')
            # if event_comment_state != []:
            #     event_comment = event_comment_state[0]
            # else:
            #     event_comment = '赛事评论少于5条'
            # event_diaries_state = selector.xpath('//div[@id="racediary"]/div/h2/span/a/span/text()')
            # if event_diaries_state != []:
            #     event_diaries = event_diaries_state[0]
            # else:
            #     event_diaries = selector.xpath('//div[@id="racediary"]/div/h2/span/span/text()')[0]
        else:
            race_nname = 'null'
            # event_location = 'null'
            # event_score = 'null'
            # event_summary = 'null'
            # event_followed = 'null'
            # event_participant = 'null'
            # event_comment = 'null'
            # event_diaries = 'null'
            print('赛事id为' + str(race_oid) + ' 的 最新赛事id信息已获取完成！')

    return race_nid, race_nname


filename = r'./user_done_participant/all_based_partipant - step3.xlsx'
data = xlrd.open_workbook(filename=filename)
sheet1 = data.sheet_by_index(2)
race_oldid_set = sheet1.col_values(0)
race_oldid_len = len(race_oldid_set)
race_oname_set = sheet1.col_values(1)

stopnum = 501
for stopnum in range(501, race_oldid_len, 500):
    startnum = stopnum - 500
    r_oid = []
    r_oname = []
    r_nid = []
    r_nname = []

    for race_oindex in range(startnum, stopnum):
        nrace_info = getRaceinfo(race_oldid_set[race_oindex])
        r_oid.append(str(race_oldid_set[race_oindex]))
        r_oname.append(str(race_oname_set[race_oindex]))
        r_nid.append(nrace_info[0])
        r_nname.append(nrace_info[1])
        print(str(race_oindex) + ': 已载入第' + str(race_oindex) + '个赛事信息，Oid为：' + str(race_oldid_set[race_oindex]))
        time.sleep(1)

    filename = './user_done_participant/race_info_update{}.xls'.format(str(stopnum))
    if os.path.exists(filename):
        print('已存在文件名：' + 'test{}'.format(str(stopnum)))
    else:
        data1 = pd.DataFrame({'r_oid': r_oid,
                              'r_oname': r_oname,
                              'r_nid': r_nid,
                              'r_nname': r_nname,

                              })
        data1.to_excel(u'./user_done_participant/race_info_update{}.xls'.format(str(stopnum)), index=False,
                       encoding='"utf_8_sig')
        print('已创建文件名：' + 'race_info_update{}.xls'.format(str(stopnum)))

for race_oindex in range(5501, race_oldid_len):
    nrace_info = getRaceinfo(race_oldid_set[race_oindex])
    r_oid.append(str(race_oldid_set[race_oindex]))
    r_oname.append(str(race_oname_set[race_oindex]))
    r_nid.append(nrace_info[0])
    r_nname.append(nrace_info[1])
    print(str(race_oindex) + ': 已载入第' + str(race_oindex) + '个赛事信息，Oid为：' + str(race_oldid_set[race_oindex]))
    time.sleep(1)

filename = './user_done_participant/race_info_update{}.xls'.format(str(race_oldid_len))
if os.path.exists(filename):
    print('已存在文件名：' + 'test{}'.format(str(race_oldid_len)))
else:
    data1 = pd.DataFrame({'r_oid': r_oid,
                          'r_oname': r_oname,
                          'r_nid': r_nid,
                          'r_nname': r_nname,

                          })
    data1.to_excel(u'./user_done_participant/race_info_update{}.xls'.format(str(race_oldid_len)), index=False,
                   encoding='"utf_8_sig')
    print('已创建文件名：' + 'race_info_update{}.xls'.format(str(race_oldid_len)))

print('测试信息写入完成！')
