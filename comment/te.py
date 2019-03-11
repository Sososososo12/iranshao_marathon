import requests
import time
import os
from lxml import etree
import urllib3

# url='http://iranshao.com/races/859/comments?page=1'
# http = urllib3.PoolManager()
# r = http.request('GET', url)
# htmlcontent = r.data.decode('utf-8')

loadingtxt=open('./te1.txt',encoding='UTF-8')
content=loadingtxt.read()
    # f.close()
selector=etree.HTML(content)
items=selector.xpath('//ol[@id="race_comment_tab"]/li')
print(items)
for eachitem in items:
    person_url=eachitem.xpath('h4/a/@href')[0]

    paragrarh = ''
    paragrarh_txt=eachitem.xpath('div[@class="comment-body"]')
    if paragrarh_txt!=[]:
        paragrarh=paragrarh_txt[0].xpath('string(.)').replace('\n','')

    score1 = '0'
    score2 = '0'
    score3 = '0'

    event_score = eachitem.xpath('div[@class="comment-score"]/span[@class="scores"]/span[@class="score-item"]/span')
    print(event_score)
    if event_score != []:
        score1 = event_score[1].xpath('@data-score')[0]
        score2 = event_score[3].xpath('@data-score')[0]



    print(1)
# print(htmlcontent)