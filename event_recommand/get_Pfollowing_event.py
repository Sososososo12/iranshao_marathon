import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re

participant_site_based='http://iranshao.com/people/{}/races'
participant_site_following='http://iranshao.com/people/{}/races?page={}&type=follow'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}


def getP_FNum(p_id):
    '''
    获得用户关注赛事的数量值
    :param p_id:
    :return:
    '''
    url = participant_site_based.format(p_id)
    http = urllib3.PoolManager()
    r = http.request('GET', url, headers=headers)
    htmlcontent = r.data.decode('utf-8')
    selector = etree.HTML(htmlcontent)
    following_num_str = selector.xpath('//li[@role="presentation"]/a/text()')[0]
    following_num = re.findall('关注的\((.*?)\)', following_num_str)[0]
    time.sleep(1)
    print('已获取id为 '+p_id +'的关注赛事总数量!')
    return int(following_num)

    # print(int(following_num))

def get_FHtmlItem(p_id,pagenum):
    '''
    获取该页下用户关注的赛事信息页
    :param p_id:
    :param pagenum:
    :return:
    '''
    url = participant_site_following.format(p_id,str(pagenum))
    http = urllib3.PoolManager()
    r = http.request('GET', url,)
    htmlcontent = r.data.decode('utf-8')
    selector = etree.HTML(htmlcontent)
    r_item = selector.xpath('//div[@class="feed-content"]/div/div/div/h3')
    print('已获取第'+str(pagenum)+'页的item信息')
    return r_item

def getP_FId(itemlist):
    '''
    获取关注的赛事的id
    :param itemlist:
    :return:
    '''
    id = []
    for itemnum in range(len(itemlist)):
        r_id = itemlist[itemnum].xpath('a/@href')[0].replace(r'/races/', '')
        id.append(r_id)
    print('id获取完成')
    return id

def getP_FName(itemlist):
    '''
    获取挂住的赛事名称
    :param itemlist:
    :return:
    '''
    name=[]
    for itemnum in range(len(itemlist)):
        r_name = itemlist[itemnum].xpath('a/text()')[0]
        name.append(r_name)
    print('name获取完成')
    return name

def getPFInfo(user_id):
    '''
    判断关注的赛事数量是否为0：
    若为0，则在listitem中添加用户信息为null；
    若不为0，则在listitem中添加用户信息，一行为单个用户关注的赛事
    :param user_id:
    :return:
    '''
    p_id = []
    idall = []
    nameall = []
    followingnumber = getP_FNum(user_id)
    if followingnumber==0:
        p_id=[user_id]
        idall = ['null']
        nameall = ['null']
        time.sleep(1)
    else:
        numberall = followingnumber // 4 + 1
        for pagenumber in range(1, numberall + 1):
            item_content = get_FHtmlItem(user_id, pagenumber)
            idx = getP_FId(item_content)
            namex = getP_FName(item_content)
            idall.extend(idx)
            nameall.extend(namex)
            print('该用户第' + str(pagenumber) + '页信息载入完成')
            time.sleep(1)
        for num in range(followingnumber):
            p_id.append(user_id)
        print('id：' + user_id + '的用户关注赛事信息已获取完成！')
        # time.sleep(1)

    return p_id,idall,nameall




