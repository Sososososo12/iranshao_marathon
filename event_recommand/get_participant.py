import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time

article_site_based = 'http://iranshao.com/races/{}/racers?page={}&type=done'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}


def getParticipant_num(race_id):
    race_partcipate_page = article_site_based.format(str(race_id), '1')
    html = requests.get(race_partcipate_page).content
    selector = etree.HTML(html.decode('utf-8'))
    participant_page_num = selector.xpath('//ul[@class="pagination pagination-v1"]/li/a/text()')
    if participant_page_num!=[]:
        all_page_num = int(participant_page_num[-2])
    else:
        all_page_num=0
    return all_page_num


def getParticipant_info(race_id, pagenum):
    id = []
    name = []
    stats = []
    result = []
    result_info = []
    comment = []

    race_partcipate_page = article_site_based.format(str(race_id), str(pagenum))
    html = requests.get(race_partcipate_page,headers=headers).content
    selector = etree.HTML(html.decode('utf-8'))
    # paticipant_page_num = selector.xpath('//ul[@class="pagination pagination-v1"]/li/a/text()')
    particpant_item = selector.xpath('//ol[@class="menber-cards"]/li')
    for particpant in particpant_item:
        p_id = particpant.xpath('div[@class="menber-info"]/h2/a/@href')[0].replace('/people/', '')
        p_name = particpant.xpath('div[@class="menber-info"]/h2/a/text()')[-1].replace('\n', '').replace(' ', '')
        p_stats = particpant.xpath('div[@class="menber-info"]/ul/li/span/em/text()')[0].replace('参加过', '').replace('场',
                                                                                                                   '')
        p_result = particpant.xpath('div[@class="menber-raceinfo"]/div/span/text()')[0].replace('\n', '').replace(' ',
                                                                                                                  '')
        p_result_state = particpant.xpath('div[@class="menber-raceinfo"]/div/div/text()')
        if p_result_state != []:
            p_result_info = p_result_state[0].replace('\n', '').replace(' ', '')
        else:
            p_result_info = 'null'
        p_comment_state = particpant.xpath('div[@class="menber-raceinfo"]/div[@class="menbercomment"]')
        if p_comment_state != []:
            p_comment = p_comment_state[0].xpath('string(.)').replace('\n', '').replace(' ', '')
        else:
            p_comment = 'null'

        id.append(p_id)
        name.append(p_name)
        stats.append(p_stats)
        result.append(p_result)
        result_info.append(p_result_info)
        comment.append(p_comment)

    return id, name, stats, result, result_info, comment


