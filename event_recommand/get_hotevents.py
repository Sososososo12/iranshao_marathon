import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re

race_id=[]
race_name=[]
race_location=[]
race_time=[]
race_following=[]
hotevent_page_based='http://iranshao.com/bundled_races?page={}&sort=hot'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}

def getHotEvent(pagenum):
    id=[]
    name=[]
    location=[]
    time=[]
    following=[]
    url = hotevent_page_based.format(str(pagenum))
    html = requests.get(url, headers=headers).content.decode('utf-8')

    selector = etree.HTML(html)
    item = selector.xpath('//div[@class="raceitems"]/div')
    for race in item:
        event_id = race.xpath('div/div[@class="itemname"]/strong/a/@href')[0]
        event_name = race.xpath('div/div[@class="itemname"]/strong/a/text()')[0].replace('\n', '')
        event_location = race.xpath('div/div[@class="attr"]/text()')[0]
        event_time = race.xpath('div/span[@class="itemtime"]/text()')[0]
        event_following = race.xpath('div/div[@class="attr"]/span/text()')[0].replace('人关注','')
        id.append(event_id)
        name.append(event_name)
        location.append(event_location)
        time.append(event_time)
        following.append(event_following)
    print('第'+str(pagenum)+'页的赛事信息已获取完成！')
    return id,name,location,time,following

for pagenum in range(1,199):
    raceinfo_tuple=getHotEvent(pagenum)
    race_id.extend(raceinfo_tuple[0])
    race_name.extend(raceinfo_tuple[1])
    race_location.extend(raceinfo_tuple[2])
    race_time.extend(raceinfo_tuple[3])
    race_following.extend(raceinfo_tuple[4])
    time.sleep(5)

data1 = pd.DataFrame({'race_id':race_id,
                      'race_name':race_name,
                      'race_location':race_location,
                      'race_time':race_time,
                      'race_follwoing':race_following

                      })
data1.to_excel(u'race_info_test.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')

