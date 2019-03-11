import re
import requests
from lxml import etree
import pandas as pd
import time
import urllib3
# import loading_province



based_url='http://iranshao.com/'
based_url2='http://iranshao.com/races/{}/racers?page={}&type=done'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
          }


def getEnperson_items(eventid):
    persons_id=[]
    persons_site=[]

    # url = based_url + '/' + str(enentid) + '/racers?type=done'
    # html = requests.get(url, headers=headers).text
    # selector = etree.HTML(html)
    # # 首先获得参与过该赛事的用户页数 page_num
    # enperson_page_number = selector.xpath('//ul[@class="pagination pagination-v1"]/li/a/text()')[10]
    # print(enperson_page_number)
    for i in range(1,6):
        surl=based_url2.format(str(eventid),str(i))
        html2=requests.get(surl,headers=headers).text
        selector = etree.HTML(html2)
        enperson_site = selector.xpath('//ol[@class="menber-cards"]/li/div//h2/a/@href')
        for person_items in enperson_site:
            id=person_items.replace('/people/','')
            enperson_site_index = based_url +person_items+'/races'
            persons_id.append(id)
            persons_site.append(enperson_site_index)

        print('loading page num '+str(i))
        time.sleep(3)

    data1 = pd.DataFrame({'persons_id': persons_id,
                          'persons_site': persons_site,
                          })

    data1.to_excel(u'persons_index_{}.xls'.format(eventid), index=False, encoding='"utf_8_sig')
    print('信息写入完成！')
    return persons_id





def getenperson_Article_Site(persons_id_d):
    persons_id_based=['96288955ad','183509bae4','isabel_zhang','wu-xi-ai-pao','mai-gong-xia-mi']
    person_url_based='http://iranshao.com/people/{}/diaries'
    ids=[]
    number=[]
    for item in persons_id_d:

        person_url=person_url_based.format(item)
        http = urllib3.PoolManager()
        r = http.request('GET', person_url)
        htmlcontent=r.data.decode('utf-8')
        # html = requests.get(person_url, headers=headers).text
        selector = etree.HTML(htmlcontent)
        enperson_items = selector.xpath('//div[@class="tabbable-line"]/ul/li/a/text()')[0]
        enperson_article_num=enperson_items.replace('\n','')
        enperson_article_num=re.findall('已发表\((.*?)\)',enperson_article_num)[0]
        ids.append(item)
        number.append(int(enperson_article_num))

        print('loading page id ' + item)
        time.sleep(5)

    data1 = pd.DataFrame({'persons_id': ids,
                          'persons_article_num': number,
                          })

    data1.to_excel(u'persons_article_num.xls', index=False, encoding='"utf_8_sig')
    print('信息写入完成！')
    return 'finish！'






getenperson_Article_Site(getEnperson_items(583))











# for each in events:
#     title=each.xpath('div/div[@class="itemname"]/strong/a/text()')[0]
#     u_url=each.xpath('div/div/strong/a/@href')
#     nameid=u_url[0].replace('/races/','')
#     url1 = start_url + u_url[0].replace('\'', '')
#     rawlocation=each.xpath('div/div[@class="attr"]/text()')[0]
#     location=rawlocation.replace('\n','').replace(' ','')
#     racetime=each.xpath('div[@class="col-md-2"]/span/text()')[0]
#     raw_intertime=each.xpath('div[@class="col-md-3 text-center"]/div[@class="inter-time"]/text()')[0]
#     intertime=raw_intertime.replace('\n','').replace(' ','')
#     orderrcon=each.xpath('div[@class="col-md-3 text-center"]/div/a/text()')
#
#     if(len(orderrcon)==1):
#         ordercon = str(orderrcon[0])
#         a = len(ordercon)
#         if (a == 4):
#             ordercon = '报名中'
#     else:ordercon = '报名已截止'
#     print(ordercon)

