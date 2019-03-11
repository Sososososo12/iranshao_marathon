import re
import requests
from lxml import etree
import pandas as pd
import loading_txt

# shm_url='http://iranshao.com/races/583'
# html=requests.get(shm_url).text
# print(html)
# 开始对详情信息框架表进行锁定
selector = etree.HTML(loading_txt.web_detail)
events = selector.xpath('//div[@id="race_detail_tab1"]')[0]
# 开始对对应的详情信息进行锁定
shm_detail=events.xpath('div/dl/dd/text()')
shm_detail2=events.xpath('div/dl/dd')
print(len(shm_detail2))
for i in shm_detail2:
    print(str(i[0]))
# print(len(shm_detail))
# for i in shm_detail:
#     print(i)