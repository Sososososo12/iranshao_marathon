from lxml import etree
import requests
import pandas as pd
import time
import os
import re
import urllib3

id=[]
name=[]

f = open('following2.txt','r', encoding='UTF-8')
web_detail=f.read()
# print(web_detail)
selector=etree.HTML(web_detail)
r_item=selector.xpath('//div[@class="feed-content"]/div/div/div/h3')
for itemnum in range(len(r_item)):
    r_id=r_item[itemnum].xpath('a/@href')[0].replace(r'/races/', '')
    r_name=r_item[itemnum].xpath('a/text()')[0]
    id.append(r_id)
    name.append(r_name)
# for num in range(4):
    # r_id[num]=r_id[num].replace(' ','').replace(r'\n','')
    # r_name[num]=r_name[num].replace(r'\"/races/', '').replace(r'\"', '')
    # id.append(r_id[num].replace(' ','').replace(r'\n',''))
    # name.append(r_name[num].replace(r'\"/races/','').replace(r'\"',''))
# item=re.findall('<a href=(.*?)<\/a>',web_detail)
# print(r_name[0])
# print(r_id[0])

# a=27//4
# print(a+1)
data1 = pd.DataFrame({'id':id,
                      'name':name,

                      })
data1.to_excel(u'aac.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')