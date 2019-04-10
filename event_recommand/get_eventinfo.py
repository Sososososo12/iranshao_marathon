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

item=1985
url=event_based_url.format(str(item))
html=requests.get(url,headers=headers).content.decode('utf-8')
# print(html.decode('utf-8'))
selector=etree.HTML(html)
event_name=selector.xpath('//div[@class="racememu hidden-xs"]/div/h1/a/text()')[0].replace('\n','').replace(' ','')
event_localtion=selector.xpath('//div[@class="race-his"]/p/text()')[0].replace('\n','').replace(' ','')
event_score=selector.xpath('//section[@class="race-scores"]/div/span/@data-score')[0]
event_summary=selector.xpath('//div[@class="race-info"]/p/text()')[0]
event_followed=selector.xpath('//div[@class="race-menbers"]/p/span/em/text()')[0]
event_panticipant=selector.xpath('//div[@class="race-menbers"]/p/span/em/text()')[1]
event_comment_state=selector.xpath('//div[@id="racecomments"]/div/h2/span/a/span/text()')
if event_comment_state!=[]:
    event_comment = event_comment_state[0]
else:
    event_comment = '赛事评论少于5条'
event_diaries_state=selector.xpath('//div[@id="racediary"]/div/h2/span/a/span/text()')
if event_diaries_state!=[]:
    event_diaries=event_diaries_state[0]
else:
    event_diaries=selector.xpath('//div[@id="racediary"]/div/h2/span/span/text()')[0]

print(event_name)
print(event_localtion)
print(event_score)
print(event_summary)
print(event_followed)
print(event_panticipant)
print(event_comment)
print(event_diaries)
