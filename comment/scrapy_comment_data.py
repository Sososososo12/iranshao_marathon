import requests
import time
import os
from lxml import etree
import urllib3
import pandas as pd

person_urls=[]
paragraph_all=[]
score1_all=[]
score2_all=[]
score3_all=[]

def scrapyCommentData(pagenumber):

    loadingtxt = open('./comment_{}.txt'.format(str(pagenumber)), encoding='UTF-8')
    content = loadingtxt.read()
    # f.close()
    selector = etree.HTML(content)
    items = selector.xpath('//ol[@id="race_comment_tab"]/li')
    # print(items)
    for eachitem in items:
        person_url = eachitem.xpath('h4/a/@href')[0]
        person_urls.append(person_url)
        paragrarh = ''
        paragrarh_txt = eachitem.xpath('div[@class="comment-body"]')
        if paragrarh_txt != []:
            paragrarh = paragrarh_txt[0].xpath('string(.)').replace('\n', '')
        paragraph_all.append(paragrarh)

        score1='0'
        score2 = '0'
        score3 = '0'

        event_score = eachitem.xpath('div[@class="comment-score"]/span[@class="scores"]/span[@class="score-item"]/span')
        print(event_score)
        if event_score!=[]:
            score1 = event_score[1].xpath('@data-score')[0]
            if len(event_score) > 2:
                score2 = event_score[3].xpath('@data-score')[0]
            if len(event_score) > 4:
                score3 = event_score[5].xpath('@data-score')[0]
        score1_all.append(score1)
        score2_all.append(score2)
        score3_all.append(score3)

    print('success loading pagenumber '+str(pagenumber))
    return 0

for page in range(1,159):
    scrapyCommentData(page)
print('finish loading all pages')
print(len(person_urls))
print(len(paragraph_all))
print(len(score1_all))
print(len(score2_all))
print(len(score3_all))

data1 = pd.DataFrame({'person_url': person_urls,
                      'paragragh': paragraph_all,
                      'score1_sight':score1_all,
                      'score2_organize':score2_all,
                      'score3_atomsphere':score3_all
                    })

data1.to_excel(u'hangzhou_comment.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')


