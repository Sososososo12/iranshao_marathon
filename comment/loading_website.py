import requests
import time
import os
from lxml import etree
import urllib3


def loadingWebsite(pagenumber):
    url = 'http://iranshao.com/races/859/comments?page={}'.format(str(pagenumber))
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    htmlcontent = r.data.decode('utf-8')

    output = open('./comment_{}.txt'.format(str(pagenumber)), 'w', encoding='utf-8')
    output.write(htmlcontent)
    output.close()
    print('finish write website ' + str(pagenumber))
    return 0

for page in range(1,159):
    loadingWebsite(page)
    time.sleep(5)
