import requests
from lxml import etree
import pandas as pd
import time
from test import loading_province

name_province= loading_province.names
url_province= loading_province.provinces
ids=[]
titles=[]
urls=[]
locations=[]
racetimes=[]
intertimes=[]
ordercons=[]
photocons=[]
follownums=[]
allurls=[]
ordercon='yiban'

print('开始构建网址...')

first_url='http://iranshao.com'
start_url='http://iranshao.com/bundled_races?&region=%E6%B5%99%E6%B1%9F%E7%9C%81&region_scope=china&sort=time&page='

for urlnum in range(1,23):
    print('开始读取信息...')

    testurl = 'http://iranshao.com/bundled_races?&region=%E6%B5%99%E6%B1%9F%E7%9C%81&region_scope=china&sort=time&page=1'
    html = requests.get(start_url+str(urlnum)).text
    # print(html)
    selector = etree.HTML(html)
    events = selector.xpath('//div[@class="race-itemlist race-search-item clearfix "]')
    # print(events)
    for each in events:
        title = each.xpath('div/div[@class="itemname"]/strong/a/text()')[0]
        u_url = each.xpath('div/div/strong/a/@href')
        nameid = u_url[0].replace('/races/', '')
        url1 = first_url + u_url[0].replace('\'', '')
        rawlocation = each.xpath('div/div[@class="attr"]/text()')[0]
        location = rawlocation.replace('\n', '').replace(' ', '')
        racetime = each.xpath('div[@class="col-md-2"]/span/text()')[0]
        raw_intertime = each.xpath('div[@class="col-md-3 text-center"]/div[@class="inter-time"]/text()')[0]
        intertime = raw_intertime.replace('\n', '').replace(' ', '')
        orderrcon = each.xpath('div[@class="col-md-3 text-center"]/div/a/text()')

        if (len(orderrcon) == 1):
            ordercon = str(orderrcon[0])
            a = len(ordercon)
            if (a == 4):
                ordercon = '报名中'
            elif(a==6):
                ordercon = '报名时间未知'
        else:
            ordercon = '报名已截止'

        photorcon = each.xpath('div/div[@style="padding-top: 12px;"]')[0]
        photorcon2 = photorcon.xpath('a/text()')
        if (len(photorcon2) == 0):
            photocon = 0
        else:
            photocon = 1

        followrnum = each.xpath('div/div/span/text()')[0].replace(' 人关注', '')
        follownum = int(followrnum)

        ids.append(nameid)
        titles.append(title)
        urls.append(url1)
        locations.append(location)
        racetimes.append(racetime)
        intertimes.append(intertime)
        ordercons.append(ordercon)
        photocons.append(photocon)
        follownums.append(follownum)

    print('第' + str(urlnum) + '页信息已读取完成...')
    time.sleep(2)




data1 = pd.DataFrame({'id':ids,
                      'title': titles,
                      'url': urls,
                      'location': locations,
                      'race_time': racetimes,
                      'inter_time': intertimes,
                      'order_condition':ordercons,
                      'photo_condition': photocons,
                      'following_numbers':follownums

                      })
data1.to_excel(u'ZHEJIANG_malathon.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')


