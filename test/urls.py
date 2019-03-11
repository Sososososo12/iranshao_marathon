import re
import requests
from lxml import etree
import pandas as pd
import time

based_url='http://iranshao.com'
allurls=[]
article_sites=[]
article_person=[]
num=0
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
           "Cookie": "GA1.2.391092334.1539011993; Hm_lvt_e1afc974687855fe8c7318ef56f0dbae=1549099769,1549099793,1551683585; _gid=GA1.2.1786043978.1551683585; remember_user_token=BAhbCFsGaQMW%2FwpJIhl6eG1reXU4cURrYl9xc3YtV3FaMgY6BkVGSSIXMTU1MTc1NDAyMi4wNDU3NTEzBjsARg%3D%3D--7b427c40d57efef4642b297daf5664db41f7fea5; _iranshao_session=BAh7DkkiD3Nlc3Npb25faWQGOgZFVEkiJTRhYWVlYWU3ZmE1MjYwNjU1NzVhYzgyYTA2YWU4MWNhBjsAVEkiEnByZXZpb3VzX3BhdGgGOwBGIh0vcGVvcGxlLzc5YTJmOTg1Y2UvcmFjZXNJIhhwcmV2aW91c19jb250cm9sbGVyBjsARkkiC3Blb3BsZQY7AFRJIh1wcmV2aW91c19jb250cm9sbGVyX3BhdGgGOwBGSSILcGVvcGxlBjsARkkiFHByZXZpb3VzX2FjdGlvbgY7AEZJIgpyYWNlcwY7AFRJIhdwcmV2aW91c19wYXJhbXNfaWQGOwBGSSIPNzlhMmY5ODVjZQY7AFRJIhBfY3NyZl90b2tlbgY7AEZJIjFQaVhENkM5Zm8raW1kMyt5aEhJZFR3Q0hCeTd0V3kxanFZMk1ncUIzZElrPQY7AEZJIhNvbW5pYXV0aC5zdGF0ZQY7AFRJIjUyMzVmZjhkY2QyNTQzZjAwN2Y2MzM4NWJjZWM4NzA3ZjI4OGQ0N2RkYmMxNmI1MGYGOwBGSSIZd2FyZGVuLnVzZXIudXNlci5rZXkGOwBUWwdbBmkDFv8KSSIiJDJhJDEwJDZCbEhIc3JPQmZkNHgybjAuYkcyTGUGOwBU--0b9eb13b9efe2f8dc3be7318bec70aab1ecc756c; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%225c9bb41e71%22%2C%22%24device_id%22%3A%2216654435d292-061433cf037987-8383268-1327104-16654435d2a262%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216654435d292-061433cf037987-8383268-1327104-16654435d2a262%22%7D; _gat=1",
           "Upgrade-Insecure-Requests": 1,
          }
start_url='http://iranshao.com/races/583/diaries'
html=requests.get(start_url).text
selector = etree.HTML(html)
enperson_site = selector.xpath('//div[@class="item"]/div/a/@href')
for item in enperson_site:
    num=num+1
    if (num % 2)!=0:
        article_sites.append(based_url+item)
    else:
        article_person.append(based_url+item)
    time.sleep(3)
    print('loading info '+str(num))
# print(len(enperson_site))

data1 = pd.DataFrame({'article': article_sites,
                    'persons': article_person,
                          })

data1.to_excel(u'article_site.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')

