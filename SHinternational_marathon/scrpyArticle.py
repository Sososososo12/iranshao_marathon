import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import time

article_site_based='http://iranshao.com/diaries/'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"}


class getPersonArticle():
    def getDairies_sites(self,enperson_id):
        person_url_based = 'http://iranshao.com/people/{}/diaries'
        http = urllib3.PoolManager()
        r = http.request('GET', person_url_based.format(enperson_id))
        htmlcontent = r.data.decode('utf-8')
        selector = etree.HTML(htmlcontent)
        allarticle_num = selector.xpath('//ol[@class="comments approved-content"]/li/@data-diary-id')
        return allarticle_num

    def getArticle(self,article_id):
        articles = ''
        for each_article_id in article_id:
            article_url = article_site_based + each_article_id
            str_info = ''
            html = requests.get(article_url, headers=headers).text
            selector = etree.HTML(html)
            items = selector.xpath('//div[@class="mod-article-bd"]/div')
            for i in range(0, len(items)):
                itemspec = items[i].xpath('string(.)')
                itemspec = itemspec.replace('\n', '')
                itemspec = itemspec.replace('\u3000', '')
                itemspec = itemspec.replace('\r', '')
                itemspec = itemspec.replace('\xa0', '')
                str_info = str_info + itemspec
            print(str_info)
            articles = articles + str_info
            articles.replace('\n', '')
            time.sleep(5)
        print(articles)

        return articles

    def downloadingTxt(self,article_str, enperson_id):
        outputs = open('./{}_articles.txt'.format(enperson_id), 'w', encoding='utf-8')
        outputs.write(article_str)
        outputs.close()





