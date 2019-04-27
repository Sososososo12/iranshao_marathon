import os
import urllib3.request
from lxml import etree
import re
import requests
import time
import xlwt
import pandas as pd

participant_site_based = 'http://iranshao.com/people/{}/races'
participant_site_partake = 'http://iranshao.com/people/{}/races?page={}&type=done'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}


def getU_PNum(user_id):
    '''
    获得用户关注赛事的数量值
    :param user_id:
    :return:
    '''
    url = participant_site_based.format(user_id)
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers=headers)
    htmlcontent = r.data.decode('utf-8')
    selector = etree.HTML(htmlcontent)
    participaing_num_str = selector.xpath('//li[@role="presentation"]/a/text()')[1]
    participaing_num = re.findall('参加过\((.*?)\)', participaing_num_str)[0]
    time.sleep(1)
    print('已获取id为 ' + user_id + '的关注赛事总数量!')
    return int(participaing_num)


def get_PHtmlItem(user_id, pagenum):
    '''
    获取该页下用户关注的赛事信息页
    :param p_id:
    :param pagenum:
    :return:
    '''
    url = participant_site_partake.format(user_id, str(pagenum))
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    htmlcontent = r.data.decode('utf-8')
    selector = etree.HTML(htmlcontent)
    r_item = selector.xpath('//div[@class="feed-content"]/div')
    print('已获取第' + str(pagenum) + '页的item信息')
    return r_item


def getU_PTime(itemlist):
    partake_time = []
    for itemnum in range(len(itemlist)):
        p_time_state = itemlist[itemnum].xpath('div[@class="time-header"]/time/text()')
        if p_time_state != []:
            p_time = p_time_state[0]
        else:
            p_time = 'null'
        partake_time.append(p_time)
        print('p_time获取完成')
    return partake_time


def getU_PId(itemlist):
    '''
    获取关注的赛事的id
    :param itemlist:
    :return:
    '''
    id = []
    for itemnum in range(len(itemlist)):
        r_id = itemlist[itemnum].xpath('div/div/h3[@class="entry-title"]/a/@href')[0].replace(r'/races/', '')
        id.append(r_id)
    print('id获取完成')
    return id


def getU_PName(itemlist):
    '''
    获取挂住的赛事名称
    :param itemlist:
    :return:
    '''
    name = []
    for itemnum in range(len(itemlist)):
        r_name = itemlist[itemnum].xpath('div/div/h3[@class="entry-title"]/a/text()')[0]
        name.append(r_name)
    print('name获取完成')
    return name


def getU_PSinfo(itemlist):
    donetime = []
    p_distance = []
    permile_speed = []
    for itemnum in range(len(itemlist)):
        inline_stats = itemlist[itemnum].xpath('div/div/ul[@class="inline-stats"]')[0]
        d_time_state = inline_stats.xpath('li[@title="用时"]/time/text()')
        distance_state = inline_stats.xpath('li[@title="距离"]/text()')
        p_speed_state = inline_stats.xpath('li[@title="配速"]/text()')
        if d_time_state != []:
            d_time = d_time_state[0]
        else:
            d_time = 'null'
        donetime.append(d_time)
        if distance_state != []:
            distance = distance_state[0].replace(' ', '')
        else:
            distance = 'null'
        p_distance.append(distance)
        if p_speed_state != []:
            p_speed = p_speed_state[0]
        else:
            p_speed = 'null'
        permile_speed.append(p_speed)
        print(str(len(itemlist)) + '条参赛信息获取完成')
    return donetime, p_distance, permile_speed


def getU_PComment(itemlist):
    comment = []
    for itemnum in range(len(itemlist)):
        r_comment_state = itemlist[itemnum].xpath('div/div/p/text()')
        if r_comment_state != []:
            r_comment = r_comment_state[0].replace('\n', '').replace(' ', '')
        else:
            r_comment = 'null'
        comment.append(r_comment)
    print('comment获取完成')
    return comment


def getUInfo(user_id):
    '''
    判断关注的赛事数量是否为0：
    若为0，则在listitem中添加用户信息为null；
    若不为0，则在listitem中添加用户信息，一行为单个用户关注的赛事
    :param user_id:
    :return:
    '''
    p_id = []
    partake_time = []
    r_idall = []
    nameall = []
    race_plist1 = []
    race_plist2 = []
    race_plist3 = []
    allcomment = []
    followingnumber = getU_PNum(user_id)
    if followingnumber == 0:
        p_id = [user_id]
        r_idall = ['null']
        partake_time = ['null']
        nameall = ['null']
        race_plist1 = ['null']
        race_plist2 = ['null']
        race_plist3 = ['null']
        allcomment = ['null']
        time.sleep(1)
    else:
        numberall = followingnumber // 4 + 1
        for pagenumber in range(1, numberall + 1):
            item_content = get_PHtmlItem(user_id, pagenumber)
            # 判断该页(pageenumber)中是否存在已参加的赛事，
            # 若不存在，则直接结束本次循环，继续下一次循环
            # 若存在，则继续读取该页中的6维数据
            if item_content == []:
                continue

            p_timex = getU_PTime(item_content)
            idx = getU_PId(item_content)
            namex = getU_PName(item_content)
            scoreinfox = getU_PSinfo(item_content)
            d_timex = scoreinfox[0]
            p_distancex = scoreinfox[1]
            permile_timex = scoreinfox[2]
            commentx = getU_PComment(item_content)

            partake_time.extend(p_timex)
            r_idall.extend(idx)
            nameall.extend(namex)
            race_plist1.extend(d_timex)
            race_plist2.extend(p_distancex)
            race_plist3.extend(permile_timex)
            allcomment.extend(commentx)
            print('该用户第' + str(pagenumber) + '页信息载入完成')
            time.sleep(3)
        for num in range(len(r_idall)):
            p_id.append(user_id)
        print('id：' + user_id + '的用户关注赛事信息已获取完成！' + '共' + str(len(r_idall)) + '条已完成的赛事信息!')
        time.sleep(1)

    return p_id, partake_time, r_idall, nameall, race_plist1, race_plist2, race_plist3, allcomment


# user_id_test = '9891cb3665'
# allinfo = getUInfo(user_id_test)
# allinfolen = [len(allinfo[0]),
#               len(allinfo[1]),
#               len(allinfo[2]),
#               len(allinfo[3]),
#               len(allinfo[4]),
#               len(allinfo[5]),
#               len(allinfo[6]),
#               len(allinfo[7]),
#               ]
# data1 = pd.DataFrame({'p_id': allinfo[0],
#                       'p_time': allinfo[1],
#                       'r_id': allinfo[2],
#                       'r_name': allinfo[3],
#                       'd_time': allinfo[4],
#                       'distance': allinfo[5],
#                       'p_speed': allinfo[6],
#                       'comment': allinfo[7]
#                       })
# data1.to_excel(u'./user_done_participant/user_partake_info_test.xls', index=False, encoding='"utf_8_sig')
# print('测试信息写入完成！')
