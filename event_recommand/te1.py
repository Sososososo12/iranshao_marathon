import requests
import urllib3
import xlwt
import xlrd
import os
from lxml import etree
import pandas as pd
import time
import re
from event_recommand import get_Pfollowing_event

# a1=[]
# a2=[]
# a3=[]
# a=([1,2,3],['a','b','c'],['as','as','as'])
# # print(a)
# a1.extend(a[0])
# a2.extend(a[1])
# a3.extend(a[2])
# print(a1,a2,a3)


user_id=[]
event_id=[]
event_name=[]
user_info=get_Pfollowing_event.getPFInfo('acelei000')
# 运行后返回的是个tuple，里面是多个返回的值（list）
# 给每一个总list加上读取到的tuple中的对应list
user_id.extend(user_info[0])
event_id.extend(user_info[1])
event_name.extend(user_info[2])

data1 = pd.DataFrame({'p_id':user_id,
                      'id':event_id,
                      'name':event_name,

                      })
data1.to_excel(u'acc_info.xls', index=False, encoding='"utf_8_sig')
print('信息写入完成！')