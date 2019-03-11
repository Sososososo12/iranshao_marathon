import re
import requests
from lxml import etree
from newtxt import  create_article_to_txt

url='http://iranshao.com/diaries/215642'
html=requests.get(url).text
# print(html)
create_article_to_txt(12345,html)

