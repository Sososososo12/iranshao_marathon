import requests
import re
from lxml import etree

based_url='http://iranshao.com'
start_url='http://iranshao.com/races/583/diaries'
enperson_page='http://iranshao.com/races/583/racers?type=done'
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}

class scrapyEvents():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
    def get_Enperson_Number(url):
        html = requests.get(url, headers=headers).text
        selector = etree.HTML(html)
        enperson_number = selector.xpath('//div[@class="num"]/a/text')[0]
        if int(enperson_number) > 0:
            return enperson_number
        else:
            enperson_number = 0
            return enperson_number

    def get_Enperson_items(enentid):
        url=based_url+'/'+str(enentid)+'/racers?type=done'
        html = requests.get(url, headers=headers).text
        selector = etree.HTML(html)
        # 首先获得参与过该赛事的用户页数 page_num
        enperson_number = selector.xpath('//ul[@class="num"]/a/text')[0]






