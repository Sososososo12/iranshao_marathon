import re
import requests
from lxml import etree
import os
# import loading_site_excel

str_info=[]
url='http://iranshao.com/diaries/382324'
html=requests.get(url).text
selector = etree.HTML(html)
items = selector.xpath('//div[@class="mod-article-bd"]/div')
for i in range(0, len(items)):
    itemspec=items[i].xpath('string(.)')
    itemspec=itemspec.replace('\n','')
    itemspec = itemspec.replace('\u3000', '')
    itemspec = itemspec.replace('\r', '')
    str_info.append(itemspec)
print(str_info)