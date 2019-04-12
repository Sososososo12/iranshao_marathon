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

event_based_url='http://iranshao.com/races/{}'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}

def getRaceInfo(race_id):
    event_id=race_id

    url = event_based_url.format(str(race_id))
    html = requests.get(url, headers=headers).content.decode('utf-8')
    # print(html.decode('utf-8'))

    selector = etree.HTML(html)
    event_website_state=selector.xpath('//div[@class="racememu hidden-xs"]/div/h1')
    if event_website_state!=[]:
        event_name_state = selector.xpath('//div[@class="racememu hidden-xs"]/div/h1/a/text()')
        if event_name_state != []:
            event_name = event_name_state[0].replace('\n', '').replace(' ', '')
        else:
            event_name = 'null'
        event_location_state = selector.xpath('//div[@class="race-his"]/p/text()')
        if event_location_state != []:
            event_location = event_location_state[0].replace('\n', '').replace(' ', '')
        else:
            event_location = 'null'
        event_score = selector.xpath('//section[@class="race-scores"]/div/span/@data-score')[0]
        event_summary_state = selector.xpath('//div[@class="race-info"]/p/text()')
        if event_summary_state != []:
            event_summary = event_summary_state[0]
        else:
            event_summary = 'null'
        event_followed = selector.xpath('//div[@class="race-menbers"]/p/span/em/text()')[0]
        event_participant = selector.xpath('//div[@class="race-menbers"]/p/span/em/text()')[1]
        event_comment_state = selector.xpath('//div[@id="racecomments"]/div/h2/span/a/span/text()')
        if event_comment_state != []:
            event_comment = event_comment_state[0]
        else:
            event_comment = '赛事评论少于5条'
        event_diaries_state = selector.xpath('//div[@id="racediary"]/div/h2/span/a/span/text()')
        if event_diaries_state != []:
            event_diaries = event_diaries_state[0]
        else:
            event_diaries = selector.xpath('//div[@id="racediary"]/div/h2/span/span/text()')[0]
    else:
        event_name='null'
        event_location='null'
        event_score='null'
        event_summary='null'
        event_followed='null'
        event_participant='null'
        event_comment='null'
        event_diaries='null'


    print('id为'+str(race_id)+'的赛事信息已获取完成！')
    return event_id,event_name,event_location,event_score,event_summary,event_followed,event_participant,event_comment,event_diaries


# getRaceInfo(11656)