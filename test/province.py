import requests
from lxml import etree
import pandas as pd
import re
import time

# urls_province=[]
name_provinces=[]
url_provinces=[]
region_datas=[]
page_number=[]

start_url='http://iranshao.com/bundled_races?page=1&region_scope=china'
first_url='http://iranshao.com'
html=requests.get(start_url).text
# print(html)
selector=etree.HTML(html)
provinces=selector.xpath('//div[@class="sub-filter clearfix"]/span[@class="word "]')
for each_provinces in provinces:
    name_province=each_provinces.xpath('a/text()')[0]

    last_url=each_provinces.xpath('a/@href')[0]
    region_data=re.findall('region=(.*?)&region_scope',last_url)[0]
    url_province = first_url + last_url

    regionhtml=requests.get(url_province).text
    selector2=etree.HTML(regionhtml)
    page_events = selector2.xpath('//div[@class="pagination-holder"]/ul/li')
    if(len(page_events)==0):
        pagenum = page_events[len(page_events) - 2].xpath('a/text()')[0]

    name_provinces.append(name_province)
    url_provinces.append(url_province)
    region_datas.append(region_data)
    page_number.append(pagenum)

    print('已读取完 '+name_province+' 的信息')
    # time.sleep(2)

data1 = pd.DataFrame({'name_province':name_provinces,
                      'url_province':url_provinces,
                      'region_data':region_datas,
                      'page_number':page_number
                      })

data1.to_excel(u'url of provinces.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')
